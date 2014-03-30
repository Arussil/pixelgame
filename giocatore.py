import pygame

WHITE = (255,255,255)

class Giocatore(pygame.sprite.Sprite):
    
    change_x = 0
    change_y = 0
    walls = None
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([5,5])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def moveright(self):
        self.rect.x -= 10
    def moveleft(self):
        self.rect.x += 10
    def moveup(self):
        self.rect.y -= 10
    def movedown(self):
        self.rect.y += 10

    def update(self):

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Proiettile(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([5,5])

        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += 10
