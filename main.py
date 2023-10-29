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

# Posições iniciais para fazer os traços
traco_x_inicial = 100
traco_y = 400
espacamento = 50

def tracoDasLetras(palavra, traco_x, traco_y, espacamento):
    tracos = []
    for i in range(len(palavra)):
        traco = (traco_x, traco_y)
        tracos.append(traco)
        traco_x += espacamento
    return tracos

gameLoop = True
if __name__ == '__main__':
    print(palavra)
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        draw()
        for traco in tracoDasLetras(palavra, traco_x_inicial, traco_y, espacamento):
            pygame.draw.line(tela, (0, 0, 0), (traco[0], traco_y), (traco[0] + espacamento - 10, traco_y), 2)
        pygame.display.update()
