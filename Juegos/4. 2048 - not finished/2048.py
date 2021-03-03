import pygame
import numpy as np
import random

pygame.init()
pygame.display.set_caption("2048!")
wdw = pygame.display.set_mode((600,600))
font = pygame.font.SysFont("consolas", 36)

def move(direction):
    itNormal, itBackwards = range(4), range(3, -1, -1)
    moves = {276:[itNormal,itBackwards],    #LEFT
             274:[itNormal,itNormal],       #DOWN
             273:[itNormal,itBackwards],    #UP
             275:[itNormal,itNormal]}       #RIGHT

    print("moving ",direction,"!")
    print(moves[direction][0])


    #Second iteration: Move all blocks to the wall
    for a in moves[direction][0]:
        fused = []
        for i in range(3):
            for b in moves[direction][1]:
                #print(a,b,board[a,b])
                    try:
                        if direction == 275:
                            if board[a, b] == 0 and board[a, b - 1] != 0:
                                board[a, b], board[a, b - 1] = board[a, b - 1], 0
                            elif board[a, b] == board[a, b - 1] and board[a, b - 1] not in fused:
                                board[a, b - 1] *= 2
                                board[a, b] = 0
                                fused.append(board[a, b - 1])
                                print(fused)

                        elif direction == 276:
                            if board[a,b] == 0 and board[a,b+1] != 0:
                                board[a,b], board[a,b+1] =  board[a,b+1],0
                            elif board[a,b] == board[a,b+1] and board[a,b+1] not in fused:
                                board[a,b+1] *= 2
                                board[a,b] = 0
                                fused.append(board[a,b+1])
                                print(fused)


                        elif direction == 273:
                            if board[b, a] == 0 and board[b + 1, a] != 0:
                                board[b,a], board[b + 1,a] = board[b+1,a], 0
                            elif board[b,a] == board[b+1,a] and board[b+1,a] not in fused:
                                board[b+1,a] *= 2
                                board[b,a] = 0
                                fused.append(board[b+1,a])

                        elif direction == 274:
                            if board[b, a] == 0 and board[b - 1, a] != 0:
                                board[b, a], board[b - 1, a] = board[b - 1, a], 0
                            elif board[b, a] == board[b - 1, a] and board[b - 1, a] not in fused:
                                board[b - 1, a] *= 2
                                board[b, a] = 0
                                fused.append(board[b - 1, a])

                    except IndexError:
                        pass

    print("Uno\n",board)

def new_block(choices):
    created = False
    while not created:
        y,x = random.randint(0,3), random.randint(0,3)
        if board[y,x] == 0:
            board[y,x] = random.choice(choices)
            created = True
    print(board)

def grid():
    for x in range(0,600,150):
        for y in range(0,600,150):
            pygame.draw.polygon(wdw,(128,128,128),[(x,y),(x+150,y),(x+150,y+150),(x,y+150)],1)

def draw_blocks(board):
    colors = {2:(169, 204, 227),
              4:(174, 214, 241 ),
              8:(163, 228, 215),
              16:(162, 217, 206 ),
              32:(169, 223, 191 ),
              64:(171, 235, 198 ),
              128:(249, 231, 159 ),
              256:(250, 215, 160 ),
              512:(245, 203, 167 ),
              1048:(237, 187, 153 ),
              2048:(230, 176, 170 ),
              5096:(245, 183, 177 )}

    for x in range(4):
        for y in range(4):
            if board[y,x] != 0:
                coordinates = [(x*150,y*150),((x+1)*150,y*150),((x+1)*150,(y+1)*150),\
                    (x*150,(y+1)*150)]
                pygame.draw.polygon(wdw,colors[board[y,x]],coordinates)
                texto = font.render(str(board[y,x]), True, (0,0,0))
                texto.blit(wdw,(x*150+20,y*150+20))



currentLevel = 1
levels = {1:[2,2,2,2,2,2,2,4], #Inicial
          2:[2,2,2,2,2,2,4,4], #Cuando llega a 32
          3:[2,2,2,2,2,4,4,4], #Cuando llega a 64
          4:[2,2,2,2,2,4,4,8], #Cuando llega a 128
          5:[2,2,2,2,4,4,4,8], #Cuando llega a 256
          6:[2,2,2,2,4,4,8,8], #Cuando llega a 512
          7:[2,2,2,4,4,8,8,16], #Cuando llega a 1024
          8:[2,2,4,4,4,8,8,16], #Cuando llega a 2048
          9:[2,2,4,4,8,8,16,32]} #Cuando llega a 5096


board = np.zeros((4,4))
running = True

while running:
    grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [273,274,275,276]:
                new_block(levels[currentLevel])
                move(event.key)
                wdw.fill((0,0,0))
                draw_blocks(board)
    pygame.display.flip()

