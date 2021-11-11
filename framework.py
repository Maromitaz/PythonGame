import pygame
from colorama import Fore as fc
# Loads the images given
def Image_load(image_location, images, size):
    image_list = []
    for image in images:
        image_path = f"{image_location}/{image}.png"
        print(fc.LIGHTBLUE_EX+f"Loading: {image_path}")
        sprite = pygame.image.load(image_path)
        sprite = pygame.transform.scale(sprite,(size,size))
        image_list.append(sprite)
    print(fc.GREEN+"Load complete"+fc.WHITE)
    return image_list
# Sets the game's window & resolution & zoom to the player
class Display:
    def __init__(self, name, width, height, zoom):
        self.width = width
        self.height = height
        self.zoom = zoom
        pygame.display.set_caption(f"{name}")
    # Settles the game's zoom
    def surface(self):
        width2 = self.width//self.zoom
        width2 = int(width2)
        height2 = self.height//self.zoom
        height2 = int(height2)
        size = (width2, height2)
        return pygame.Surface(size)
    # Does what it's told to do
    def set_display(self):
        return pygame.display.set_mode((self.width, self.height),0,32)
# Just drawing, that was the first thing that i've done on this framework
class Draw:         #       Start          End
    def __init__(self,start_x,start_y, end_x,end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
    def get_rect(self):
        rect_return = (self.start_x, self.start_y, self.end_x, self.end_y)
        return rect_return
    def rect(self, surface, color, rect_return):
        pygame.draw.rect(surface, color, rect_return)
    # def circle(self, surface, color, center, radius):
    #     pygame.draw.rect(surface, color, center, radius)
    # def line (self, surface, color, ):
    #     pass
# Predefined colors, you can define yourself some more in your game's folder by calling the "custom_color" function, working on
# to make it return a list, so you can add more to one var
class Color:
    def custom_color(color_rgb):
        custom_color = color_rgb
        return custom_color
    color = {
        'RED'       : (255,0,0),
        'GREEN'     : (0,255,0),
        'BLUE'      : (0,0,255),
        'WHITE'     : (255,255,255),
        'BLACK'     : (0,0,0),
        'ORANGE'    : (255,125,0),
        'MAGENDA'   : (255,0,255)
    }
# TODO: player loader, player collision player movement
class Move:
    def __init__(self,rect, movement, tiles):
        self.rect = rect
        self.movement = movement
        self.tiles = tiles

    def player_motion(self):
        rect = self.rect
        movement = self.movement
        tiles = self.tiles
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = Move.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = Move.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def collision_test(rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list
# The map loader for the game
class Map:
    def __init__(self, tiles, path, size):
        self.size = size
        self.tiles = tiles
        # Searches + opens the map folder
        f = open(path+'.txt', 'r')
        data = f.read()
        f.close()
        data = data.split("\n")
        game_map = []
        # Searches every row of the text file that contains numbers/letters
        for row in data:
            game_map.append(list(row))
        self.game_map = game_map
    # Loads the map
    def map_loader(self, surface):
        tile_rects = []
        y = 0
        # Loops through the map file and assigns each letter/number to a tile
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    surface.blit(self.tiles[0], (x* self.size , y* self.size))
                if tile == '2':
                    surface.blit(self.tiles[1], (x* self.size , y* self.size))
                if tile == '3':
                    surface.blit(self.tiles[2], (x* self.size , y* self.size))
                if tile == '4':
                    surface.blit(self.tiles[3], (x* self.size , y* self.size))
                if tile == '5':
                    surface.blit(self.tiles[4], (x* self.size , y* self.size))
                if tile == '6':
                    surface.blit(self.tiles[5], (x* self.size , y* self.size))
                if tile == '7':
                    surface.blit(self.tiles[6], (x* self.size , y* self.size))
                if tile == '8':
                    surface.blit(self.tiles[7], (x* self.size , y* self.size))
                if tile == '9':
                    surface.blit(self.tiles[8], (x* self.size , y* self.size))
                if tile == 'a':
                    surface.blit(self.tiles[9], (x* self.size , y* self.size))
                if tile == 'b':
                    surface.blit(self.tiles[10], (x* self.size , y* self.size))
                if tile == 'c':
                    surface.blit(self.tiles[11], (x* self.size , y* self.size))
                if tile == 'd':
                    surface.blit(self.tiles[12], (x* self.size , y* self.size))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * self.size, y * self.size, self.size, self.size))
                x += 1
            y += 1
        self.tile_rects = tile_rects
