import pygame,random,os

#Initial variables
playing, exit, players = False, False, False
jugx, jugy, jug2x, jug2y = 1000,400,1000,600
width, height = 1280,800
points, maxscore, level, pink, green = 0,0,1,0,0
playerWidth, playerHeight = (30,30)
left, right, up, down = (False,False,False,False)
left2, right2, up2, down2 = (False,False,False,False)
starts = False
winner1, finalwinner = None, None
clean, cancel, asteroids = [],[],[]

#Import highscore
os.chdir("E:\Spain\CODES\PYTHON\PYGAME\Asteroids")
file = "highscore.txt"
with open(file,"r",encoding="utf-8") as archivo:
    maxscore = int(archivo.read())

#Init pygame
pygame.init()
wdw = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 36)

#Main loop
while True:
    asteroids = [[-50, 100, 5], [-50, 400, 2], [-50, 350, 5], [-50, 250, 3], [-50, 200, 4], [-50, 300, 3]]
    maxvel = 5

    if starts is False:
        green,pink = (0,0)
        while True:
            wdw.fill((0, 0, 0))
            text_pl1 = font.render("* 1 Player", True, (255, 255, 255))
            text_pl2 = font.render("* 2 Players", True, (255, 255, 255))
            texto3 = font.render("Enter to continue ...", True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        playing = True
                    if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if players is False:
                            players = True
                        else:
                            players = False

            wdw.fill((0, 0, 0))
            if players is False:
                pygame.draw.circle(wdw,(0, 255, 0),(410,270),15)
            else:
                pygame.draw.circle(wdw, (255,0,255), (410, 370), 15)

            wdw.blit(texto3, (400, 160))
            wdw.blit(text_pl1, (400, 260))
            wdw.blit(text_pl2, (400, 360))

            pygame.display.update()
            if playing:
                starts = True
                break

    if players is False:
        jug2x = 3000

    if winner1 is True:
        wdw.fill((0,0,0))
        wins = font.render("VERDE +1!", True, (255, 255, 255))
        wdw.blit(wins, (500, 500))
        pygame.time.delay(1000)
    elif winner1 is False:
        wdw.fill((0, 0, 0))
        wins = font.render("ROSA +1!", True, (255, 255, 255))
        wdw.blit(wins, (500, 500))
        pygame.time.delay(1000)

    jugx, jugy = 1000, 400

    if players:
        jug2x = 1000
        jug2y = 600

    while True:
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                elif event.key == pygame.K_RIGHT:
                    right = True
                elif event.key == pygame.K_UP:
                    up = True
                elif event.key == pygame.K_DOWN:
                    down = True
                elif event.key == pygame.K_a:
                    left2 = True
                elif event.key == pygame.K_d:
                    right2 = True
                elif event.key == pygame.K_w :
                    up2 = True
                elif event.key == pygame.K_s:
                    down2 = True
                elif event.key == pygame.K_ESCAPE:
                    playing = False
                    exit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                elif event.key == pygame.K_RIGHT:
                    right = False
                elif event.key == pygame.K_UP:
                    up = False
                elif event.key == pygame.K_DOWN:
                    down = False
                elif event.key == pygame.K_a:
                    left2 = False
                elif event.key == pygame.K_d:
                    right2 = False
                elif event.key == pygame.K_w:
                    up2 = False
                elif event.key == pygame.K_s:
                    down2 = False
                elif event.key == pygame.K_ESCAPE:
                    playing = False

        #Game Logic
        if left:
            if jugx >=5:
                jugx -= 5
        if right:
            if jugx+playerWidth <= (width-5):
                jugx += 5
        if up:
            if jugy >= 5:
                jugy -= 5
        if down:
            if jugy+playerHeight <= (height-5):
                jugy += 5
        if players is True:
            if left2:
                if jug2x >= 5:
                    jug2x -= 5
            if right2:
                if jug2x + playerWidth <= (width - 5):
                    jug2x += 5
            if up2:
                if jug2y >= 5:
                    jug2y -= 5
            if down2:
                if jug2y + playerHeight <= (height - 5):
                    jug2y += 5

        clock.tick(60)
        asteroidsQuant = len(asteroids)

        for i in range(len(asteroids)):
            asteroids[i][0] += asteroids[i][2]
            if asteroids[i][0] >= width:
                asteroids[i][0] = -50
                asteroids[i][1] = random.randint(0,height-50)
                points += 1

            if asteroids[i][0]+playerWidth > jugx and \
                asteroids[i][0] < jugx + playerWidth and \
                asteroids[i][1] + playerHeight > jugy and \
                asteroids[i][1] < jugy + playerHeight:
                winner1 = True
                points = 0
                level = 1
                playing = False
                pink +=1

            if asteroids[i][0]+playerWidth > jug2x and \
                asteroids[i][0] < jug2x + playerWidth and \
                asteroids[i][1] + playerHeight > jug2y and \
                asteroids[i][1] < jug2y + playerHeight:
                winner1 = False
                points = 0
                level = 1
                playing = False
                green +=1

        if jugx + playerWidth > jug2x and \
            jugx < jug2x + playerWidth and \
            jugy + playerHeight > jug2y and \
            jugy < jug2y + playerHeight:
            if left:
                if jug2x <= 0:
                    left2 = False
                    left = False
                    jugx += 5
                else:
                    jug2x -= 5

            if up:
                if jug2y <= 0:
                    up, up2 = (False, False)
                    jugy += 5
                else:
                    jug2y -= 5

            if right:
                if jug2x + playerWidth >= width:
                    right2 = False
                    right = False
                    jugx -= 5
                else:
                    jug2x += 5

            if down:
                if jug2y + playerHeight >= height:
                    down2 = False
                    down = False
                    jugy -= 5
                else:
                    jug2y += 5

            if left2:
                if jugx <= 0:
                    left2 = False
                    left = False
                    jug2x +=5
                else:
                    jugx -= 5

            if up2:
                if jugy <= 0:
                    up,up2 =(False,False)
                    jug2y +=5
                else:
                    jugy -= 5

            if right2:
                if jugx+playerWidth >= width:
                    right2 = False
                    right = False
                    jug2x -=5
                else:
                    jugx +=5

            if down2:
                if jugy + playerHeight >= height:
                    down2 = False
                    down = False
                    jug2y -=5
                else:
                    jugy +=5

        if points >= int((level*3)**(1+level/100)):
            asteroids.append([-50,random.randint(0,height-50),random.randint(2,maxvel)])
            level += 1
            if level % 5 == 0:
                maxvel += 1

        if points > maxscore:
            maxscore = points

        #Objects
        wdw.fill((0,0,0))
        text = font.render("Puntos: " + str(points), True, (255, 255, 255))
        text2 = font.render("Máx Score: " + str(maxscore), True, (255, 255, 255))
        texto3 = font.render("Jugador pink: " + str(pink)+" - "+"Jugador green: "+str(green), True, (255, 255, 255))

        pygame.draw.rect(wdw, (0, 255, 0), (jugx, jugy, playerWidth, playerHeight))

        if players is True:
            pygame.draw.rect(wdw, (255, 0, 255), (jug2x, jug2y, playerWidth, playerHeight))

        for i in range(len(asteroids)):
            pygame.draw.rect(wdw, (255, 255, 0), (asteroids[i][0], asteroids[i][1], playerWidth,playerHeight))

        wdw.blit(text,(10,10))

        if players is True:
            wdw.blit(texto3, (width-700, 10))
        else:
            wdw.blit(text2, (width-320, 10))


        cancel.sort(reverse=True)

        if len(cancel) != 0:
            asteroids.pop(cancel[0])
            cancel.pop(0)
            if len(cancel) == 0:
                isborrar = False

        pygame.display.update()
        if playing is False:
            break

    with open(file,"w",encoding="utf-8") as archivo:
        archivo.write(str(maxscore))

    playing = True

    #Restore params
    left, right, up, down = (False, False, False, False)
    left2, right2, up2, down2 = (False, False, False, False)

    wdw.fill((0,0,0))

    if pink == 5 or green == 5:
        if pink == 5:
            finalwinner = "pink"
        if green == 5:
            finalwinner = "green"
        starts = False
        playing = False

    if exit:
        break