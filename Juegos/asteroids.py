import pygame,random

#Variables
jugando,salir,players = False, False, False
jugx = 1000
jugy = 400
ANCHO = 1280
ALTO = 800
pasaron = 0
maxscore = 0
nivel = 1


jug2x = 1000
jug2y = 600
rosa = 0
verde = 0

ANCHOjug,ALTOjug = (30,30)
left,right,up,down = (False,False,False,False)
left2,right2,up2,down2 = (False,False,False,False)
inicio = False

winner1,finalwinner = None, None

borrar = []
cancel = []

file = "files/04_highscore.txt"
with open(file,"r",encoding="utf-8") as archivo:
    maxscore = int(archivo.read())


pygame.init()
wdw = pygame.display.set_mode((ANCHO,ALTO))
reloj = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 36)



asteroides = []



while True:
    asteroides = [[-50, 100, 5], [-50, 400, 2], [-50, 350, 5], [-50, 250, 3], [-50, 200, 4], [-50, 300, 3]]
    maxvel = 5

    if inicio is False:
        verde,rosa = (0,0)
        while True:
            wdw.fill((0, 0, 0))
            text_pl1 = font.render("* 1 Player", True, (255, 255, 255))
            text_pl2 = font.render("* 2 Players", True, (255, 255, 255))
            texto3 = font.render("Enter para empezar ...", True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        jugando = True
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
            if jugando:
                inicio = True
                break
    print(players)

    if players is False:
        jug2x = 3000

    if winner1 is True:
        wdw.fill((0,0,0))
        wins = font.render("VERDE +1!", True, (255, 255, 255))
        wdw.blit(wins, (500, 500))
        print("GANO VERDE")
        pygame.time.delay(1000)
    elif winner1 is False:
        wdw.fill((0, 0, 0))
        wins = font.render("ROSA +1!", True, (255, 255, 255))
        wdw.blit(wins, (500, 500))
        pygame.time.delay(1000)

    jugx = 1000
    jugy = 400
    if players:
        jug2x = 1000
        jug2y = 600

    while True:
        #Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True
                if event.key == pygame.K_a:
                    left2 = True
                if event.key == pygame.K_d:
                    right2 = True
                if event.key == pygame.K_w :
                    up2 = True
                if event.key == pygame.K_s:
                    down2 = True
                if event.key == pygame.K_ESCAPE:
                    jugando = False
                    salir = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False
                if event.key == pygame.K_a:
                    left2 = False
                if event.key == pygame.K_d:
                    right2 = False
                if event.key == pygame.K_w:
                    up2 = False
                if event.key == pygame.K_s:
                    down2 = False
                if event.key == pygame.K_ESCAPE:
                    jugando = False



        if left:
            if jugx >=5:
                jugx -= 5
        if right:
            if jugx+ANCHOjug <= (ANCHO-5):
                jugx += 5
        if up:
            if jugy >= 5:
                jugy -= 5
        if down:
            if jugy+ALTOjug <= (ALTO-5):
                jugy += 5
        if players is True:
            if left2:
                if jug2x >= 5:
                    jug2x -= 5
            if right2:
                if jug2x + ANCHOjug <= (ANCHO - 5):
                    jug2x += 5
            if up2:
                if jug2y >= 5:
                    jug2y -= 5
            if down2:
                if jug2y + ALTOjug <= (ALTO - 5):
                    jug2y += 5

        #print(left,right,up,down,"   ",left2,right2,up2,down2)

        #Logica
        reloj.tick(60)
        cant_asteroides = len(asteroides)

        for i in range(len(asteroides)):
            asteroides[i][0] += asteroides[i][2]
            if asteroides[i][0] >= ANCHO:
                asteroides[i][0] = -50
                asteroides[i][1] = random.randint(0,ALTO-50)
                pasaron += 1

            if asteroides[i][0]+ANCHOjug > jugx and \
                asteroides[i][0] < jugx + ANCHOjug and \
                asteroides[i][1] + ALTOjug > jugy and \
                asteroides[i][1] < jugy + ALTOjug:
                print("CHOCO EL JUGADOR 1 !!!")
                winner1 = True
                pasaron = 0
                nivel = 1
                jugando = False
                rosa +=1

            if asteroides[i][0]+ANCHOjug > jug2x and \
                asteroides[i][0] < jug2x + ANCHOjug and \
                asteroides[i][1] + ALTOjug > jug2y and \
                asteroides[i][1] < jug2y + ALTOjug:
                print("CHOCO EL JUGADOR 2 !!!")
                winner1 = False
                pasaron = 0
                nivel = 1
                jugando = False
                verde +=1

        if jugx + ANCHOjug > jug2x and \
            jugx < jug2x + ANCHOjug and \
            jugy + ALTOjug > jug2y and \
            jugy < jug2y + ALTOjug:
            print("CHORARON LOS DOS")
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
                if jug2x + ANCHOjug >= ANCHO:
                    right2 = False
                    right = False
                    jugx -= 5
                else:
                    jug2x += 5
            if down:
                if jug2y + ALTOjug >= ALTO:
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
                if jugx+ANCHOjug >= ANCHO:
                    right2 = False
                    right = False
                    jug2x -=5
                else:
                    jugx +=5

            if down2:
                if jugy + ALTOjug >= ALTO:
                    down2 = False
                    down = False
                    jug2y -=5
                else:
                    jugy +=5

        print(nivel, maxvel)




        #print(cant_asteroides,asteroides,borrar,isborrar,i)
        #print(pasaron,nivel)

        if pasaron >= int((nivel*3)**(1+nivel/100)):
            asteroides.append([-50,random.randint(0,ALTO-50),random.randint(2,maxvel)])
            nivel += 1
            if nivel % 5 == 0:
                maxvel += 1

        if pasaron > maxscore:
            maxscore = pasaron

        #print(pasaron)

        #print()







        #Objetos
        wdw.fill((0,0,0))
        texto = font.render("Puntos: " + str(pasaron), True, (255, 255, 255))
        texto2 = font.render("Máx Score: " + str(maxscore), True, (255, 255, 255))
        texto3 = font.render("Jugador rosa: " + str(rosa)+" - "+"Jugador verde: "+str(verde), True, (255, 255, 255))

        pygame.draw.rect(wdw, (0, 255, 0), (jugx, jugy, ANCHOjug, ALTOjug))
        if players is True:
            pygame.draw.rect(wdw, (255, 0, 255), (jug2x, jug2y, ANCHOjug, ALTOjug))

        for i in range(len(asteroides)):
            pygame.draw.rect(wdw, (255, 255, 0), (asteroides[i][0], asteroides[i][1], ANCHOjug,ALTOjug))
        wdw.blit(texto,(10,10))
        if players is True:
            wdw.blit(texto3, (ANCHO-700, 10))
        else:
            wdw.blit(texto2, (ANCHO-320, 10))


        cancel.sort(reverse=True)
        #print(cancel)
        if len(cancel) != 0:
            print(cancel[0])
            asteroides.pop(cancel[0])
            cancel.pop(0)
            if len(cancel) == 0:
                isborrar = False




        pygame.display.update()
        if jugando is False:
            break

    with open(file,"w",encoding="utf-8") as archivo:
        archivo.write(str(maxscore))

    print("SALIRRRRRRRR","GANADOR:", winner1)
    jugando = True
    #salir = True
    #Reestablecer parametros
    left, right, up, down = (False, False, False, False)
    left2, right2, up2, down2 = (False, False, False, False)

    wdw.fill((0,0,0))

    if rosa == 5 or verde == 5:
        if rosa == 5:
            finalwinner = "rosa"
        if verde == 5:
            finalwinner = "verde"
        inicio = False
        jugando = False








    if salir is True:
        break