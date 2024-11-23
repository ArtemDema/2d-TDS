import pygame
import os

from modules.screen import WIDTH, HEIGHT
from modules.wall import Wall

pygame.init()

class Player:
    def __init__(self, width, height, x, y, image):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image
        self.can_go_bottom = True
        self.can_go_left = True
        self.can_go_right = True
        self.can_go_top = True
        self.load_image()

    def load_image(self):
        absolute_path = os.path.abspath(__file__ +"/../..")
        absolute_path = os.path.join(absolute_path,self.image)   
        image = pygame.image.load(absolute_path)
        scaled_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = scaled_image

    def draw_image(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def check_collide_left(self, wall:Wall):
        bottom_y_p = self.y + self.height
        top_y_p = self.y
        left_x_p = self.x

        left_x_w = wall.x
        right_x_w = wall.x + wall.width
        top_y_w = wall.y
        bottom_y_w = wall.y + wall.height

        #нижний угол
        if top_y_p >= top_y_w:
            if left_x_p <= right_x_w + 2:
                if top_y_p <= bottom_y_w:
                    if left_x_p >= left_x_w:
                        self.can_go_left = False

        #верхний угол
        if top_y_p <= top_y_w:
            if left_x_p <= right_x_w + 2:
                if top_y_w <= bottom_y_p:
                    if left_x_p >= left_x_w:
                        self.can_go_left = False
        #-----------------------------------------------------------

    def check_collide_top(self, wall:Wall):
        bottom_y_p = self.y + self.height
        top_y_p = self.y
        left_x_p = self.x
        right_x_p = self.x + self.width

        left_x_w = wall.x
        right_x_w = wall.x + wall.width
        top_y_w = wall.y
        bottom_y_w = wall.y + wall.height

        #левый угол
        if left_x_p <= left_x_w:
            if bottom_y_p >= bottom_y_w:
                if right_x_p >= left_x_w:
                    if top_y_p <= bottom_y_w + 2:
                        self.can_go_top = False
        #правый угол
        if left_x_p <= right_x_w:
            if bottom_y_p >= top_y_w:
                if right_x_p >= right_x_w:
                    if top_y_p <= bottom_y_w + 2:
                        self.can_go_top = False
    #-----------------------------------------------------------
                
    def check_collide_right(self, wall:Wall):
        bottom_y_p = self.y + self.height
        top_y_p = self.y
        left_x_p = self.x
        right_x_p = self.x + self.width
            
        left_x_w = wall.x
        right_x_w = wall.x + wall.width
        top_y_w = wall.y
        bottom_y_w = wall.y + wall.height

        #нижний угол
        if right_x_p >= left_x_w - 2:
            if bottom_y_p >= bottom_y_w:
                if left_x_p <= right_x_w:
                    if top_y_p <= bottom_y_w:
                        self.can_go_right = False

        #верхний угол
        if top_y_p <= top_y_w:
            if right_x_p >= left_x_w - 2:
                if left_x_p <= right_x_w:
                    if bottom_y_p >= top_y_w:
                        self.can_go_right = False
        #-----------------------------------------------------------
    
    def check_collide_bottom(self, wall:Wall):
        bottom_y_p = self.y + self.height
        top_y_p = self.y
        left_x_p = self.x
        right_x_p = self.x + self.width

        left_x_w = wall.x
        right_x_w = wall.x + wall.width
        top_y_w = wall.y
        bottom_y_w = wall.y + wall.height

        #левый угол
        if left_x_p <= left_x_w:
            if right_x_p >= left_x_w:
                if bottom_y_p >= top_y_w - 2:
                    if bottom_y_p <= bottom_y_w:
                        self.can_go_bottom = False
        
        #правый угол
        if left_x_p <= right_x_w:
            if right_x_p >= right_x_w:
                if bottom_y_p >= top_y_w - 2:
                    if bottom_y_p <= bottom_y_w:
                        self.can_go_bottom = False


        


player = Player(width = 40, height = 40, x = WIDTH / 2 - 20, y = HEIGHT / 2 - 20, image = "images/water.png")