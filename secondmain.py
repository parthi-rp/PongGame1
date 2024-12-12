from random import choice

import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    if opponent.top <  ball.x:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= choice((1,-1))
    ball_speed_y *= choice((1,-1))



screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong game 1")

ball = pygame.Rect(screen_width/2-10,screen_height/2-10,20,20)
opponent = pygame.Rect(10,120,10,150)
player = pygame.Rect(780,120,10,150)

ball_speed_x = 7 * choice((1,-1))
ball_speed_y = 7 * choice((1,-1))

player_speed = 0
opponent_speed = 7

game_active = True
while game_active:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    screen.fill((200,100,100))
    pygame.draw.ellipse(screen, (0, 0, 0), ball)
    pygame.draw.rect(screen, (0,0,0), player)
    pygame.draw.rect(screen, (0,0,0), opponent)

    ball_animation()
    player_animation()
    opponent_animation()

    pygame.display.flip()
    clock.tick(60)