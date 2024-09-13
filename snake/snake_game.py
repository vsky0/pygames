import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake initialization
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = pygame.K_RIGHT  # Initial direction of the snake
snake_speed = 8  # Speed of the snake

# Food initialization
food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

# Function to draw the snake
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Function to place food
def draw_food():
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                # Prevent the snake from moving in the opposite direction directly
                if (event.key == pygame.K_UP and direction != pygame.K_DOWN) or \
                   (event.key == pygame.K_DOWN and direction != pygame.K_UP) or \
                   (event.key == pygame.K_LEFT and direction != pygame.K_RIGHT) or \
                   (event.key == pygame.K_RIGHT and direction != pygame.K_LEFT):
                    direction = event.key

    # Calculate the new position of the snake's head
    head_x, head_y = snake[0]
    if direction == pygame.K_UP:
        head_y -= CELL_SIZE
    elif direction == pygame.K_DOWN:
        head_y += CELL_SIZE
    elif direction == pygame.K_LEFT:
        head_x -= CELL_SIZE
    elif direction == pygame.K_RIGHT:
        head_x += CELL_SIZE

    # Insert the new head at the beginning of the snake list
    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    # Check for collision with food
    if snake[0] == food:
        # Place new food at a random location
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    else:
        # Remove the last segment of the snake (move forward)
        snake.pop()

    # Check for collisions with walls or self
    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or
            len(snake) != len(set(snake))):  # Check for collisions with self
        running = False

    # Draw everything
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    pygame.display.flip()

    # Control the game speed
    clock.tick(snake_speed)

pygame.quit()
