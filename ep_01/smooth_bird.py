import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 400
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Bird properties
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Pipe properties
PIPE_WIDTH = 70
PIPE_GAP = 200
pipe_x = WIDTH
pipe_height = random.randint(100, 400)

# Game variables
score = 0
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.rect(SCREEN, GREEN, (x, y, BIRD_WIDTH, BIRD_HEIGHT))

def draw_pipe(x, height):
    pygame.draw.rect(SCREEN, GREEN, (x, 0, PIPE_WIDTH, height))
    pygame.draw.rect(SCREEN, GREEN, (x, height + PIPE_GAP, PIPE_WIDTH, HEIGHT - height - PIPE_GAP))

def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over!", True, BLACK)
    SCREEN.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 18))
    pygame.display.flip()
    pygame.time.wait(2000)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP_STRENGTH

    # Update bird position
    bird_y += bird_velocity
    bird_velocity += GRAVITY

    # Move pipe
    pipe_x -= 3
    if pipe_x < -PIPE_WIDTH:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Check for collisions
    if bird_y < 0 or bird_y > HEIGHT - BIRD_HEIGHT:
        game_over()
        running = False
    
    if pipe_x < bird_x + BIRD_WIDTH < pipe_x + PIPE_WIDTH:
        if bird_y < pipe_height or bird_y + BIRD_HEIGHT > pipe_height + PIPE_GAP:
            game_over()
            running = False

    # Draw everything
    SCREEN.fill(WHITE)
    draw_bird(bird_x, bird_y)
    draw_pipe(pipe_x, pipe_height)
    show_score()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
