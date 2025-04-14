import pygame
import time
import random
import psycopg2
#database
conn = psycopg2.connect(
    dbname="Snake",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
#user name and default level
username = input("Enter your username: ")
user_level = 1
#searhing user name
if not username:
    print("Username cannot be empty!")
else:
    #check if user exist
    cur.execute("SELECT user_id FROM UserSnake WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:  #if exist
        user_id = user[0]
        print(f"Welcome back, {username}!")

        # getting level and score
        cur.execute("SELECT user_level, user_score FROM UserScore WHERE user_id = %s", (user_id,))
        info = cur.fetchone()
        user_level = info[0]
        user_score = info[1]
        print(f"Your current level: {user_level}, Score: {user_score}")
    else:  # if user does not exist
        # creating new user
        cur.execute("INSERT INTO UserSnake (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO UserScore (user_id, user_level, user_score) VALUES (%s, %s, %s)", (user_id, 1, 0))  #starting from level 1 and score=0
        print(f"Welcome {username}! Starting with level 1 and score 0.")

    conn.commit()

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

CELL = 30

message_font = pygame.font.SysFont("Verdana", 50)
ingame_font = pygame.font.SysFont("Verdana", 25)

#game pause
def pause_game():
    paused = True

    # saving if score is higher than the previous
    cur.execute("SELECT user_score FROM UserScore WHERE user_id = %s", (user_id,))
    info = cur.fetchone()
    if info[0] < snake.eaten_fruits:
        cur.execute("UPDATE UserScore SET user_level = %s, user_score = %s WHERE user_id = %s", (snake.level, snake.eaten_fruits, user_id))
        conn.commit()
        print("Game paused. Progress saved.")

    pause_message = message_font.render("Paused", True, "white")
    screen.blit(pause_message, (200, 250))
    pygame.display.flip()

    # waiting for player to click 'p' to continue
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

#game over logic
def game_over():
    global running
    game_over_mess = message_font.render("Game Over!", True, "white")
    screen.fill("dodgerblue4")
    screen.blit(game_over_mess, (160, 250))
    #check score
    cur.execute("SELECT user_level, user_score FROM UserScore WHERE user_id = %s", (user_id,))
    info = cur.fetchone()
    if info[1]<snake.eaten_fruits:
        cur.execute("UPDATE UserScore SET user_level=%s, user_score=%s WHERE user_id=%s", (snake.level, snake.eaten_fruits, user_id))  #saving level and score if score is higher
    conn.commit()
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
        self.level = user_level # current level
        self.fruits_for_level_up = 5

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
            self.eaten_fruits += food.value #increasing counter
            food.spawn(self.body) #spawn new fruit
            self.body.append(Point(head.x, head.y))
            #checking eaten fruits for level up
            if self.eaten_fruits >= self.fruits_for_level_up:
                level_up()
                self.fruits_for_level_up +=5

class Food:
    def __init__(self):
        self.spawn([])

    def spawn(self, snake_body): #food would not appear on the snake body
        while True:
            new_pos = Point(random.randint(0, 19), random.randint(0, 19)) #generating new position
            if not any(segment.x == new_pos.x and segment.y == new_pos.y for segment in snake_body): #if food position not on snake we can move on
                self.pos = new_pos #saving new position
                self.value = random.choice([1,2,3])
                self.is_temporary = random.random() < 0.3  # 30% chance for temporary food
                if self.is_temporary:
                    self.expire_time = pygame.time.get_ticks() + 4000
                break

    
    def update(self):
        if self.is_temporary and pygame.time.get_ticks() > self.expire_time:
            self.spawn(snake.body)

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
            #pausing game by 'p'
            if event.key == pygame.K_p:
                pause_game()

    screen.fill('black')

    draw_grid()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()
    food.update()

    rend_fruits = ingame_font.render(str(snake.eaten_fruits), True, "green")
    screen.blit(rend_fruits, (545, 0))

    rend_level = ingame_font.render(str(snake.level)+' level', True, "hotpink")
    screen.blit(rend_level, (0 , 0))

    #game over if leaving playing area
    if snake.body[0].x > 19 or snake.body[0].x < 0 or snake.body[0].y < 0 or snake.body[0].y > 19:
        game_over()

    pygame.display.flip()
    clock.tick(min(30, FPS * 1.2 * user_level))

pygame.quit()