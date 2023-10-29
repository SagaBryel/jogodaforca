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

def desenhar_letras(letras_corretas, tracos):
    fonte = pygame.font.Font(None, 36)
    for i, letra in enumerate(letras_corretas):
        if letra != '_':
            letra_surface = fonte.render(letra, True, (0, 0, 0))
            letra_rect = letra_surface.get_rect()
            letra_rect.center = (tracos[i][0] + espacamento // 2, tracos[i][1] - 30)
            tela.blit(letra_surface, letra_rect)

def desenha_boneco(qtdvidas):#inicialmente será representado por um contador de vidas
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(f'Vidas: {qtdvidas}', True, (0, 0, 0))
    tela.blit(texto, (10, 10))


gameLoop = True
if __name__ == '__main__':
    print(palavra)#com a finalidade de conferencia
    # Cria uma lista inicializada com sublinhados e com numero de elementos igual à quantidade de letras na palavra
    letras_corretas = ['_' for _ in palavra]

    vidas = 3

    while gameLoop:
        if(vidas <= 0):
            gameLoop = False
        for event in pygame.event.get():
            # Clicaram no X na janela para fechar
            if event.type == pygame.QUIT:
                gameLoop = False

            # O jogador interagiu com o teclado
            elif event.type == pygame.KEYDOWN:
                # A tecla pressionada é uma letra
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    # Conversão para maiúscula
                    chute = event.unicode.upper()
                    if chute in palavra:
                        for i, letra in enumerate(palavra):
                            if letra == chute:
                                letras_corretas[i] = chute
                    else:
                        vidas-=1
        tracos = tracoDasLetras(palavra, traco_x_inicial, traco_y, espacamento)
        draw()

        # Desenhando os traços das letras (tela, cor, inicio, fim, largura)
        for traco in tracos:
            pygame.draw.line(tela, (0, 0, 0), (traco[0], traco_y), (traco[0] + espacamento - 10, traco_y), 2)

        desenhar_letras(letras_corretas, tracos)
        desenha_boneco(vidas)
        pygame.display.update()
