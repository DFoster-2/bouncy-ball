import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
ball_radius = 20
ball_color = (250, 250, 250)
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 30, 30
trail_color = (250, 250, 250)
trail_buffer = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_x <= ball_radius or ball_x >= width - ball_radius:
        ball_speed_x *= -1
    if ball_y <= ball_radius or ball_y >= height - ball_radius:
        ball_speed_y *= -1
    trail_buffer.append((ball_x, ball_y))
    trail_buffer = trail_buffer[-1500:]  # Limit trail length
    screen.fill((0, 0, 0))
    for i in range(len(trail_buffer)):
        color = int(255 * (1 - i / len(trail_buffer)))
        pygame.draw.circle(screen, (color, color, color), trail_buffer[i], ball_radius)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
pygame.quit()