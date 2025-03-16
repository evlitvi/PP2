import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

running = True
clock = pygame.time.Clock()

movement_speed = 20
circle_x = 400
circle_y = 400

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()       
    if pressed_keys[pygame.K_UP] and circle_y > 25:
        circle_y -= movement_speed
    if pressed_keys[pygame.K_DOWN] and circle_y < 775:
        circle_y += movement_speed
    if pressed_keys[pygame.K_RIGHT] and circle_x < 775:
        circle_x += movement_speed
    if pressed_keys[pygame.K_LEFT] and circle_x > 25:
        circle_x -= movement_speed

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (circle_x, circle_y), 25)

    pygame.display.flip()
    clock.tick(60)

