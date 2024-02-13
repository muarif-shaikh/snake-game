import pygame
import random

player_score = 0

# Define game constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 8

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Create the game clock
clock = pygame.time.Clock()

# Define helper functions
def draw_cell(x, y, color):
    pygame.draw.rect(window, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def generate_food(snake):
    while True:
        food_x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
        food_y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
        if (food_x, food_y) not in snake:
            return (food_x, food_y)

# Initialize game state
snake = [(WINDOW_WIDTH // CELL_SIZE // 2, WINDOW_HEIGHT // CELL_SIZE // 2)]
food = generate_food(snake)
direction = 'right'

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

    # Move the snake
    head_x, head_y = snake[-1]
    if direction == 'left':
        head_x -= 1
    elif direction == 'right':
        head_x += 1
    elif direction == 'up':
        head_y -= 1
    elif direction == 'down':
        head_y += 1

    # Check for collision with walls
    if head_x < 0 or head_x >= WINDOW_WIDTH // CELL_SIZE or head_y < 0 or head_y >= WINDOW_HEIGHT // CELL_SIZE:
        pygame.quit()
        print("Your Score : "+str(player_score))
        quit()
        

    # Check for collision with snake body
    if (head_x, head_y) in snake:
        pygame.quit()
        print("Your Score : "+str(player_score))
        quit()

    # Check for collision with food
    if (head_x, head_y) == food:
        food = generate_food(snake)
        player_score += 1
    else:
        snake.pop(0)

    # Add the new head to the snake
    snake.append((head_x, head_y))

    # Draw the game board
    window.fill(BLACK)
    for cell in snake:
        draw_cell(cell[0], cell[1], GREEN)
    draw_cell(food[0], food[1], RED)
    pygame.display.update()

    # Wait for the next frame
    clock.tick(FPS)
