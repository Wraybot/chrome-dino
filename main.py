import pygame
import sys
from spritesheet import spritesheet

pygame.init()

WIN = pygame.display.set_mode((600, 600))
WIN_rect = WIN.get_rect()

player_ss = spritesheet("art\dino.png")
player_images = player_ss.images_at([[4*24, 0, 24, 24], [5*24, 0, 24, 24], [6*24, 0, 24, 24], [7*24, 0, 24, 24], 
                                     [8*24, 0, 24, 24], [9*24, 0, 24, 24]], (0, 0, 0))
#furcorn colorkey = (186.5, 31.3, 63.7)
obstacle_image = pygame.image.load("art\_furcorn.png")
colorkey = obstacle_image.get_at((0,0))
obstacle_image.set_colorkey(colorkey, pygame.RLEACCEL)
obstacle_rect = obstacle_image.get_rect()
obstacle_rect.x = 50
obstacle_rect.y = 50

#fix redundency later
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
        keys = pygame.key.get_pressed()
        
        for ground_rect in ground_rects:
            if keys[pygame.K_SPACE] and player_rect.colliderect(ground_rect):
                gravity = -15
                player_rect.y -= 8
    
    #gravity
    gravity += .5
    for ground_rect in ground_rects:
        if player_rect.colliderect(ground_rect):
            gravity = 0
            
        ground_rect.x -= 2
        if ground_rect.x <= -336:
            ground_rect.x = 336 * 3
    
    player_rect.y += gravity
      
    #draws objects      
    WIN.fill("light blue")
    for i, ground in  enumerate(grounds):
        WIN.blit(ground, ground_rects[i])
    
    if player_frame_delay <= 0:
        player_frame += 1
        if player_frame >= len(player_images):
            player_frame = 0
        player_frame_delay = 20
    else:
        player_frame_delay -= 3
          
    WIN.blit(obstacle_image, obstacle_rect)
        
    WIN.blit(player_images[player_frame], player_rect)
               
    pygame.display.update()
    
    clock.tick(60)
    
    
    