import pygame
import math

# Setting of game
WIDTH = 1280
HEIGHT = 720
FPS = 60

def positionx(xlt):
    xt = xlt - (p.pos[0] - WIDTH // 2)
    return xt
def positiony(ylt):
    yt = ylt - (p.pos[1] - HEIGHT // 2)
    return yt
class Player():
    def __init__(self):
        self.pos = [0, 0]
        self.speed = 5
        self.velocity_x = 0
        self.velocity_y = 0
        self.image = pygame.image.load("player.png")
    def input(self):
        self.velocity_x = 0
        self.velocity_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.velocity_y = self.speed * -1
        if keys[pygame.K_s]:
            self.velocity_y = -self.speed * -1
        if keys[pygame.K_d]:
            self.velocity_x = -self.speed * -1
        if keys[pygame.K_a]:
            self.velocity_x = self.speed * -1
        if keys[pygame.K_LSHIFT]:
            self.speed = 10
        if not keys[pygame.K_LSHIFT]:
            self.speed = 5

        if self.velocity_x != 0 and self.velocity_y != 0:  # moving diagonally
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)
    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
    def interface(self):
        f = pygame.font.SysFont('Verdana', 20)
        n1 = f.render(f'X: {round(self.pos[0])} Y: {round(self.pos[1])}', True, (255, 255, 255))
        screen.blit(n1, (5, 5))
    def update(self):
        self.input()
        self.move()
        self.interface()
        screen.blit(self.image, (WIDTH//2-self.image.get_width()//2, HEIGHT//2-self.image.get_height()//2))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("It is my game")
clock = pygame.time.Clock()

size_image = 100
background0 = pygame.transform.scale(pygame.image.load("water.jpg").convert(), (size_image, size_image))
background1 = pygame.transform.scale(pygame.image.load("grass.jpg").convert(), (size_image, size_image))
background2 = pygame.transform.scale(pygame.image.load("sand.jpg").convert(), (size_image, size_image))
background3 = pygame.transform.scale(pygame.image.load("earth.jpg").convert(), (size_image, size_image))
background4 = pygame.transform.scale(pygame.image.load("stone.jpg").convert(), (size_image, size_image))
background5 = pygame.transform.scale(pygame.image.load("diamond.jpg").convert(), (size_image, size_image))
textures = [background0, background1, background2, background3, background4, background5]
p = Player()
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 3, 4, 0, 3, 0, 0, 0],
    [0, 0, 2, 3, 5, 2, 2, 3, 0, 0],
    [1, 2, 2, 1, 4, 2, 1, 3, 0, 0],
    [0, 0, 2, 2, 2, 2, 2, 2, 0, 0],
    [0, 0, 1, 0, 0, 0, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# основоно цикл игры
while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for i in range(len(map)):
        for j in range(len(map[0])):
            screen.blit(textures[map[i][j]], (positionx(i*size_image), positiony(j*size_image)))
    p.update()
    pygame.display.flip()
