import pygame
import sys
import math
import random
from spritesheet import spritesheet
from spritesheet import Get_text

pygame.init()

WIN = pygame.display.set_mode((600, 600))
WIN_rect = WIN.get_rect()

get_text = Get_text()
score = 0
score_img = get_text.prep_message("Score: " + str(score))

button_image = get_text.prep_message("Play again", (38, 35, 34))
button_bg_image = pygame.surface.Surface((button_image.get_width(), button_image.get_height()))
button_bg_image = get_text.enlarge_image(button_bg_image)
button_bg_image.fill((235, 64, 52))
button_rect = button_image.get_rect()
button_rect.y = 10000

obstacle_image = pygame.image.load("art\_furcorn.png")
obstacle_image = pygame.transform.flip(obstacle_image, True, False)
colorkey = obstacle_image.get_at((0,0))
obstacle_image.set_colorkey(colorkey, pygame.RLEACCEL)
obstacle_rect = obstacle_image.get_rect()
obstacle_rect.x = 1000
obstacle_rect.y = 420

speed = 4

player_ss = spritesheet("art\dino.png")
player_images = player_ss.images_at([[4*24, 0, 24, 24], [5*24, 0, 24, 24], [6*24, 0, 24, 24], [7*24, 0, 24, 24], 
                                     [8*24, 0, 24, 24], [9*24, 0, 24, 24], 
                                     [13*24, 0, 24, 24], [14*24, 0, 24, 24], [15*24, 0, 24, 24], [16*24, 0, 24, 24]], (0, 0, 0))

player_frame = 0
player_frame_delay = 20

player_rect = player_images[0].get_rect()
player_rect.center = WIN_rect.center

grounds = [pygame.image.load("art\ground.png")] * 4
ground_rects = [grounds[0].get_rect(), grounds[0].get_rect(), grounds[0].get_rect(), grounds[0].get_rect()]

clock = pygame.time.Clock()

gravity = 0

for i in range(len(ground_rects)):
    ground_rects[i].x = 336 * i
    ground_rects[i].y = 500

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and speed == 0:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                obstacle_rect.x = 1000
                speed = 4 
                score = 0
                button_rect.y = 10000
                
        keys = pygame.key.get_pressed()
        
        for ground_rect in ground_rects:
            if keys[pygame.K_SPACE] and player_rect.colliderect(ground_rect) and speed > 0:
                gravity = -15
                player_rect.y -= 8
            if keys[pygame.K_SPACE] and speed == 0:
                obstacle_rect.x = 1000
                speed = 4 
                score = 0
                button_rect.y = 10000
    
    #gravity
    gravity += .5
    for ground_rect in ground_rects:
        if player_rect.colliderect(ground_rect):
            gravity = 0
            
        ground_rect.x -= int(speed)
        if ground_rect.right <= 0 -20:
            #the furthest right ground
            rightest = 0
            
            for ground_rect2 in ground_rects:
                #checks all the grounds to see if there is anything righter
                if ground_rect2.right > rightest:
                    rightest = ground_rect2.right -10
            #makes ground that needs to move go to right spot    
            ground_rect.left = rightest
    
    obstacle_rect.x -= int(speed)
    if obstacle_rect.x <= -100:
        
        score += 1
        speed = math.sqrt(score) + 4
        
        obstacle_rect.x = 620 + random.randint(0, 100)
        
    if player_rect.colliderect(obstacle_rect):
        speed = 0
        button_rect.center = WIN_rect.center
    
    player_rect.y += gravity
      
    #draws objects      
    WIN.fill("light blue")
    for i, ground in  enumerate(grounds):
        WIN.blit(ground, ground_rects[i])
    
    if player_frame_delay <= 0:
        player_frame += 1
        if speed == 0:
          if player_frame >= len(player_images):
              player_frame = len(player_images) -1
           
        elif player_frame >= len(player_images) - 4:
            player_frame = 0
        player_frame_delay = 20
    else:
        player_frame_delay -= 3
          
    WIN.blit(obstacle_image, obstacle_rect)
        
    WIN.blit(player_images[player_frame], player_rect)
    
    score_img = get_text.prep_message("Score: " + str(score))
    WIN.blit(score_img, (WIN_rect.w - 10 - score_img.get_width(), 30))
    
    WIN.blit(button_bg_image, (button_rect.left - button_rect.w/2, button_rect.top - button_rect.h/2))
    WIN.blit(button_image, button_rect)
               
    pygame.display.update()
    
    clock.tick(60)
    
    
    