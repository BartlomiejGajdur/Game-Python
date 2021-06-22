# importowanie biblioteki
import pygame
import time
import random
import math
import pygame.freetype

# inicjalizacja, rozpocznij program
pygame.init()
GAME_FONT= pygame.freetype.Font("assets/ChopinScript.otf",24)
score=0

# Stwórz ekran gry
screen = pygame.display.set_mode((800, 600))  # szerokość i wysokość
# Nazwa gry
pygame.display.set_caption("Testowa")

# Dodanie ikony gry
ikona = pygame.image.load("assets/1_obrazek.png")
pygame.display.set_icon(ikona)

# Dodanie gracza
graczimg = pygame.image.load("assets/Gracz.png")
graczX = 400
graczY = 500
speedL = 0
speedR = 0
speedU = 0
speedD = 0

# Dodanie strzałki
strzalkaimg = pygame.image.load("assets/Strzałka.png")
speedS = -5
strzalkaX = graczX
strzalkaY = graczY
spearState = "ready"  # ready/ throw

# Dodanie przeciwnika
przeciwnikimg = pygame.image.load("assets/przciwnik.png")
przeciwnikX = random.randint(0, 736)
przeciwnikY = 0
speedE = random.randint(-6, 6)


def gracz(x, y):  # x- pozycja pionowa y-pozycja pozioma
    screen.blit(graczimg, (x, y))  # Blit oznacza narysuj


def przeciwnik(x, y):
    screen.blit(przeciwnikimg, (x, y))


def strzalka(x, y):
    global spearState
    spearState = "throw"
    screen.blit(strzalkaimg, (x + 6, y - 32))


def is_Collision(przeciwnikX, przeciwnikY, strzalkaX, strzalkaY):
    distance = math.sqrt((math.pow(przeciwnikX+26 - strzalkaX, 2) + math.pow(przeciwnikY+33- strzalkaY, 2)))
    if distance<43:
        return True
    else:
        return False


def display_box(screen, message):

  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)


running = True  # Zmienna running true (czyli gra jest otwarta)
while running:  # Kiedy running jest True To gra działa cały czas

    screen.fill((125, 0, 255))  # R G B  Wypełnij zmienna screen ( czyli nasz program) dany kolor . RGB od 0--->255

    for wydarzenie in pygame.event.get():  # zmienna wydarzenie pobiera klik itp...
        if wydarzenie.type == pygame.QUIT:  # Jeżeli klikniemy q QUIT w okienku
            running = False  # To running zmienia się na False i kończy działanie programu
        if wydarzenie.type == pygame.KEYDOWN:
            if wydarzenie.key == pygame.K_SPACE:
                strzalkaY = graczY
                strzalkaX = graczX
                strzalka(strzalkaX, strzalkaY)
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



    graczX += speedL
    graczX += speedR
    graczY += speedU
    graczY += speedD

    if graczX <= 0:
        graczX = 0
    elif graczX >= 772:
        graczX = 772
    if graczY <= 0:
        graczY = 0
    elif graczY >= 536:
        graczY = 536

    # Ogranicz obszar ruchu przecniwnika
    if przeciwnikX <= 0:
        speedE *= -1  # Jeśli dochodzi do prawej krawędzi zmiena speed na druga strone i przeciwnik wraca.obniza o 32 piksele w dół
        przeciwnikY += 25
    elif przeciwnikX >= 736:
        speedE *= -1
        przeciwnikY += 25

    przeciwnikX += speedE

    # Strzał przeciwnika na spacji. zaczyna od lokalizacji gracza, przypisuje inna zmienna do lokalizacji gracza i potem idzie w góre np o 200 pixeli w pętli while np

    gracz(graczX, graczY)  # to musimy dać po screen.fill. Teraz najpierw rysuje ekran a potem gracza
    przeciwnik(przeciwnikX, przeciwnikY)
    if spearState == "throw":
        strzalka(strzalkaX, strzalkaY)
        strzalkaY += speedS

    if strzalkaY >= 600 or strzalkaY <= 0:
        spearState = "ready"

    collision = is_Collision(przeciwnikX,przeciwnikY,strzalkaX,strzalkaY)
    if collision == True:
        spearState = "ready"
        spearY=-50
        spearX=-40
        score+=1
        print(score)
        przeciwnikimg = pygame.image.load("assets/przciwnik.png")
        przeciwnikX = random.randint(1, 735)
        przeciwnikY = 0
        speedE = random.choice([2,4,1,-1,-3])

    GAME_FONT.render_to(screen,(40,560),("Wynik: "+ str(score)),(0,0,0))

    display_box(screen,"awiesz")
    # chcialbym zeby to bylo tylko w wpis gracza na ekran

    time.sleep(0.01)
    pygame.display.update()  # Co kazda klatke odswieża nam wyświetlacz # Dla pętli while jest wcięcie
