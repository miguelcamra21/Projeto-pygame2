import pygame
import random
class Obstaculo:
    def __init__(self,arquivoImagem,largura,altura,posX,posY):
        self.imagem = pygame.image.load(arquivoImagem) 
        self.largura = largura
        self.altura = altura
        self.imagem =  pygame.transform.scale(self.imagem,(self.largura,self.altura))
        self.posX = posX
        self.posY = posY
        self.vel = random.randint(1,3)
        self.mascara = pygame.mask.from_surface(self.imagem)

    def apareca(self,tela):
        tela.blit(self.imagem,(self.posX,self.posY))
    
    def movimentosSozinho (self):
        self.posX = self.posX - self.vel
        if self.posX <= 0:
            self.posX = 710
            self.vel = random.randint(1,3)