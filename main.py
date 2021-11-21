import framework, pygame
color = framework.Color.color
pygame.init()
clock = pygame.time.Clock()
    # Window things and for the player's camera
display_manager = framework.Display("Super Ultra Cool Game",1200, 800, 2)
display = display_manager.set_display()
surface = display_manager.surface()
running = True
true_scroll = [0,0]
    # Player's movement
moving_left = False
moving_right = False
player_y_momentum = 0
player_y_momentum_max = 5
air_timer = 0
    # loading images
tile_size = 24
tile_images = framework.Image_load("images/map", tile_size)
    # Loading map
map = framework.Map(tile_images, "map", tile_size)
    # Player's animation controll
player_movement = [0,0]
player_rect = pygame.Rect(300,10,5,12)
player_controller=framework.Move((255,0,0))
animation_frames = framework.animation_frames
animation_database = {}
animation_database['idle'] = player_controller.player_anim('images/player/idle',(13,100))
animation_database['run'] = player_controller.player_anim('images/player/run',(7,7))
player_action = 'idle'
player_frame = 0
player_flip = False
    # colors
DarkSlateGray = framework.Color.custom_color((47,79,79))
    # Discord things
RPC = framework.discord_rich_presence(909845043798499379).RPC()
try:
    RPC.connect()
except:
    print("Could not connect to Discord")
else:
    print("Successfully connected to Discord")
var = 0
world = "Null"
while running:
        # Discord rich presence
    if var == 0:
        world = "Dev"
    elif var == 1:
        var = 0
    RPC.update(state = "Locating the funny" ,large_image = "9eq4jhgaspi71", details=f"World: {world}", small_image = "9eq4jhgaspi71", small_text="Testing my game")
    var += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_w:
                if air_timer < 6:
                    player_y_momentum -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_a:
                moving_left = False
    true_scroll[0] += (player_rect.x-true_scroll[0]-display_manager.width//4)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-display_manager.height//2//2+23)/10
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    draw = framework.Draw
    draw.rect(draw, surface, DarkSlateGray, (0, 0, display_manager.width, display_manager.height))
    map.map_loader(surface, scroll)
    player_rect, collisions = player_controller.player_motion(player_movement, player_rect, map.tile_rects) # player's collision detection
    player_movement = [0,0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum >= player_y_momentum_max:
        player_y_momentum = player_y_momentum_max
    if player_movement[0] > 0:
        player_action,player_frame = player_controller.animation_change(player_action,player_frame,'run')
        player_flip = False
    if player_movement[0] == 0:
        player_action,player_frame = player_controller.animation_change(player_action,player_frame,'idle')
    if player_movement[0] < 0:
        player_action,player_frame = player_controller.animation_change(player_action,player_frame,'run')
        player_flip = True
    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer +=1
    if collisions['top']:
        player_y_momentum = 0
    player_frame += 1
    if player_frame >= len(animation_database[player_action]):
        player_frame = 0
    player_img_id = animation_database[player_action][player_frame]
    player_image = animation_frames[player_img_id]
    surface.blit(pygame.transform.flip(player_image, player_flip, False), (player_rect.x-scroll[0], player_rect.y-scroll[1]))
    surf = pygame.transform.scale(surface, (display_manager.width, display_manager.height))
    display.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()