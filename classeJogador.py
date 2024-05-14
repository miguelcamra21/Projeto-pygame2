import pygame

class Jogador:

    def __init__(self,arquivoImagem,largura,altura,posX,posY):
        self.imagem = pygame.image.load(arquivoImagem) 
        self.largura = largura
        self.altura = altura
        self.imagem =  pygame.transform.scale(self.imagem,(self.largura,self.altura))
        self.posX = posX
        self.posY = posY
        self.mascara = pygame.mask.from_surface(self.imagem)
    
    def apareca(self,tela):
        tela.blit(self.imagem,(self.posX,self.posY))
    
    def movimentosPorTeclas (self,cima,baixo,direita,esquerda):
        keys = pygame.key.get_pressed()
        if keys [direita]:    
            if self.posX < 800 - self.largura:   
                self.posX= self.posX + 5
        elif keys [esquerda]:
            if self.posX > 0:
                self.posX= self.posX - 5
        elif keys [cima]:
            if self.posY > 0:
                self.posY = self.posY - 5
        elif keys [baixo]:
            if self.posY < 500 - self.altura:
                self.posY = self.posY+ 5
