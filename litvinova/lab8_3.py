import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

mode = "rect"
color = colorRED

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

#calculating cirle radius and center
def calculate_circle(x1, y1, x2, y2):
    center = ((x1 + x2) // 2, (y1 + y2) // 2)  
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2  
    return center, radius

#drawing by mode
def draw_by_mode(mode, x, y):
    if mode == "rect":
        pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
    elif mode == "circle":
        center, radius = calculate_circle(prevX, prevY, currX, currY)
        pygame.draw.circle(screen, color, center, radius, THICKNESS)
    elif mode == "eraser":
        pygame.draw.circle(screen, colorBLACK, (x, y), THICKNESS)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                screen.blit(base_layer, (0, 0))
                # drawing depending on mode
                if mode in ["rect", "circle"]:
                    draw_by_mode(mode, currX, currY)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            # drawing depending on mode
            if mode in ["rect", "circle"]:
                draw_by_mode(mode, currX, currY)
                base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

        #erasing
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            currX, currY = event.pos
            if mode == "eraser":  
                draw_by_mode(mode, currX, currY) 
                base_layer.blit(screen, (0, 0))

        #switching mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "rect"
                print("Mode chacnged to: 'rect'")
            if event.key == pygame.K_2:
                mode = "circle"
                print("mode changed to: 'circle'")
            if event.key == pygame.K_3:
                mode = "eraser"
                print("mode changed to: 'eraser'")
            #switching color
            if event.key == pygame.K_r:
                color = colorRED
            if event.key == pygame.K_b:
                color = colorBLUE
            if event.key == pygame.K_w:
                color = colorWHITE
               
    pygame.display.flip()
    clock.tick(60)