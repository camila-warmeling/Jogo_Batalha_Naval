from python.classes.parametros import Parametros
from python.classes.tabuleiro import Tabuleiro
from python.classes.posicionar_embarcacoes import Posicionar

def main():
    parametros = Parametros()
    tabuleiro = Tabuleiro()
    posicionar = Posicionar(
        parametros.quant_submarino, 
        parametros.quant_navio, 
        parametros.quant_aviao, 
        tabuleiro.tabuleiro)
    posicionar.posicionar_submarino()


#Dessa forma, a função main só vai rodar se for esse próprio arquivo.
#Se algum outro arquivo importar o app.py ele não vai rodar automaticamente o jogo.
if __name__ == '__main__':
    main()
