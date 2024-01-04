import pygame
import math

# Setting of game
WIDTH = 1280
HEIGHT = 720
FPS = 60
SIZE_WORLD = 1

# 2 functions for relative rendering of objects
def positionx(xlt):
    xt = xlt - (p.pos[0] - WIDTH // 2)
    return xt
def positiony(ylt):
    yt = ylt - (p.pos[1] - HEIGHT // 2)
    return yt

# creating the Player class
class Player():
    def __init__(self):
        self.name = "None"
        self.pos = [0, 0]
        self.speed = 5
        self.velocity_x = 0
        self.velocity_y = 0

        self.cell = []
        self.size_cell = 50

        self.image = pygame.image.load("player.png")

        # cell
        self.h = pygame.transform.scale(pygame.image.load("h.png").convert(), (self.size_cell, self.size_cell))
        self.h = pygame.image.load("h.png").convert_alpha()
        self.h.set_alpha(200)

        # character picture
        self.i = pygame.image.load("i.png").convert_alpha()
        self.i = pygame.transform.scale(pygame.image.load("i.png").convert(), (50, 50))
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
        name = f.render(self.name, True, (255, 255, 255))
        n1 = f.render(f'X: {round(self.pos[0])} Y: {round(self.pos[1])}', True, (255, 255, 255))
        n2 = f.render(f'Velocity: {pygame.math.Vector2(self.velocity_x, self.velocity_y)}', True, (255, 255, 255))
        screen.blit(name, (5, 5))
        screen.blit(n1, (205, 5))
        screen.blit(n2, (205, 30))
        size_b = 100
        # pygame.draw.rect(screen, (127, 127, 127), [WIDTH//2-size_b//2, HEIGHT-size_b*2, size_b, size_b])
        screen.blit(self.h, (WIDTH//2-size_b//2, HEIGHT-size_b))
        screen.blit(self.i, (5, 5))
    def update(self):
        self.input()
        self.move()
        self.interface()
        screen.blit(self.image, (WIDTH//2-self.image.get_width()//2, HEIGHT//2-self.image.get_height()//2))

pygame.init()
# setting up the game window
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
background6 = pygame.transform.scale(pygame.image.load("water2.jpg").convert(), (size_image, size_image))
textures = [background0, background1, background2, background3, background4, background5, background6]

# Tree
class Tree:
    def __init__(self):
        self.sizex_tree = 200
        self.sizey_tree = 200
        self.tree1 = pygame.transform.scale(((pygame.image.load("tree1.png")).convert()), (150, 250))
        # self.tree1 = (pygame.image.load("tree1.png")).convert_alpha()
        self.tree2 = pygame.transform.scale(pygame.image.load("tree2.png").convert(), (self.sizex_tree, self.sizey_tree))


        self.h = pygame.transform.scale(pygame.image.load("tree1.png").convert(), (150, 250))
        self.h = self.h.convert_alpha()
    def draw(self):
        screen.blit(self.h, (positionx(60), positiony(100)))
    def update(self):
        self.draw()

p = Player()
t = Tree()

# creating a map
ma = []
f = open("map.txt")
l = len(f.readlines())
f.seek(0)
for i in range(l):
    ma.append(list(str(f.readline()).replace("\n", "")))

# changing strings to numbers
for i in range(len(ma)):
    for j in range(len(ma[i])):
        ma[i][j] = int(ma[i][j])

# The main cycle of the game
while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # drawing the map
    for i in range(len(ma)):
        for j in range(len(ma[0])):
            screen.blit(textures[ma[i][j]], (positionx(i*size_image), positiony(j*size_image)))

    p.update()
    pygame.display.flip()
