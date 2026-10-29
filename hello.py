import random
import sys

GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 4

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)

DIRECTIONS = {
    "R": RIGHT,
    "L": LEFT,
    "U": UP,
    "D": DOWN,
}

OPPOSITE = {
    RIGHT: LEFT,
    LEFT: RIGHT,
    UP: DOWN,
    DOWN: UP,
}


class SnakeGame:
    def __init__(self):
        self.snake = [(5, 5)]  # Head is the first coordinate.
        self.direction = RIGHT
        self.score = 0
        self.game_over = False
        self.food_index = 0
        self.food = (7, 5)

    def new_food(self):
        """Use the assignment's fixed test food first, then random food."""
        if self.food_index == 0:
            self.food = (7, 5)
        elif self.food_index == 1:
            self.food = (0, 0)
        else:
            empty_cells = [
                (x, y)
                for x in range(GRID_SIZE)
                for y in range(GRID_SIZE)
                if (x, y) not in self.snake
            ]
            if not empty_cells:
                self.game_over = True
                return
            self.food = random.choice(empty_cells)

    def change_direction(self, key):
        """Change direction unless the key is invalid or reverses movement."""
        key = key.upper()
        if key not in DIRECTIONS:
            return "Invalid key. Use R, L, U or D"

        new_direction = DIRECTIONS[key]
        if new_direction == OPPOSITE[self.direction]:
            return "Reverse move not allowed. Snake continues " + self.direction_name()

        self.direction = new_direction
        return None

    def direction_name(self):
        return {
            RIGHT: "Right",
            LEFT: "Left",
            UP: "Up",
            DOWN: "Down",
        }[self.direction]

    def move(self):
        """Move one cell and detect food, wall, and self collisions."""
        if self.game_over:
            return None

        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Wall collision: coordinates must remain between 0 and 9.
        x, y = new_head
        if not (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE):
            self.game_over = True
            return f"Game Over! Wall hit at {new_head}"

        eating = new_head == self.food

        # If not eating, the tail moves away, so it is excluded from collision
        # detection. If eating, the tail remains and all segments count.
        body_to_check = self.snake if eating else self.snake[:-1]
        if new_head in body_to_check:
            self.game_over = True
            return f"Game Over! Self-collision at {new_head}"

        self.snake.insert(0, new_head)

        if eating:
            self.score += 10
            self.food_index += 1
            self.new_food()
            # Do not remove the tail: this makes the snake grow by one segment.
            return f"Food eaten at {new_head}!"
        else:
            self.snake.pop()
            return None


def run_tests():
    """Run the four test cases described in the assignment sheet."""
    print("SNAKE GAME - CONSOLE TESTS")
    print("=" * 34)

    # Test Case 1: Normal input
    game = SnakeGame()
    for key in ("R", "R"):
        game.change_direction(key)
        message = game.move()
        if message:
            print(message)
    print("\nTest Case 1: Moves R, R")
    print(f"Head: {game.snake[0]}")
    print(f"Score: {game.score} | Length: {len(game.snake)} | Head: {game.snake[0]}")

    # Test Case 2: Boundary / minimum input
    game = SnakeGame()
    print("\nTest Case 2: Moves R, R, R, R, R")
    for key in ("R", "R", "R", "R", "R"):
        game.change_direction(key)
        message = game.move()
        if message:
            print(message)
        if game.game_over:
            break
    print(f"Final score: {game.score}")

    # Test Case 3(a): Invalid key
    game = SnakeGame()
    print("\nTest Case 3(a): Key X")
    print(game.change_direction("X"))

    # Test Case 3(b): Reverse key while moving Right
    print("\nTest Case 3(b): Key L while snake is moving Right")
    print(game.change_direction("L"))
    print(f"Current direction: {game.direction_name()}")

    # Test Case 4: Different valid scenario
    game = SnakeGame()
    print("\nTest Case 4: Moves R, R, U, U")
    for key in ("R", "R", "U", "U"):
        error = game.change_direction(key)
        if error:
            print(error)
            continue
        message = game.move()
        if message:
            print(message)
        if game.game_over:
            break
    print(f"Snake: {game.snake}")
    print(f"Length: {len(game.snake)} | Head: {game.snake[0]}")
    print("\nAll four test scenarios completed.")


def run_graphical_game():
    try:
        import pygame
    except ImportError:
        print("Pygame is not installed. Install it using: pip install pygame")
        return

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 70))
    pygame.display.set_caption("Snake Game - PS No. 58")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 22)
    small_font = pygame.font.SysFont("arial", 16)

    game = SnakeGame()
    key_map = {
        pygame.K_RIGHT: "R",
        pygame.K_LEFT: "L",
        pygame.K_UP: "U",
        pygame.K_DOWN: "D",
    }

    running = True
    last_message = "Use arrow keys to move. Press ESC to quit."
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif game.game_over and event.key == pygame.K_SPACE:
                    game = SnakeGame()
                    last_message = "New game started."
                elif event.key in key_map and not game.game_over:
                    error = game.change_direction(key_map[event.key])
                    if error:
                        last_message = error

        if not game.game_over:
            message = game.move()
            if message:
                last_message = message

        screen.fill((20, 24, 32))

        # Draw grid lines and board.
        for i in range(GRID_SIZE + 1):
            pygame.draw.line(
                screen, (48, 54, 65),
                (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), 1
            )
            pygame.draw.line(
                screen, (48, 54, 65),
                (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), 1
            )

        # Draw food.
        fx, fy = game.food
        pygame.draw.rect(
            screen, (240, 75, 75),
            (fx * CELL_SIZE + 5, fy * CELL_SIZE + 5,
             CELL_SIZE - 10, CELL_SIZE - 10),
            border_radius=8
        )

        # Draw snake, with a different colour for the head.
        for index, (sx, sy) in enumerate(game.snake):
            color = (90, 220, 130) if index == 0 else (45, 170, 100)
            pygame.draw.rect(
                screen, color,
                (sx * CELL_SIZE + 3, sy * CELL_SIZE + 3,
                 CELL_SIZE - 6, CELL_SIZE - 6),
                border_radius=7
            )

        pygame.draw.rect(
            screen, (35, 40, 50),
            (0, WINDOW_SIZE, WINDOW_SIZE, 70)
        )
        score_text = font.render(
            f"Score: {game.score}    Length: {len(game.snake)}",
            True, (255, 255, 255)
        )
        screen.blit(score_text, (10, WINDOW_SIZE + 5))

        status = "GAME OVER! Press SPACE to restart." if game.game_over else last_message
        status_text = small_font.render(status[:70], True, (235, 235, 235))
        screen.blit(status_text, (10, WINDOW_SIZE + 38))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        run_graphical_game()