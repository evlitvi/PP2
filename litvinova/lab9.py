import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 800))

clockImage = pygame.image.load("clock.png")
minImage = pygame.image.load("min_hand.png")
secImage = pygame.image.load("sec_hand.png")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(clockImage, (0, 0))

    currentTime = time.localtime()
    minutes = currentTime.tm_min
    seconds = currentTime.tm_sec

    minAngle = -(minutes * 6)
    secAngle = -(seconds * 6)

    rotatedMinHand = pygame.transform.rotate(minImage, minAngle)
    rotatedSecHand = pygame.transform.rotate(secImage, secAngle)

    minRect = rotatedMinHand.get_rect(center=(400, 290))
    secRect = rotatedSecHand.get_rect(center=(400, 290))

    screen.blit(rotatedMinHand, minRect.topleft)
    screen.blit(rotatedSecHand, secRect.topleft)

    pygame.display.flip()
    clock.tick(60)


