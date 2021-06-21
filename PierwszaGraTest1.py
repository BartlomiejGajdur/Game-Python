# importowanie biblioteki
import pygame
import time
import random
#inicjalizacja, rozpocznij program
pygame.init()

#Stwórz ekran gry
screen = pygame.display.set_mode((800, 600))  # szerokość i wysokość
#Nazwa gry
pygame.display.set_caption("Testowa")

#Dodanie ikony gry
ikona = pygame.image.load("assets/1_obrazek.png")
pygame.display.set_icon(ikona)

#Dodanie gracza
graczimg = pygame.image.load("assets/Gracz.png")
graczX = 400
graczY = 500
speedL = 0
speedR = 0
speedU = 0
speedD = 0

#Dodanie przeciwnika
przeciwnikimg=pygame.image.load("assets/przciwnik.png")
przeciwnikX=random.randint(0,736)
przeciwnikY=20
speedE=2
def gracz(x, y): #x- pozycja pionowa y-pozycja pozioma
    screen.blit(graczimg, (x, y)) # Blit oznacza narysuj

def przeciwnik(x,y):
    screen.blit(przeciwnikimg, (x, y))

running = True # Zmienna running true (czyli gra jest otwarta)
while running:    #Kiedy running jest True To gra działa cały czas

    screen.fill((125,0,255)) #R G B  Wypełnij zmienna screen ( czyli nasz program) dany kolor . RGB od 0--->255

    for wydarzenie in pygame.event.get(): #zmienna wydarzenie pobiera klik itp...
        if wydarzenie.type == pygame.QUIT: # Jeżeli klikniemy q QUIT w okienku
            running = False                #To running zmienia się na False i kończy działanie programu
        if wydarzenie.type == pygame.KEYDOWN:
            if wydarzenie.key == pygame.K_LEFT:
                speedL = -1
            if wydarzenie.key == pygame.K_RIGHT:
                speedR = 1
            if wydarzenie.key == pygame.K_UP:
                speedU = -1
            if wydarzenie.key == pygame.K_DOWN:
                speedD = 1
        if wydarzenie.type == pygame.KEYUP:
            if wydarzenie.key == pygame.K_LEFT:
                speedL = 0
            if wydarzenie.key == pygame.K_RIGHT:
                speedR = 0
            if wydarzenie.key == pygame.K_UP:
                speedU = 0
            if wydarzenie.key == pygame.K_DOWN:
                speedD = 0


    print(graczX , graczY)

    graczX += speedL
    graczX += speedR
    graczY += speedU
    graczY += speedD

    if graczX <=0:
        graczX=0
    elif graczX>=772:
        graczX=772
    if graczY<=0:
        graczY=0
    elif graczY >=536:
        graczY=536

 #Ogranicz obszar ruchu przecniwnika
    if przeciwnikX <= 0:
        speedE*=-1   #Jeśli dochodzi do prawej krawędzi zmiena speed na druga strone i przeciwnik wraca.obniza o 32 piksele w dół
        przeciwnikY+= 32
    elif przeciwnikX >= 736:
        speedE*= -1
        przeciwnikY+= 32

    przeciwnikX+=speedE




    gracz(graczX, graczY)  # to musimy dać po screen.fill. Teraz najpierw rysuje ekran a potem gracza
    przeciwnik(przeciwnikX, przeciwnikY)
    time.sleep(0.005)
    pygame.display.update() # Co kazda klatke odswieża nam wyświetlacz # Dla pętli while jest wcięcie



