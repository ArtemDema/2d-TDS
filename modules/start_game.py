import pygame

from modules.screen import screen
from modules.player import player
from modules.wall import blocks, blocks_without_collide, Wall, walls
from modules.mini_map import mini_map, mini_player, rect
from modules.copper_wall import Copper_Wall
from modules.mouse import Mouse

pygame.init()

def game():
    game_run = True
    can_put_block = False
    while game_run:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            #выход
            if event.type == pygame.QUIT:
                game_run = False

            #запоминание позиции мыши
            if event.type == pygame.MOUSEMOTION:
                position_mouse = event.pos

            #если нажал ЛКМ, и можно ставить блок - то оно шерстит весь массив.
            #Если нашло по позиции - рисует стену поверх пола
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if can_put_block:
                    position_block = [c_wall.x, c_wall.y]
                    for wall in blocks_without_collide:
                        if position_block[0] == wall.x:
                            if position_block[1] == wall.y:
                                can_put_block = False
                                wall = Wall(width = 40, height = 40, x = c_wall.x, y = c_wall.y, image = "images/copper_wall.png")
                                walls.append(wall)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for wall in walls:
                    mouse.check_collide_for_delete(wall)

        #отрисовка карты и игрока
        #---------------------------------
        screen.fill((0, 0, 0))
        for wall in blocks:
            wall.draw_image(screen)

        for wall in blocks_without_collide:
            wall.draw_image(screen)

        for wall in walls:
            wall.draw_image(screen)

        player.draw_image(screen)
        #---------------------------------

        #для норм поставки блока(по коллизии)
        #---------------------------------
        if can_put_block:
            mouse = Mouse(position_mouse[0], position_mouse[1])
            for wall in blocks_without_collide:
                mouse.check_collide(wall, c_wall)
        #---------------------------------

        #проверка на то, что я могу, или не могу ставить
        #---------------------------------
        if keys[pygame.K_1]:
            can_put_block = True
            c_wall = Copper_Wall(40, 40, wall.x, wall.y, "images/copper_wall.png")
        
        if can_put_block:
            c_wall.draw_image(screen)
        #---------------------------------

        #отрисовка мини карты
        #---------------------------------
        pygame.draw.rect(screen, (0, 31, 77), rect)
        mini_map.draw_image(screen)
        mini_player.draw_image(screen)
        #---------------------------------

        #передвижение:
        #вверх
        if keys[pygame.K_w]:
            player.can_go_top = True
            for wall in blocks:
                player.check_collide_top(wall)
            
            for wall in walls:
                player.check_collide_top(wall)
            
            if player.can_go_top:
                mini_player.y -= 0.2
                for wall in blocks:
                    wall.y +=  wall.speed

                for wall in blocks_without_collide:
                    wall.y +=  wall.speed

                for wall in walls:
                    wall.y +=  wall.speed

        #вниз
        if keys[pygame.K_s]:
            player.can_go_bottom = True
            for wall in blocks:
                player.check_collide_bottom(wall)

            for wall in walls:
                player.check_collide_bottom(wall)
            
            if player.can_go_bottom:
                mini_player.y += 0.2
                for wall in blocks:
                    wall.y -=  wall.speed

                for wall in blocks_without_collide:
                    wall.y -=  wall.speed
                
                for wall in walls:
                    wall.y -=  wall.speed
        
        #влево
        if keys[pygame.K_a]:
            player.can_go_left = True
            for wall in blocks:
                player.check_collide_left(wall)

            for wall in walls:
                player.check_collide_left(wall)
            
            if player.can_go_left:
                mini_player.x -= 0.2
                for wall in blocks:
                    wall.x +=  wall.speed

                for wall in blocks_without_collide:
                    wall.x +=  wall.speed

                for wall in walls:
                    wall.x +=  wall.speed

        #вправо
        if keys[pygame.K_d]:
            player.can_go_right = True
            for wall in blocks:
                player.check_collide_right(wall)
            
            for wall in walls:
                player.check_collide_right(wall)
            
            if player.can_go_right:
                mini_player.x += 0.2
                for wall in blocks:
                    wall.x -=  wall.speed

                for wall in blocks_without_collide:
                    wall.x -=  wall.speed

                for wall in walls:
                    wall.x -=  wall.speed

        pygame.display.flip()