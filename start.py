import pygame
from pygame.locals import *
from giocatore import Giocatore, Proiettile
from muro import Muro

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
done = False

all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()

wall = Muro(0,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Muro(590,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Muro(10,0,600,10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Muro(10,590,600,10)
wall_list.add(wall)
all_sprite_list.add(wall)

player = Giocatore(50,50)
player.walls = wall_list

all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveright()
            elif event.key == pygame.K_RIGHT:
                player.moveleft()
            elif event.key == pygame.K_UP:
                player.moveup()
            elif event.key == pygame.K_DOWN:
                player.movedown()
            elif event.key == pygame.K_SPACE:
                bullet = Proiettile()
                all_sprite_list.add(bullet)
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y

    screen.fill(BLACK)
    all_sprite_list.update()
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
