import pygame

#Alteracoes feitas como sugestao de melhorias no codigo
#Pensei que a main tava com muito cheia e dessa forma ficaria mais "limpo" :)

TELA_LARGURA = 480
TELA_ALTURA = 854

#Classe SpriteAnimation que herda de pygame.sprite.Sprite
class SpriteAnimation(pygame.sprite.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.frames = frames
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.center = (TELA_LARGURA // 2, 200)

    def update(self):
        self.frame_atual = (self.frame_atual + 1) % len(self.frames)
        self.image = self.frames[self.frame_atual]
