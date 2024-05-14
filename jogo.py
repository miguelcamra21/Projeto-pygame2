import pygame 
from classeJogador import *
from obstaculo import *
pygame.init()

tela = pygame.display.set_mode((800,500))
tittle = pygame.display.set_caption("Miguel")
tela.fill((0,100,255))
FUNDO = pygame.image.load("imagens/fundoMar.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

jogador1 = Jogador("imagens/tartaruga2.png",100,80,0,420)
jogador2 = Jogador("imagens/peixe-palhaco.png",75,55,105,445)

list_tuba = [Obstaculo("imagens/icons8-pizza-48.png",90,60,710,100)]
             

fonte = pygame.font.SysFont("Arial Black",16)
pontos = 0
pontosNemo = 0


clock = pygame.time.Clock()
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           rodando = False

    tela.fill((0,100,255))
    tela.blit(FUNDO,(0,0))
    jogador1.apareca(tela)
    jogador1.movimentosPorTeclas(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
    jogador2.movimentosPorTeclas(pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a)
    jogador2.apareca(tela)
    for tuba in list_tuba:
        tuba.apareca(tela)
        tuba.movimentosSozinho()

        if jogador1.mascara.overlap(tuba.mascara,(jogador1.posX - tuba.posX,jogador1.posY - tuba.posY)):
            jogador1.posX = 0
            jogador1.posY = 420
            pontos = pontos - 1
        elif jogador2.mascara.overlap(tuba.mascara,(jogador2.posX - tuba.posX,jogador2.posY - tuba.posY)):
            jogador2.posX = 105
            jogador2.posY = 445
            pontosNemo = pontosNemo - 1

        if jogador1.posY == 0:
            jogador1.posX = 0
            jogador1.posY = 420
            pontos = pontos + 1
        elif jogador2.posY == 0:
            jogador2.posX = 105
            jogador2.posY = 445
            pontosNemo = pontosNemo + 1

    texto_tartaruga = fonte.render(f"Pontuação Tartaruga: {pontos} ",False,(255,0,0))
    texto_nemo = fonte.render(f"Pontuação Nemo: {pontosNemo} ",False,(255,0,0))
    tela.blit(texto_tartaruga,(0,0))
    tela.blit(texto_nemo, (0,20))
    pygame.display.update()
    clock.tick(90)