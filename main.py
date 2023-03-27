import pygame
import sys

pygame.init()

WIN = pygame.display.set_mode((600, 600))
WIN_rect = WIN.get_rect()

player = pygame.Surface((20, 20))
player.fill("black")
player_rect = player.get_rect()
player_rect.center = WIN_rect.center

grounds = [pygame.image.load("art\ground.png")] * 4
ground_rects = grounds[0].get_rect()
for ground_rect in  ground_rects:
    ground_rect.y = 500

clock = pygame.time.Clock()

gravity = 0

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
        
        if keys[pygame.K_SPACE] and player_rect.colliderect(ground_rect):
            gravity = -15
            player_rect.y -= 8
            
    gravity += .5
    
    if player_rect.colliderect(ground_rect):
        gravity = 0
    
    player_rect.y += gravity
            
    WIN.fill("light blue")
    WIN.blit(ground, ground_rect)
    WIN.blit(player, player_rect)
               
    pygame.display.update()
    
    clock.tick(60)