import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    snake_pos[0] += (mouse_pos[0] - snake_pos[0]) * 0.2
    snake_pos[1] += (mouse_pos[1] - snake_pos[1]) * 0.2

    snake_body.insert(0, list(snake_pos))
    if len(snake_body) > 10:
        snake_body.pop()

    screen.fill((10, 10, 10))

    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.display.flip()
    clock.tick(35)
