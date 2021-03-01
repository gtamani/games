import pygame
import numpy as np
import time

wdw_size = 1000
size_pixels = 20
colors = {"black":(255,255,255),"gray":(128, 128, 128)}

pygame.init()
wdw = pygame.display.set_mode((wdw_size,wdw_size))

def grid(wdw_size,pixel):
    global matrix
    wdw.fill((0, 0, 0))

    for x in range(0,wdw_size,pixel):
        for y in range(0,wdw_size,pixel):
            posy,posx = int((x/pixel)),int((y/pixel))
            cells = int(wdw_size/pixel)
            neighbors = matrix[(posx-1)%cells][(posy)%cells] + \
                        matrix[(posx-1)%cells][(posy-1)%cells] + \
                        matrix[(posx)%cells][(posy-1)%cells] + \
                        matrix[(posx+1)%cells][(posy-1)%cells] + \
                        matrix[(posx+1)%cells][(posy)%cells] + \
                        matrix[(posx+1)%cells][(posy+1)%cells] + \
                        matrix[(posx)%cells][(posy+1)%cells] + \
                        matrix[(posx-1)%cells][(posy+1)%cells]



            if matrix[posx,posy] == 0 and neighbors == 3:
                #Si una célula muerta posee 3 vecinas vivas, revive
                matrix_copy[posx,posy] = 1
            elif matrix[posx,posy] == 1 and (neighbors < 2 or neighbors > 3):
                #Si una célula viva posee 1 vecina o menos muere por soledad.
                #Si una célula viva posee más de 3 vecinas muere por sobrepoblación.
                matrix_copy[posx,posy] = 0
            else:
                matrix_copy[posx,posy] = matrix[posx,posy]

            coordinates = [(x, y), (x + pixel, y), (x + pixel, y + pixel), (x, y + pixel)]
            if matrix_copy[posx,posy] == 0:
                pygame.draw.polygon(wdw, colors["gray"], coordinates, 1)
            if matrix_copy[posx,posy] == 1:
                pygame.draw.polygon(wdw, colors["black"], coordinates, 0)

    matrix = np.copy(matrix_copy)

playing,running = True,False
speed = 0.05

matrix = np.zeros(shape=(int(wdw_size/size_pixels),int(wdw_size/size_pixels)))
matrix_copy = np.copy(matrix)

grid(wdw_size, size_pixels)

while playing:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            xpos = (x // size_pixels)
            ypos = (y // size_pixels)
            x = xpos * size_pixels
            y = ypos * size_pixels
            if matrix[ypos][xpos] == 0:
                matrix[ypos][xpos] = 1
                pygame.draw.polygon(wdw,colors["black"],[(x,y),(x+size_pixels,y),(x+size_pixels,y+size_pixels),(x,y+size_pixels)])
            else:
                matrix[ypos][xpos] = 0
                pygame.draw.polygon(wdw, (0, 0, 0),
                                    [(x, y), (x + size_pixels, y), (x + size_pixels, y + size_pixels),
                                     (x, y + size_pixels)])
                pygame.draw.polygon(wdw, colors["gray"],
                                    [(x, y), (x + size_pixels, y), (x + size_pixels, y + size_pixels),
                                     (x, y + size_pixels)],1)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = True

    if running:
        time.sleep(0.05)
        grid(wdw_size,size_pixels)
        pygame.display.flip()


