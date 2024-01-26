import pygame
x = pygame.init()
window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My PyGame")

game_exist = False

while not game_exist:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exist = True

        #is any key pressed
        if event.type == pygame.KEYDOWN:
            #if pressed then check is it the 1 number key
            if event.key == pygame.K_1:
                print("You enter 1")

pygame.quit()
quit()