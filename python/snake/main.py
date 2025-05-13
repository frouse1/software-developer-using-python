import pygame as pg
from random import randrange
import io 
import os

WINDOW = 1000

def main():
    screen = pg.display.set_mode((WINDOW, WINDOW))
    clock = pg.time.Clock()
    pg.display.set_caption("Taylor's Snake Game")
    snake = [(5, 5), (5, 6), (5, 7)]
    direction = (1, 0)
    apple = (randrange(0, WINDOW // 10), randrange(0, WINDOW // 10))
    score = 0 

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pg.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pg.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pg.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        snake.insert(0, (snake[0][0] + direction[0], snake[0][1] + direction[1]))

        if snake[0] == apple:
            score += 1
            apple = (randrange(0, WINDOW // 10), randrange(0, WINDOW // 10))
        else:
            snake.pop()

        screen.fill((255, 255, 255))
        for segment in snake:
            pg.draw.rect(screen, (0, 255, 0), (segment[0] * 10, segment[1] * 10, 10, 10))
        pg.draw.rect(screen, (255, 0, 0), (apple[0] * 10, apple[1] * 10, 10, 10))
        pg.display.flip()
        clock.tick(15)
        if (snake[0][0] < 0 or snake[0][0] >= WINDOW // 10 or
            snake[0][1] < 0 or snake[0][1] >= WINDOW // 10 or
            len(snake) != len(set(snake))):
            print(f"Game Over! Your score: {score}")
            pg.quit()
            return
        pg.display.set_caption(f"Snake Game - Score: {score}")

def readHighScore():
    score = 0
    try:
        with open("high_score.txt") as f:
            score = int(f.readline().strip())
    except ValueError:
        print(f"high_score file corrupted.")
    except FileNotFoundError:
        print(f"No high_score file found.")
    return score


def writeHighSore(new_score):
    cwd = os.getcwd()
    print (f" My current directory is {cwd}")
    os.chdir("scores\\top_topscores")
    with open("high_score.txt", mode='w') as f:
        f.write(str(new_score))
            
if __name__ == "__main__":
    # main()
    score = readHighScore()
    print (f" The high score is {score}")
    # score = 44
    # writeHighScore(score)
