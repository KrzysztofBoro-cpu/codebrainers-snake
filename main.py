import pygame

from model import initialize_snake, initialize_board, set_new_position, initialize_apple, eat_apple, get_score
from view import draw

step = 20
width = 400
height = 400
dimensions = (width, height)

pygame.init()
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("codebrainers-snake")
clock = pygame.time.Clock()

head_direction = 0
board = initialize_board()
snake = initialize_snake(board)
apple = initialize_apple(board)


def turn(direction):
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN] and direction != 0:
        return 2
    if pressed_key[pygame.K_UP] and direction != 2:
        return 0
    if pressed_key[pygame.K_LEFT] and direction != 1:
        return 3
    if pressed_key[pygame.K_RIGHT] and direction != 3:
        return 1
    return direction


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)

    head_direction = turn(head_direction)
    apple = eat_apple(board, snake, apple)
    snake = set_new_position(head_direction, snake, board)
    screen.fill((0, 255, 0))  # kolor tablicy (ekranu gry)

    # kwadrat = pygame.Rect(head_x, head_y, 20, 20)       #pierwsze dwa koordynaty, to jego pozycja na początku, a drugie dwa to jego wymiary w pix
    # pygame.draw.rect(screen, (128,128,128),kwadrat)   #kolor naszego kwadratu(w sensie węża)
    draw(board, screen, get_score(snake))
    pygame.display.flip()
    clock.tick(8)
