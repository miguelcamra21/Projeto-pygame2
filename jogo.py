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

list_ruins = [Obstaculo("imagens/maça.png",90,60,0),
              Obstaculo("imagens/laranja.png",90,60,0),
              Obstaculo("imagens/abacate.png",90,60,0)]           

fonte = pygame.font.SysFont("Arial Black",16)
fonte_derrota = pygame.font.SysFont("Arial Black",16)
fonte_vitoria = pygame.font.SysFont("Arial Black",16)
fonte2 = pygame.font.SysFont("Arial Black",16)
pontos = 0
vidas = 5

clock = pygame.time.Clock()
rodando = True
while rodando:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           rodando = False
        
        

    tela.blit(FUNDO,(0,0))
    jogador1.apareca(tela)
    jogador1.movimentosPorTeclas(pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.poder_especial(pygame.K_SPACE)
    

    for comidas in list_bons:
        comidas.apareca(tela)
        comidas.movimentosSozinho()

        if jogador1.mascara.overlap(comidas.mascara,(jogador1.posX - comidas.posX,jogador1.posY - comidas.posY)):
            pontos = pontos + 1
            comidas.posY = 0
            comidas.posX = random.randint(200,600)
        
        if pontos == 10:
            texto_vitoria = fonte.render("Você Ganhou!",False,(0,255,0))
            tela.blit(texto_vitoria,(400,250))
            pygame.display.update()
            pygame.time.wait(250)
            rodando = False
            

    for comidas_ruins in list_ruins:
        comidas_ruins.apareca(tela)
        comidas_ruins.movimentosSozinho()

        if jogador1.mascara.overlap(comidas_ruins.mascara,(jogador1.posX - comidas_ruins.posX,jogador1.posY - comidas_ruins.posY)):
            texto_derrota = fonte.render("Você Perdeu",False,(225,0,0))
            tela.blit(texto_derrota,(400,250))
            pygame.display.update()
            pygame.time.wait(1250)
            rodando = False
            
            
            
    

    texto_scooby = fonte.render(f"Pontuação scooby: {pontos} ",False,(255,0,0))
    tela.blit(texto_scooby,(0,0))
    pygame.display.update()
    clock.tick(90)