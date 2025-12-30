import pygame, random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kah Kuromi Be Like")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 30)

# Variáveis do jogo
coins = 0
click_power = 1
auto_power = 0
level = 1

# Imagem da Kuromi
kuromi_img = pygame.image.load("kuromi.png")
kuromi_img = pygame.transform.scale(kuromi_img, (150,150))

particles = []  # Lista para partículas visuais

# Cria partículas quando o player clica
def create_particles(x, y):
    for _ in range(10):
        particles.append([x, y, random.randint(-5,5), random.randint(-5,5), random.randint(10,20)])

# Atualiza e desenha partículas
def draw_particles():
    for p in particles:
        pygame.draw.circle(screen, (255,255,0), (p[0], p[1]), p[4]//2)
        p[0] += p[2]
        p[1] += p[3]
        p[4] -= 1
    for p in particles[:]:
        if p[4] <= 0:
            particles.remove(p)

# Desenha informações do jogo na tela
def draw_text():
    text = font.render(f"Coins: {int(coins)}", True, (255,255,255))
    screen.blit(text, (10,10))
    text2 = font.render(f"Level: {level}", True, (255,255,255))
    screen.blit(text2, (10,50))
    text3 = font.render(f"Click Power: {click_power}", True, (255,255,255))
    screen.blit(text3, (10,90))
    text4 = font.render(f"Auto Power: {auto_power:.1f}", True, (255,255,255))
    screen.blit(text4, (10,130))

# Função de upgrade
def upgrade():
    global coins, click_power, auto_power, level
    if coins >= 50*level:
        coins -= 50*level
        click_power += 1
        auto_power += 0.5
        level += 1

# Loop principal
while True:
    screen.fill((50,0,50))  # Fundo roxo escuro
    mx, my = pygame.mouse.get_pos()

    # Eventos do jogador
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clique na Kuromi
            if kuromi_img.get_rect(topleft=(WIDTH//2-75, HEIGHT//2-75)).collidepoint(mx,my):
                coins += click_power
                create_particles(mx,my)
            # Clique no botão de upgrade
            if pygame.Rect(650,500,120,50).collidepoint(mx,my):
                upgrade()

    coins += auto_power/60  # Incremento automático
    draw_particles()
    screen.blit(kuromi_img, (WIDTH//2-75, HEIGHT//2-75))  # Desenha Kuromi
    pygame.draw.rect(screen, (100,100,100), (650,500,120,50))  # Botão de upgrade
    draw_text()
    pygame.display.flip()
    clock.tick(60)
