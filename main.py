import framework, pygame
color = framework.Color.color
pygame.init()
clock = pygame.time.Clock()
# Window things
display_manager = framework.Display("Super Ultra Cool Game",1200, 800, 2)
display = display_manager.set_display()
surface = display_manager.surface()
running = True
# Player's movement
moving_left = False
moving_right = False
player_y_momentum = 0
player_y_momentum_max = 5
air_timer = 0
# loading images
tile_size = 24
tile_images = framework.Image_load("images/map",["Tile_01","Tile_02","Tile_03","Tile_04","Tile_05","Tile_06","Tile_07","Tile_08","Tile_09","Tile_10","Tile_11","Tile_12","Tile_13"], tile_size)
player = pygame.image.load('images/player/Sprite.png').convert()
player.set_colorkey((255,0,0))
player_rect = player.get_rect()
player_rect.bottom = (display_manager.width//display_manager.zoom)//4
player_rect.left = (display_manager.width//display_manager.zoom)//2
# Loading map
map = framework.Map(tile_images, "map", tile_size)
# colors
DarkSlateGray = framework.Color.custom_color((47,79,79))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_a:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_a:
                moving_left = False
    player_movement = [0,0]
    if moving_right:
        player_movement[0] +=2
    if moving_left:
        player_movement[0] -=2
    player_movement[1] += player_y_momentum
    player_y_momentum +=0.2
    if player_y_momentum >= player_y_momentum_max:
        player_y_momentum = player_y_momentum_max

    draw = framework.Draw
    draw.rect(draw, surface, DarkSlateGray, (0,0,display_manager.width, display_manager.height))
    map.map_loader(surface)
    player_rect, collisions = framework.Move(player_rect,player_movement, map.tile_rects).player_motion()
    surface.blit(player,player_rect)

    surf = pygame.transform.scale(surface,(display_manager.width, display_manager.height))
    display.blit(surf,(0,0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()