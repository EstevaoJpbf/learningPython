import pygame
import random

pygame.init()

# cores usadas no jogo

rosa = (215, 2, 112)
verde = (0, 153, 0)
azul = (0, 56, 168)
amarelo = (255, 255, 102)
vermelho = (216, 34, 47)

# valores iniciais

dimensoes = (600, 600)
clock = pygame.time.Clock()
fonte = pygame.font.SysFont('Cambria Math', 24)

x = 300 # posição inicial da cobra no eixo x
y = 300 # posição inicial da cobra no eixo y

d = 20 # tamanho das unidades da cobra (em pixel)

listaCobra = [[x, y]]

dx = 0 # movimento da cobra em x
dy = 0 # movimento da cobra em y

comidaX = round(random.randrange(0, 600 - d) / 20) * 20 # posição da comida no eixo x
comidaY = round(random.randrange(0, 600 - d) / 20) * 20 # posição da comida no eixo y

tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Jogo da Cobrinha by Estevão J. P. B. de França')

tela.fill(azul)

# definindo quando você perde o jogo (!!! ainda preciso editar pra poder reiniciar o jogo !!!)

def gameOver(): 
    fontePerdeu = pygame.font.SysFont('Cambria Math', 30)
    textoPerdeu = fontePerdeu.render('GAME OVER', True, vermelho)
    tela.fill(azul)
    tela.blit(textoPerdeu, [245, 300])

# desenhando a cobra na tela

def desenhaCobra():
    tela.fill(azul)
    for unidade in listaCobra:
        pygame.draw.rect(tela, rosa, [unidade[0], unidade[1], d, d])

# configurando as teclas que serão usadas pra mover a cobra

def moverCobra(dx, dy, listaCobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx  = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    novoX = listaCobra[-1][0] + dx
    novoY = listaCobra[-1][1] + dy

    listaCobra.append([novoX, novoY])

    del listaCobra[0]

    return dx, dy, listaCobra

# criando comida randomicamente na tela

def verificaComida(dx, dy, comidaX, comidaY, listaCobra):

    head = listaCobra[-1]

    novoX = head[0] + dx
    novoY = head[1] + dy

    if head[0] == comidaX and head[1] == comidaY:
        listaCobra.append([novoX, novoY])
        comidaX = round(random.randrange(0, 600 - d) / 20) * 20
        comidaY = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(tela, verde, [comidaX, comidaY, d, d])

    return comidaX, comidaY, listaCobra

# limitando o movimento da cobra dentro da tela de jogo
  
def verificaParede(listaCobra):
    head = listaCobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        gameOver()

# verificando se a cobra bate nela mesma
        
def verificaMordeuCobra(listaCobra):
    head = listaCobra[-1]
    corpo = listaCobra.copy()

    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
            gameOver()
            
# define a pontuação do jogo (comprimento da cobra)            

def atualizaPontos(listaCobra):
    pts = str(len(listaCobra))
    score = fonte.render('Pontuação: ' + pts, True, amarelo)
    tela.blit(score, [10, 10])

# rodando o jogo
    
while True:
    pygame.display.update()
    desenhaCobra()
    dx, dy, listaCobra = moverCobra(dx, dy, listaCobra)
    comidaX, comidaY, listaCobra = verificaComida(
        dx, dy, comidaX, comidaY, listaCobra)
    verificaParede(listaCobra)
    verificaMordeuCobra(listaCobra)
    atualizaPontos(listaCobra)


    clock.tick(10)
