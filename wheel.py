import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 255, 0)

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wheel")

pygame.font.init()
FONTSIZE = 40
font = pygame.font.SysFont("Calibri", FONTSIZE)

FPS = 60
clock = pygame.time.Clock()

class Tab:

    def __init__(self, text, color, x, y, sizex, sizey):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.selected = False

    def calcxoffset(self, radius, centery):
        dist = centery - (self.y + self.sizey/2)
        return radius-(radius**2 - dist**2)**0.5

    def draw(self, screen):
        text = font.render(self.text, False, BLACK)
        textsize = text.get_size()
        offset = self.calcxoffset(2000, 300)
        if self.selected:
            pygame.draw.rect(screen, BLACK, (self.x+offset, self.y, self.sizex, self.sizey))
            pygame.draw.rect(screen, self.color, (self.x+5+offset, self.y+5, self.sizex-10, self.sizey-10))
        else:
            pygame.draw.rect(screen, self.color, (self.x+offset, self.y, self.sizex, self.sizey))
        screen.blit(text, (self.x+(self.sizex-textsize[0])/2+offset, self.y+(self.sizey-textsize[1])/2))

    def update(self, dist):
        self.y += dist
        if self.y >= 200 and self.y < 300:
            self.selected = True
        else:
            self.selected = False

possibilities = ["900",	"940", "993", "1080", "1109", "1114"]

tabs = [Tab(random.choice(possibilities), RED, 300, 500, 200, 100)]
for i in range(6):
    nextname = tabs[-1].text
    while nextname == tabs[-1].text:
        nextname = random.choice(possibilities)
    tabs.append(Tab(nextname, [RED, WHITE][tabs[-1].color==RED], 300, tabs[-1].y-100, 200, 100))

speed = random.randint(200, 250)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #Left Click
                pass
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #Left Click
                pass
    screen.fill(BLACK)
    for tab in tabs:
        tab.update(min(speed, 10))
    tabs = [tab for tab in tabs if tab.y <= HEIGHT]
    if tabs[-1].y >= 0:
        nextname = tabs[-1].text
        while nextname == tabs[-1].text:
            nextname = random.choice(possibilities)
        tabs.append(Tab(nextname, [RED, WHITE][tabs[-1].color==RED], 300, tabs[-1].y-100, 200, 100))
    for tab in tabs:
        tab.draw(screen)
    pygame.draw.polygon(screen, GREEN, ((295, 300), (200, 220), (200, 380)))
    if speed == 0:
        pygame.draw.polygon(screen, GREEN, ((505, 300), (600, 220), (600, 380)))
    speed *= 0.994
    if speed < 0.1:
        speed = 0
    pygame.display.flip()       

pygame.quit()
    
