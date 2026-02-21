import pygame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maze Runner")
clock = pygame.time.Clock()

# Colors
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

# Load images
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (30, 30))

goal_img = pygame.image.load("goal.png")
goal_img = pygame.transform.scale(goal_img, (40, 40))

# Load multiple enemy images
enemy_imgs = [
    pygame.image.load("enemy1.png"),
    pygame.image.load("enemy2.png"),
    pygame.image.load("enemy3.png")
]
enemy_imgs = [pygame.transform.scale(img, (40, 40)) for img in enemy_imgs]

# Walls (optional)
walls = [
    pygame.Rect(0,0,600,20), pygame.Rect(0,0,20,600),
    pygame.Rect(580,0,20,600), pygame.Rect(0,580,600,20),
    pygame.Rect(100,0,20,500), pygame.Rect(200,100,20,500),
    pygame.Rect(300,0,20,500), pygame.Rect(400,100,20,500),
    pygame.Rect(500,0,20,500)
]

font = pygame.font.SysFont(None, 48)
speed = 5

# Function to initialize/reset game
def init_game():
    player = pygame.Rect(40, 40, 30, 30)
    goal = pygame.Rect(530, 530, 40, 40)
    enemies = [
        pygame.Rect(350, 20, 30, 30),
        pygame.Rect(250, 280, 40, 40),
        pygame.Rect(400, 400, 40, 40)
    ]
    return player, goal, enemies, False, False

player, goal, enemies, win, lose = init_game()

# Function to check movement
def move(dx, dy):
    temp = player.move(dx, dy)
    return not any(temp.colliderect(w) for w in walls)

# Main game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if not win and not lose:
        if keys[pygame.K_LEFT] and move(-speed,0): player.x -= speed
        if keys[pygame.K_RIGHT] and move(speed,0): player.x += speed
        if keys[pygame.K_UP] and move(0,-speed): player.y -= speed
        if keys[pygame.K_DOWN] and move(0,speed): player.y += speed

        # Check win
        if player.colliderect(goal): win = True

        # Check lose
        if any(player.colliderect(e) for e in enemies): lose = True

    else:
        # Restart game on pressing 'R'
        if keys[pygame.K_r]:
            player, goal, enemies, win, lose = init_game()

    # Draw everything
    screen.fill(WHITE)  # White background
    for w in walls: pygame.draw.rect(screen, BLACK, w)  # Walls (optional)
    screen.blit(goal_img, (goal.x, goal.y))             # Goal image
    for i, e in enumerate(enemies):                     # Enemy images
        screen.blit(enemy_imgs[i], (e.x, e.y))
    screen.blit(player_img, (player.x, player.y))      # Player image

    # Display win/lose message
    if win: screen.blit(font.render("BALEN IS THE PM!", True, (0,200,0)), (200,260))
    if lose: screen.blit(font.render("KP CHOR DESH XOD!", True, (200,0,0)), (190,260))
    if win or lose:
        screen.blit(font.render("Press 'R' to Restart", True, (0,0,200)), (150,320))

    pygame.display.update()

pygame.quit()
