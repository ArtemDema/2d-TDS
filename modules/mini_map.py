import pygame
import os


class Mini_map:
    def __init__(self, width, height, x, y, image):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image
        self.load_image()

    def load_image(self):
        absolute_path = os.path.abspath(__file__ + "/../..")
        absolute_path = os.path.join(absolute_path, self.image)
        image = pygame.image.load(absolute_path)
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = scaled_image

    def draw_image(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

class Mini_player:
    def __init__(self, width, height, x, y, image):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image
        self.load_image()

    def load_image(self):
        absolute_path = os.path.abspath(__file__ + "/../..")
        absolute_path = os.path.join(absolute_path, self.image)
        image = pygame.image.load(absolute_path)
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = scaled_image

    def draw_image(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

rect = pygame.Rect(940, 10, 260, 260)

mini_map = Mini_map(width = 240, height = 240, x = 950, y = 20, image = "images/mini_map.png")

mini_player = Mini_map(width = 5, height = 5, x = 1005, y = 55, image = "images/Opengamer.png")