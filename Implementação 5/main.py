import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32

MAZE_WIDTH = SCREEN_WIDTH // TILE_SIZE 
MAZE_HEIGHT = SCREEN_HEIGHT // TILE_SIZE -1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Labyrinth of Zelda")

#assets
try:
    player_images = {
        'front': pygame.image.load('assets/images/player_front.png').convert_alpha(),
        'back': pygame.image.load('assets/images/player_back.png').convert_alpha(),
        'left': pygame.image.load('assets/images/player_left.png').convert_alpha(),
        'right': pygame.image.load('assets/images/player_right.png').convert_alpha()
    }
    wall_img = pygame.image.load('assets/images/wall.png').convert_alpha()
    floor_img = pygame.image.load('assets/images/floor.png').convert_alpha()
    collectible_img = pygame.image.load('assets/images/collectible.png').convert_alpha()
    portal_img = pygame.image.load('assets/images/portal.png').convert_alpha()

    pygame.mixer.music.load('assets/sounds/background_music.mp3')
    footstep_sfx = pygame.mixer.Sound('assets/sounds/footstep.wav')
    item_pickup_sfx = pygame.mixer.Sound('assets/sounds/item_pickup.wav')
    puzzle_solved_sfx = pygame.mixer.Sound('assets/sounds/puzzle_solved.wav')
    portal_entry_sfx = pygame.mixer.Sound('assets/sounds/portal_entry.wav')

    #ajuste de volume
    pygame.mixer.music.set_volume(0.3)
    footstep_sfx.set_volume(0.8)
    item_pickup_sfx.set_volume(0.7)
    puzzle_solved_sfx.set_volume(0.9)
    portal_entry_sfx.set_volume(0.7)

except pygame.error as e:
    print(f"Erro ao carregar asset: {e}")
    pygame.quit()
    sys.exit()

#sprites
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = player_images
        self.direction = 'front'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)
        self.collision_rect = pygame.Rect(0, 0, TILE_SIZE - 6, 16)
        self.collision_rect.midbottom = self.rect.midbottom

    def move(self, dx=0, dy=0):
        old_pos = self.rect.topleft
        self.rect.x += dx * TILE_SIZE
        self.rect.y += dy * TILE_SIZE
        self.collision_rect.midbottom = self.rect.midbottom

        if not puzzle_solved:
            collided = False
            for wall in wall_sprites:
                if self.collision_rect.colliderect(wall.rect):
                    collided = True
                    break
            if collided:
                self.rect.topleft = old_pos
                self.collision_rect.midbottom = self.rect.midbottom
                return
        
        footstep_sfx.play(maxtime=500)
        if dx > 0: self.direction = 'right'
        elif dx < 0: self.direction = 'left'
        elif dy > 0: self.direction = 'front'
        elif dy < 0: self.direction = 'back'
        self.image = self.images[self.direction]

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = wall_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = collectible_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = portal_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)


#gerador de labirinto aleatorio
def generate_maze(width, height):
    # Garante que as dimensões são ímpares
    maze_width = width if width % 2 != 0 else width - 1
    maze_height = height if height % 2 != 0 else height - 1
    maze = [['1' for _ in range(maze_width)] for _ in range(maze_height)]

    def carve_passages_from(cx, cy, grid):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 <= ny < maze_height and 0 <= nx < maze_width and grid[ny][nx] == '1':
                grid[ny - dy][nx - dx] = '0'
                grid[ny][nx] = '0'
                carve_passages_from(nx, ny, grid)

    start_x = random.randrange(1, maze_width, 2)
    start_y = random.randrange(1, maze_height, 2)
    maze[start_y][start_x] = '0'
    carve_passages_from(start_x, start_y, maze)
    return ["".join(row) for row in maze]

