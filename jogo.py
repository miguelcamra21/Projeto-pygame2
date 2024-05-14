import pygame 
from classeJogador import *
from obstaculo import *
pygame.init()

tela = pygame.display.set_mode((800,500))
tittle = pygame.display.set_caption("Projeto pygame")
FUNDO = pygame.image.load("imagens/Fundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))


jogador1 = Jogador("imagens/scooby.png",150,80,0,420)


list_bons = [Obstaculo("imagens/icons8-pizza-48.png",90,60,0),
             Obstaculo("imagens/burguer.png",90,60,0),
             Obstaculo("imagens/coca.png",90,60,0),
             Obstaculo("imagens/batata-frita.png",90,60,0),
             Obstaculo("imagens/lasanha.png",90,60,0)]
             

fonte = pygame.font.SysFont("Arial Black",16)
pontos = 0

clock = pygame.time.Clock()
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           rodando = False

    tela.blit(FUNDO,(0,0))
    jogador1.apareca(tela)
    jogador1.movimentosPorTeclas(pygame.K_RIGHT,pygame.K_LEFT)
    

    for comidas in list_bons:
        comidas.apareca(tela)
        comidas.movimentosSozinho()

        if jogador1.mascara.overlap(comidas.mascara,(jogador1.posX - comidas.posX,jogador1.posY - comidas.posY)):
            pontos = pontos + 1

    

    texto_scooby = fonte.render(f"Pontuação scooby: {pontos} ",False,(50,50,225))
    tela.blit(texto_scooby,(0,0))
    pygame.display.update()
    clock.tick(90)