# Projeto: Jogo Educativo
## Equipe

    Gabriel Paschoal (6º período)

## Contato

    Gabriel: gabriel.paschoal@edu.ufes.br

## Descrição

O projeto consiste em desenvolver um jogo educativo para inclusão na biblioteca de aplicativos do Laboratório do NCD (Núcleo de Cidadania Digital). O jogo será adicionado a uma plataforma de jogos com palavras relacionadas ao contexto do projeto (Cidadania, Digital) outro projeto para essa plataforma é o Worldle(https://github.com/lgscosta/ncd_gamestation). Após o jogador acertar as palavras, será apresentada uma definição formal. Em estágios avançados do projeto, será incluído um link para uma fonte confiável na internet, permitindo que o jogador aprofunde seus conhecimentos sobre o assunto.
Divisão

## Desafios

    Transformar o jogo de forca em uma experiência multiplayer.

## Tecnologias

    PyGame
    Python

## Problemas e limitações conhecidas

    1) Ao final, quando o jogador vence ou perde uma partida há alguns problemas com a apresentação das definições das palavras.
        - As definições pode sair da telas
        - Caracteres especials não tem tratamento adequado

    2) O codigo está todo em um unico arquivo. Pelomenos as classes deveriam estar em outros arquivos.
    3) Há a possibilidade de iniciar um novo jogo à partir da tela de vitoria mas não à partir da tela de derrota 
    4) Os indicadores das letras, que dão feedback de letras chutadas, erros e acertos, são simples demais.

## Possiveis Melhorias e correções (por ordem de uma pressuposta dificuldade)

    01) Inclusão da possibilidade de iniciar uma nova palavra à partir da tela de derrota
    02) Aprimoramento dos indicadores das letras
    03) Separação do codigo em pelomenos 3 arquivos ("main", "indicadores", "sprites", por exemplo)
    04) Correção do problema com os caracteres especiais e texto fora da janela
    05) 
    06) 
    07) Adição de tela para seleção de modo de jogo 
    08) Adição de modo de jogo de palavras em sequencia, o jogador tem 7 vidas e ao acertar uma palavra aparece a tela de definição, ele recupera até 4 vidas e vai para a proxima palavra
            nesse modo, quando o jogador perde todas as vidas aparece uma tela com a pontuação (numero de palavras que ele acertou e quantas vidas ele perdeu ao longo da partida)
    09) Separação do codigo em pelomenos 3 arquivos ("main", "indicadores", "sprites", por exemplo)
    10) Adição de modo contra o tempo. Nesse modo os jogadores terão duas opções de dificuldade, ambos com 7 vidas, mas com tempos diferentes.

    
