import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
size = (700, 500)
background_colour = (0, 0,255)
(width, height) = (750, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Typing Test')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False