import pygame
import random
class Obstaculo:
    def __init__(self,arquivoImagem,largura,altura,posY):
        self.imagem = pygame.image.load(arquivoImagem) 
        self.largura = largura
        self.altura = altura
        self.imagem =  pygame.transform.scale(self.imagem,(self.largura,self.altura))
        self.posX = random.randint(100,600)
        self.posY = posY
        self.vel = random.randint(5,10)
        self.mascara = pygame.mask.from_surface(self.imagem)

    def apareca(self,tela):
        tela.blit(self.imagem,(self.posX,self.posY))
    
    def movimentosSozinho (self):
        self.posY = self.posY + self.vel
        if self.posY >= 710:
            self.posY = 0
            self.vel = random.randint(5,20)