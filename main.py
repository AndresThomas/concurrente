import pygame as pg
import threading
import random
from threading import Lock


class player():
    def __init__(self, live, name):
        self.name = name
        self.live = live
        self.lock = Lock()


p1 = player(live=100, name="player 1")
p2 = player(live=100, name="player 2")
pg.init()

size = width, height = 720, 360
# load images
scene = pg.image.load("1.jpg")
player1 = pg.image.load('s.png')
player2 = pg.image.load('b.png')
buttonA = pg.image.load('a.png')
buttonB = pg.image.load('c.png')
buttonC = pg.image.load('a.png')
buttonD = pg.image.load('c.png')
# create world
screen = pg.display.set_mode(size)
pg.display.set_caption('Game')

run = True
playerTurn = True  # true player 1 false player 2

def attack(atacado, damage):
    t = threading.Thread(name="thread", target=calculo, args=(atacado, damage))
    t.start()
    t.join()


def calculo(atacado, damage):
    atacado.lock.acquire() # bloqueamos la vida del jugador
    print(atacado.name +' tiene '+ str(atacado.live))
    atacado.live -= damage
    print(atacado.name +' tiene '+ str(atacado.live))
    atacado.lock.release() # desbloqueamos al jugador


while run:

    screen.blit(scene, (0, 0))
    screen.blit(player1, (200, 120))
    screen.blit(player2, (390, 150))
    screen.blit(buttonA, (140, 100))
    screen.blit(buttonB, (200, 50))
    screen.blit(buttonC, (500, 150))
    screen.blit(buttonD, (450, 100))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # si es un click izq
                if playerTurn:  # si es turno del player 1
                    if (pg.mouse.get_pos()[0] > 199 and pg.mouse.get_pos()[0] < 246) and (pg.mouse.get_pos()[1] > 49 and pg.mouse.get_pos()[1] < 96):
                        attack(atacado=p2, damage=random.randrange(
                            10, 25))
                        playerTurn = False
                    if (pg.mouse.get_pos()[0] > 140 and pg.mouse.get_pos()[0] < 182) and (pg.mouse.get_pos()[1] < 160 and pg.mouse.get_pos()[1] < 146):
                        attack(atacado=p2, damage=random.randrange(
                            2, 10))
                        playerTurn = False
                else:  # turno del player 2
                    if (pg.mouse.get_pos()[0] > 450 and pg.mouse.get_pos()[0] < 491) and (pg.mouse.get_pos()[1] > 100 and pg.mouse.get_pos()[1] < 145):
                        attack(atacado=p1, damage=random.randrange(
                            10, 25))
                        playerTurn = True
                    if (pg.mouse.get_pos()[0] > 500 and pg.mouse.get_pos()[0] < 544) and (pg.mouse.get_pos()[1] > 150 and pg.mouse.get_pos()[1] < 195):
                        attack(atacado=p1, damage=random.randrange(
                            2, 10))
                        playerTurn = True
                
                if (p1.live < 0):
                    run = False
                    print('player 2 wins')
                if(p2.live < 0):
                    run = False
                    print('player 1 wins')
    pg.display.update()

pg.quit()
