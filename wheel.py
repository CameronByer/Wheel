import random
import pygame

BLACK = (0, 0, 0)

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wheel")

def drawtab(self, x, y, sizex, sizey, text, fontsize):
    pass

possibilities = ["Cameron", "Rob", "Steve", "Matt", "Lorena", "Daniel"]

running = True
while running:
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
    pygame.display.flip()       

pygame.quit()
    
