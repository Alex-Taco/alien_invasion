import pygame

my_image = pygame.image.load('images/ship.bmp')
my_rect = my_image.get_rect()

a = 1.58
my_rect.x = a

print (my_rect.x)