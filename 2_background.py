from turtle import back
import pygame

pygame.init() 


screen_width = 480
screen_height = 640
screen =pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("Nado game")


background = pygame.image.load("C:/Users/jinsm/OneDrive/デスクトップ/공부관련/Pygame/background.png")

running = True 
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
    screen.blit(background,(0,0)) 

    pygame.display.update() 


pygame.quit()