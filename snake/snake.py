"""
create classic snake game with pygame
"""

import pygame
import random
import time

pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# background image
bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# title and icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

# FPS
fps = pygame.time.Clock()

# score
score_value = 0
font = pygame.font.SysFont(None, 32)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# snake function
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# game over function
def game_over(gameWindow, score):
    gameWindow.fill(white)
    text_screen("Game Over", red, screen_width/2, screen_height/2)
    text_screen("Your Score is: " + str(score), black, screen_width/2, screen_height/2 + 50)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

# main function
def main():
    global score_value
    game_over = False
    game_close = False
    snk_x = 45
    snk_y = 45
    snk_size = 10
    snk_list = []
    snk_length = 1
    # if we want to add more food
    # we can add more food_x and food_y
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    # velocity
    velocity_x = 0
    velocity_y = 0
    # score
    score = 0

    while not game_over:
        if game_close:
            game_over(gameWindow, score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 10
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -10
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -10
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = 10
                    velocity_x = 0

        # snake movement
        snk_x += velocity_x
        snk_y += velocity_y

        # border
        if snk_x > screen_width or snk_x < 0 or snk_y > screen_height or snk_y < 0:
            game_over = True

        # snake eating itself
        if snk_x == food_x and snk_y == food_y:
            score += 1
            food_x = random.randint(20, screen_width/2)
            food_y = random.randint(20, screen_height/2)
            snk_length += 5

        # snake body
        snk_list.append([snk_x, snk_y])
        if len(snk_list) > snk_length:
            del snk_list[0]

        print((snk_x-food_x)**2 + (snk_y-food_y)**2)

        # snake eating food (created by OpenAI Codex)
        # if snk_x == food_x and snk_y == food_y:
        # snake eating food (created by fcomovaz)
        if ((snk_x-food_x)**2 + (snk_y-food_y)**2)<=50:
            score += 1
            food_x = random.randint(20, screen_width/2)
            food_y = random.randint(20, screen_height/2)
            snk_length += 5

        # background
        gameWindow.fill(white)
        gameWindow.blit(bgimg, (0, 0))
        text_screen("Score: " + str(score), red, 5, 5)
        # snake
        plot_snake(gameWindow, black, snk_list, snk_size)
        # food
        pygame.draw.rect(gameWindow, red, [food_x, food_y, snk_size, snk_size])
        pygame.display.update()

        # FPS
        fps.tick(30)

# main function
if __name__ == "__main__":
    main()