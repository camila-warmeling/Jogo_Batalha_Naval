lista_letras = ['a','b','c','d','e','f','g','h','i']
lista_numeros = [1,2,3,4,5,6,7,8]
class Posicionar:
    def __init__(self, quant_submarino, quant_navio, quant_aviao, tabuleiro):
        self.mapa_computador = None
        self.mapa_usuario = None
     
    def verificacao_posicao_correta(self, posicao):
        if len(posicao) == 2:
            coluna = [0]
            linha = [1]
            if coluna in lista_letras and linha in lista_numeros:
                posicao_correta = posicao
                self.verificar_posicao_vazia(posicao_correta)
            else:
                print('Digite uma posição válida')
        else:
            print(f'Digite uma posição válida')

    def verificar_posicao_vazia(self, posicao):
        self.posicionar_embarcacao(posicao_vazia)

    def posicionar_embarcação(self, posicao, tabuleiro, embarcacao, quantidade):
        coluna = posicao[0] #a
        linha = posicao[1] #5
        posicionar_coluna = lista_letras.index(coluna)
        posicionar_linha = lista_numeros.index(linha)
        tabuleiro[posicionar_linha][posicionar_coluna]: embarcacao+quantidade
        quantidade -= 1

    def posicionar_submarino(self, quantidade):
        quant_submarino = quantidade
        print('O submarino ocupa 1 espaço no tabuleiro:')
        print(f'Restam {quant_submarino} submarinos!')
        while True:
            posicao = input('Qual a posição deseja?(Ex:A5):').strip().lower() #tira os espaços e coloca tudo minusculo
            self.verificar_posicao_embarcacao(posicao)
