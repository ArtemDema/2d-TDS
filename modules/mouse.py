import pygame

pygame.init()

class Mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_collide(self, wall, c_wall):
        left_x_w = wall.x
        right_x_w = wall.x + wall.width
        top_y_w = wall.y
        bottom_y_w = wall.y + wall.height

        if self.x >= left_x_w:
            if self.x <= right_x_w:
                if self.y >= top_y_w:
                    if self.y <= bottom_y_w:
                        c_wall.x = wall.x
                        c_wall.y = wall.y

    def check_collide_for_delete(self, wall):
        left_x_w = wall.x
        right_x_w = wall.x + wall.width
        top_y_w = wall.y
        bottom_y_w = wall.y + wall.height

        if self.x > left_x_w:
            if self.x < right_x_w:
                if self.y > top_y_w:
                    if self.y < bottom_y_w:
                        wall.x = 3000
                        wall.y = 3000