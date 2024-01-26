import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Colors
white = (24, 163, 156)
red = (255, 0, 0)
black = (0, 0, 0)


# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

welcome_image = pygame.image.load("welcome.png")
welcome_image = pygame.transform.scale(welcome_image,(screen_width,screen_height)).convert_alpha()
playing_page = pygame.image.load("play.jpg")
playing_page = pygame.transform.scale(playing_page,(screen_width,screen_height)).convert_alpha()
game_over_page = pygame.image.load("gameOver.png")
game_over_page = pygame.transform.scale(game_over_page,(screen_width,screen_height)).convert_alpha()


# Game Title
pygame.display.set_caption("My Snake Game")
pygame.display.update()


font = pygame.font.SysFont("monospace",30)
def text_screen(score,color,x,y):
    screen_text = font.render(score,True,color)
    gameWindow.blit(screen_text,[x,y])


def make_snake(gameWindow,color,snk_list, snake_size):
    for x,y in snk_list:
        #print(snk_list)

        pygame.draw.rect(gameWindow, color, [x,y, snake_size, snake_size])

clock = pygame.time.Clock()

def welcome_page():
    pygame.mixer.music.load("welcomepage.mp3")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(welcome_image,(0,0))
        text_screen("Welcome to Snake Game.Press Space Bar to Play",(255,255,255),40,40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("Beep Short .mp3")
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()

# Game Loop
def game_loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snake_size = 30
    fps = 50


    snk_list = []
    snk_len = 1

    with open("highscore.txt",'r') as f:
        h_score = f.read()

    food_x = random.randint(20, screen_width-50)
    food_y = random.randint(50, screen_height-50)
    score = 0
    while not exit_game:
        if game_over:
            with open("highscore.txt", 'w') as f:
                f.write(str(h_score))
            gameWindow.fill(white)
            gameWindow.blit(game_over_page,(0,0))
            #text_screen("Game over!Please enter to continue.",red,100,150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.key == pygame.K_BACKSPACE:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                pygame.mixer.music.load("Beep Short .mp3")
                pygame.mixer.music.play()

                score += 10
                #print("Score :",score)
                #print(food_x,food_y)
                food_x = random.randint(20, screen_width-50)
                food_y = random.randint(50, screen_height-50)
                snk_len =snk_len+5

                if score>int(h_score):
                    h_score = score
                    fps = 90

            gameWindow.fill(white)
            gameWindow.blit(playing_page,(0,0))
            text_screen("Score :" + str(score)+"  Highscore"+str(h_score), (255,255,255), 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            #print("head",head)

            if len(snk_list)>snk_len:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load("Stomach Thumps.mp3")
                pygame.mixer.music.play()
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load("Stomach Thumps.mp3")
                pygame.mixer.music.play()
                game_over = True
                #print("Game Over")



            make_snake(gameWindow,black,snk_list, snake_size)
        #pygame.draw.rect(gameWindow, black, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome_page()

