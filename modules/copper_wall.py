import pygame
import os

class Copper_Wall:
    def __init__(self, width, height, x, y, image):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image
        self.speed = 2
        self.load_image()

    def load_image(self):
        absolute_path = os.path.abspath(__file__ + "/../..")
        absolute_path = os.path.join(absolute_path, self.image)
        image = pygame.image.load(absolute_path)
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = scaled_image

    def draw_image(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))