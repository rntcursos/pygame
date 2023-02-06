import random
import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

display = pygame.display.set_mode((1280,720))

campo_img = pygame.image.load("assets/bg.png")
campo = campo_img.get_rect()

player1_img = pygame.image.load("assets/player1.png")
player1 = player1_img.get_rect()
player1_score = 0
player1_speed = 6

player2_img = pygame.image.load("assets/player2.png")
player2 = player2_img.get_rect(right=1280)
player2_score = 0

ball_img = pygame.image.load("assets/ball.png")
ball = ball_img.get_rect(center=[1280 /2, 720 / 2])
ball_dir_x = 6
ball_dir_y = 6

font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")

menu_img = pygame.image.load("assets/menu.png")
menu = menu_img.get_rect()

gameover_img = pygame.image.load("assets/gameover.png")
gameover = gameover_img.get_rect()

fade_img = pygame.Surface((1280,720)).convert_alpha()
fade = fade_img.get_rect()
fade_img.fill("black")
fade_alpha = 255

music = pygame.mixer.Sound("assets/music.ogg")
music.play(-1)
hit = pygame.mixer.Sound("assets/pong.wav")

cena = "menu"

fps = pygame.time.Clock()
loop = True
while loop:

    if cena == "jogo":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    loop = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed = -6
                elif event.key == pygame.K_s:
                    player1_speed = 6
        
        if player2_score >= 3:
            cena = "gameover"
            fade_alpha = 255
    
        if player1_score >= 3:
            cena = "gameover"
            fade_alpha = 255

        if ball.colliderect(player1) and ball.x > player1.x + 55:
            ball_dir_x = random.randint(6,8)
            hit.play()
        elif ball.colliderect(player2) and ball.x < player2.x:
            ball_dir_x = random.randint(-8,-6)
            hit.play()
        
        if player1.y <= 0:
            player1.y = 0
        elif player1.y >= 720 - 150:
            player1.y = 720 - 150

        player1.y += player1_speed


        if ball.x <= 0:
            player2_score += 1
            placar_player2 = font.render(str(player2_score), True, "white")
            ball.x = 600
            ball_dir_x *= -1
        elif ball.x >= 1280:
            player1_score += 1
            placar_player1 = font.render(str(player1_score), True, "white")
            ball.x = 600
            ball_dir_x *= -1

        if ball.y <= 0:
            hit.play()
            ball_dir_y = random.randint(4,8)
        elif ball.y >= 720 - 15:
            hit.play()
            ball_dir_y = random.randint(-8,-4)

        ball.x += ball_dir_x 
        ball.y += ball_dir_y 

        if ball.y > player2.y + 75:
            player2.y += 2
        elif ball.y < player2.y + 75:
            player2.y -= 2

        if player2.y <= 0:
            player2.y = 0
        elif player2.y >= 720 - 150:
            player2.y = 720 - 150
        
        if fade_alpha > 0:
            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)

        display.fill((0,0,0))
        display.blit(campo_img, campo)
        display.blit(player1_img, player1)
        display.blit(player2_img, player2)
        display.blit(ball_img, ball)
        display.blit(placar_player1, (500,50))
        display.blit(placar_player2, (780,50))
        display.blit(fade_img, fade)

    elif cena == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "menu"
                    fade_alpha = 255
                if event.key == pygame.K_q:
                    loop = False

        if fade_alpha > 0:
            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)

        display.fill((0,0,0))
        display.blit(gameover_img, gameover)
        display.blit(fade_img, fade)
    
    elif cena == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player1_score = 0
                    placar_player1 = font.render(str(player1_score), True, "white")
                    player2_score = 0
                    placar_player2 = font.render(str(player2_score), True, "white")
                    player1.y = 0
                    player2.y = 0
                    ball.x = 640
                    ball.y = 320
                    cena = "jogo"
                    fade_alpha = 255

                    start = pygame.mixer.Sound("assets/start.wav")
                    start.play()
                if event.key == pygame.K_q:
                    loop = False

        if fade_alpha > 0:
            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)

        display.fill((0,0,0))
        display.blit(menu_img, menu)
        display.blit(fade_img, fade)
    
    fps.tick(60)
    pygame.display.flip()
