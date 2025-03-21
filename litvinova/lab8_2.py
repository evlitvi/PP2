import pygame
import time
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

CELL = 30

message_font = pygame.font.SysFont("Verdana", 50)
ingame_font = pygame.font.SysFont("Verdana", 25)

#game over logic
def game_over():
    global running
    game_over_mess = message_font.render("Game Over!", True, "white")
    screen.fill("dodgerblue4")
    screen.blit(game_over_mess, (160, 250))
    pygame.display.flip()
    time.sleep(2)
    running = False

#level up logic
def level_up():
    snake.level += 1
    global FPS
    new_fps = int(FPS*1.2)
    FPS = min(30, new_fps)
    level_up_mess = message_font.render("Level Up!", True, "white")
    screen.blit(level_up_mess, (190, 250))
    pygame.display.flip() 
    pygame.time.delay(2000)


def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, 'gray30', (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = ['white', 'gray30']

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.eaten_fruits = 0 # counting fruits
        self.level = 0 # current level

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, 'red', (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, 'yellow', (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.eaten_fruits += 1 #increasing counter
            food.spawn(self.body) #spawn new fruit
            self.body.append(Point(head.x, head.y))
            if self.eaten_fruits%5==0:
                level_up()

class Food:
    def __init__(self):
        self.spawn([])

    def spawn(self, snake_body): #food would not appear on the snake body
        while True:
            new_pos = Point(random.randint(0, 19), random.randint(0, 19)) #generating new position
            if new_pos not in snake_body: #if food position not on snake we can move on
                self.pos = new_pos #saving new position
                break

    def draw(self):
        pygame.draw.rect(screen, 'green', (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    screen.fill('black')

    draw_grid()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()

    rend_fruits = ingame_font.render(str(snake.eaten_fruits), True, "green")
    screen.blit(rend_fruits, (545, 0))

    rend_level = ingame_font.render(str(snake.level)+' level', True, "hotpink")
    screen.blit(rend_level, (0 , 0))

    #game over if leaving playing area
    if snake.body[0].x > 19 or snake.body[0].x < 0 or snake.body[0].y < 0 or snake.body[0].y > 19:
        game_over()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()