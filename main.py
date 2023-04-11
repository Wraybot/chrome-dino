import pygame
import sys
from spritesheet import spritesheet

pygame.init()

WIN = pygame.display.set_mode((600, 600))
WIN_rect = WIN.get_rect()

player_ss = spritesheet("art\dino.png")
player_image = player_ss.image_at([0, 0, 24, 24])
player_image = player_ss.enlarge_image(player_image, (0, 0, 0))

player_rect = player_image.get_rect()
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
    WIN.blit(player_image, player_rect)
               
    pygame.display.update()
    
    clock.tick(60)