def place_objects_in_maze(maze, num_collectibles):
    floor_tiles = []
    for r, row in enumerate(maze):
        for c, tile in enumerate(row):
            if tile == '0':
                floor_tiles.append((r, c))

    if not floor_tiles: return maze
    
    player_pos = random.choice(floor_tiles)
    floor_tiles.remove(player_pos)
    
    collectible_pos = random.sample(floor_tiles, min(num_collectibles, len(floor_tiles)))

    list_maze = [list(row) for row in maze]
    list_maze[player_pos[0]][player_pos[1]] = 'P'
    for r, c in collectible_pos:
        list_maze[r][c] = 'C'
        
    return ["".join(row) for row in list_maze]

#agrupando sprites
all_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
collectible_sprites = pygame.sprite.Group()
portal_sprites = pygame.sprite.Group()

def setup_level():
    #Gera um novo labirinto e posiciona os objetos
    base_maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
    level_data = place_objects_in_maze(base_maze, 3)

    all_sprites.empty()
    wall_sprites.empty()
    collectible_sprites.empty()
    portal_sprites.empty()
    
    player_instance = None
    for row_index, row in enumerate(level_data):
        for col_index, tile in enumerate(row):
            if tile == '1':
                wall = Wall(col_index, row_index)
                all_sprites.add(wall)
                wall_sprites.add(wall)
            if tile == 'C':
                collectible = Collectible(col_index, row_index)
                all_sprites.add(collectible)
                collectible_sprites.add(collectible)
            if tile == 'P':
                player_instance = Player(col_index, row_index)
                all_sprites.add(player_instance)
    
    #Adiciona uma borda externa para garantir que o jogador não saia do mapa
    for i in range(MAZE_WIDTH):
        for j in [0, MAZE_HEIGHT-1]:
            w = Wall(i, j); all_sprites.add(w); wall_sprites.add(w)
    for i in range(MAZE_HEIGHT):
        for j in [0, MAZE_WIDTH-1]:
            w = Wall(j, i); all_sprites.add(w); wall_sprites.add(w)

    return player_instance, len(collectible_sprites), level_data

#execução do jogo:
player, total_collectibles, current_map_data = setup_level()
collectibles_collected = 0
puzzle_solved = False
running = True
clock = pygame.time.Clock()

RESUME_MUSIC_EVENT = pygame.USEREVENT + 1
pygame.mixer.music.play(-1)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: player.move(dx=-1)
            if event.key == pygame.K_RIGHT: player.move(dx=1)
            if event.key == pygame.K_UP: player.move(dy=-1)
            if event.key == pygame.K_DOWN: player.move(dy=1)
        if event.type == RESUME_MUSIC_EVENT:
            pygame.mixer.music.unpause()
            pygame.time.set_timer(RESUME_MUSIC_EVENT, 0)

    
    collected_list = pygame.sprite.spritecollide(player, collectible_sprites, True)
    if collected_list:
        collectibles_collected += len(collected_list)
        item_pickup_sfx.play()
        
        if collectibles_collected == total_collectibles and not puzzle_solved:
            puzzle_solved = True
            pygame.mixer.music.pause()
            puzzle_solved_sfx.play()
            
            resume_time = int(puzzle_solved_sfx.get_length() * 1000)
            pygame.time.set_timer(RESUME_MUSIC_EVENT, resume_time)

            for wall in wall_sprites:
                wall.kill()
            
            portal = Portal(len(current_map_data[0]) - 2, 1)
            all_sprites.add(portal)
            portal_sprites.add(portal)

    if puzzle_solved:
        if pygame.sprite.spritecollide(player, portal_sprites, False):
            portal_entry_sfx.play()
            pygame.time.wait(500)

            # REINICIA O NÍVEL COM UM NOVO LABIRINTO
            player, total_collectibles, current_map_data = setup_level()
            collectibles_collected = 0
            puzzle_solved = False


    for row in range(SCREEN_HEIGHT // TILE_SIZE + 1):
        for col in range(SCREEN_WIDTH // TILE_SIZE + 1):
            screen.blit(floor_img, (col * TILE_SIZE, row * TILE_SIZE))

    for sprite in sorted(all_sprites, key=lambda s: s.rect.centery):
        screen.blit(sprite.image, sprite.rect)

    pygame.display.flip()


pygame.quit()
sys.exit()