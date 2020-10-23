# Simple game with pygame


import pygame as pg

red = (255, 0, 0)
green = (0, 250, 0)

pg.init()
screen = pg.display.set_mode((500,500))
clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        if keystate[pg.K_UP]:
            self.speedx = -5
        if keystate[pg.K_DOWN]:
            self.speedx = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()
    screen.fill(red)
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()

