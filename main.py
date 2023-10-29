import pygame
import random

# Inicializando o pygame e criando a janela
pygame.init()
# Tela na proporcao 16:9
TELA_LARGURA = 854
TELA_ALTURA = 480
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Jogo da Forca")

# numeros para verde piscina em RGB
verdepis = [60, 85, 80]

# Banco de palavras provisório
palavras = ['CIDADE',
            'SOCIAL',
            'ESTADO']

palavra = random.choice(palavras)

def draw():
    # teste com alteração da cor de fundo
    tela.fill(verdepis)


def traçoDasLetras(palavra, linha_x, linha_y, espacamento):
    linhas = []
    for i in range(len(palavra)):
        linha = (linha_x, linha_y)
        linhas.append(linha)
        linha_x += espacamento
    return linhas

gameLoop = True
if __name__ == '__main__':
    print(palavra)
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        draw()
        pygame.display.update()
