import pygame
import random

width, height = 1000,1000

pygame.init()
wdw = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas",36)

running = True
loose = False

class Snake:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 10
        self.direction = "DOWN"
        self.color = (23, 165, 137) #verde
        self.body = [(self.x,self.y-10),(self.x,self.y)]
        self.score = 0


    def move(self):
        try:
            self.body.pop(0)
        except:
            pass

        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        self.body.append((self.x,self.y))


        print(self.x,self.y)
        if self.x > width - 20 or self.x < 0 or self.y > height or self.y < 0:
            self.loose()

    def eat(self):
        self.body.append((self.x,self.y))
        self.score += 1

    def loose(self):
        self.score = 0
        self.x = 100
        self.y = 100
        self.body = [(self.x, self.y - 10), (self.x, self.y)]
        self.direction = "DOWN"
        print("PERDIO")


class Food():
    def __init__(self):
        self.x, self.y = 0,0
        self.color = (241, 196, 15)
        self.eaten()

    def eaten(self):
        self.x = random.randint(0, width-20)
        self.y = random.randint(0, height-20)
        print("COME")



#Objetos
mainPlayer = Snake()
food = Food()

while running:
    for event in pygame.event.get():
        # Salir
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        # Moverse
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and mainPlayer.direction != "DOWN":
                mainPlayer.direction = "UP"
            if event.key == pygame.K_DOWN and mainPlayer.direction != "UP":
                mainPlayer.direction = "DOWN"
            if event.key == pygame.K_LEFT and mainPlayer.direction != "RIGHT":
                mainPlayer.direction = "LEFT"
            if event.key == pygame.K_RIGHT and mainPlayer.direction != "LEFT":
                mainPlayer.direction = "RIGHT"
            if event.key == pygame.K_KP_ENTER:
                mainPlayer.eat()
            if event.key == pygame.K_a:
                food.eaten()
                mainPlayer.eat()


        print(food.x,food.y)

    wdw.fill((0,0,0))
    mainPlayer.move()

    print(len(mainPlayer.body))

    # AUTOCHOQUE
    for i in range(len(mainPlayer.body)-1):
        if mainPlayer.body[-1][0] + 10 > mainPlayer.body[i][0] and \
                mainPlayer.body[-1][0] < mainPlayer.body[i][0] + 10 and \
                mainPlayer.body[-1][1] + 10 > mainPlayer.body[i][1] and \
                mainPlayer.body[-1][1] < mainPlayer.body[i][1] + 10:
            loose = True


    # CHOCO

    if mainPlayer.body[-1][0] + 20 > food.x and \
             mainPlayer.body[-1][0] < food.x + 20 and \
             mainPlayer.body[-1][1] + 20 > food.y and \
             mainPlayer.body[-1][1] < food.y + 20:
         food.eaten()
         mainPlayer.eat()

    if loose:
        mainPlayer.loose()


    for i in mainPlayer.body:
        pygame.draw.rect(wdw,mainPlayer.color,(i[0],i[1],20,20))
    pygame.draw.rect(wdw, food.color, (food.x, food.y, 20, 20))

    scoreText = font.render("Score: "+str(mainPlayer.score),True,(255,255,255))
    wdw.blit(scoreText,(height-200,50))


    pygame.time.delay(15)
    pygame.display.update()
    loose = False


