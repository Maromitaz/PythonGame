import pygame, os, time
from colorama import Fore as fc
from pygame.mouse import get_pos
from pypresence import Presence
global animation_frames
animation_frames = {}
global grass
grass = []
# Loads the images given
def Image_load(image_location, size):
    image_list = []
    for image in os.listdir(image_location):
        image_path = f"{image_location}/{image}"
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
# Just as the name implies, it adds rich presence to your game on discord, for more information check https://qwertyquerty.github.io/pypresence/html/index.html
class discord_rich_presence:
    def __init__(self, client_id):
        self.client_id = client_id
    def RPC(self):
        RPC = Presence(client_id=self.client_id)
        return RPC
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
# Movement and things for the player
class Move:
    def __init__(self, color_key):
        self.color_key = color_key
    def player_anim(self,path, frame_duration):
        animation_name = path.split('/')[-1]
        animation_frame_data = []
        n = 0
        for frame in frame_duration:
            global animation_frames
            animation_frame_id = animation_name+'_'+str(n)
            img_location = path+'/'+animation_frame_id+'.png'
            animation_image = pygame.image.load(img_location).convert()
            animation_image.set_colorkey(self.color_key)
            animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n+=1
        return animation_frame_data
    def animation_change(self, action_var,frame,new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var, frame

    def player_motion(self, movement, rect, tiles):
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
        self.tile_rects = []
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
    def map_loader(self, surface, scroll):
        self.tile_rects = []
        y = 0
        # Loops through the map file and assigns each letter/number to a tile
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    surface.blit(self.tiles[0], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '2':
                    surface.blit(self.tiles[1], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                    global grass
                    grass.append((x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '3':
                    surface.blit(self.tiles[2], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '4':
                    surface.blit(self.tiles[3], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '5':
                    surface.blit(self.tiles[4], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '6':
                    surface.blit(self.tiles[5], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '7':
                    surface.blit(self.tiles[6], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '8':
                    surface.blit(self.tiles[7], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == '9':
                    surface.blit(self.tiles[8], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == 'a':
                    surface.blit(self.tiles[9], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == 'b':
                    surface.blit(self.tiles[10], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == 'c':
                    surface.blit(self.tiles[11], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile == 'd':
                    surface.blit(self.tiles[12], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                # if tile == 'f':
                #     surface.blit(self.tiles[13], (x* self.size-scroll[0] , y* self.size-scroll[1]))
                if tile != '0':
                    self.tile_rects.append(pygame.Rect(x * self.size, y * self.size, self.size, self.size))
                x += 1
            y += 1
        
