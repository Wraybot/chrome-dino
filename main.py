import pygame
import sys

pygame.init()

WIN = pygame.display.set_mode((600, 600))
WIN_rect = WIN.get_rect()

player = pygame.Surface((20, 20))
player.fill("black")
player_rect = player.get_rect()
player_rect.center = WIN_rect.center

ground = pygame.image.load("art\ground.png")
ground_rect = ground.get_rect()
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
        
        if keys[pygame.K_SPACE]:
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