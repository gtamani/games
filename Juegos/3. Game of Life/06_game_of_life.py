import pygame
import numpy as np
import time, random, os


#Initial variables
wdw_size, size_pixels = 900, 15
colors = {"white":(255,255,255),"gray":(128, 128, 128),"black":(0,0,0)}


#Pygame config
pygame.init()
wdw = pygame.display.set_mode((wdw_size,wdw_size))
pygame.display.set_caption("Game of life!")


#Functions
def grid(wdw_size,pixel):
    global matrix
    wdw.fill(colors["black"])

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
                # If a dead cell has 3 neighbors, it gets back to life.
                matrix_copy[posx,posy] = 1
            elif matrix[posx,posy] == 1 and (neighbors < 2 or neighbors > 3):
                # If a cell is alive and has one or none neighbors, it dies.
                # If a cell has more than 3 neighbors, dies due to overpopulation.
                matrix_copy[posx,posy] = 0
            else:
                matrix_copy[posx,posy] = matrix[posx,posy]

            coordinates = [(x, y), (x + pixel, y), (x + pixel, y + pixel), (x, y + pixel)]
            if matrix_copy[posx,posy] == 0:
                pygame.draw.polygon(wdw, colors["gray"], coordinates, 1)
            if matrix_copy[posx,posy] == 1:
                pygame.draw.polygon(wdw, colors["white"], coordinates, 0)

    matrix = np.copy(matrix_copy)

def save():
    name = ""
    for times in range(10):
        name += random.choice("abcdefghijklmnopqrstuvwxyz123456789")
    path = "saved/"+name+".txt"
    np.savetxt(path, matrix, "%d")

def change_plot(left,current_plot):
    print(os.getcwd())
    os.chdir("E:/Spain/CODES/VUE.JS/games/Juegos/3. Game of Life")
    plots = os.listdir(os.getcwd()+os.sep+"saved")
    current_plot += left
    current_plot %= len(plots)
    print(plots[current_plot])
    return np.loadtxt("saved/"+plots[current_plot]),current_plot

current_plot = 0
playing,running = True,False
speed = 0.05

matrix = np.zeros(shape=(int(wdw_size/size_pixels),int(wdw_size/size_pixels)))
matrix_copy = np.copy(matrix)
grid(wdw_size, size_pixels)


# Main loop
while playing:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            xpos = (x // size_pixels)
            ypos = (y // size_pixels)
            x = xpos * size_pixels
            y = ypos * size_pixels
            if matrix[ypos][xpos] == 0:
                matrix[ypos][xpos] = 1
                pygame.draw.polygon(wdw,colors["white"],[(x,y),(x+size_pixels,y),(x+size_pixels,y+size_pixels),(x,y+size_pixels)])
            else:
                matrix[ypos][xpos] = 0
                pygame.draw.polygon(wdw, colors["black"],
                                    [(x, y), (x + size_pixels, y), (x + size_pixels, y + size_pixels),
                                     (x, y + size_pixels)])
                pygame.draw.polygon(wdw, colors["gray"],
                                    [(x, y), (x + size_pixels, y), (x + size_pixels, y + size_pixels),
                                     (x, y + size_pixels)],1)

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if running:
                        running = False
                    else:
                        running = True
                elif event.key == pygame.K_s:
                    save()
                elif event.key == pygame.K_LEFT:
                    matrix, current_plot = change_plot(-1,current_plot)
                    wdw.fill(colors["black"])
                    grid(wdw_size, size_pixels)
                elif event.key == pygame.K_RIGHT:
                    matrix, current_plot = change_plot(1,current_plot)
                    wdw.fill(colors["black"])
                    grid(wdw_size, size_pixels)

    if running:
        time.sleep(0.02)
        grid(wdw_size,size_pixels)
        pygame.display.flip()


