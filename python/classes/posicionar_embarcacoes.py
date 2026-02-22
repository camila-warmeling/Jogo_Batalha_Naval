lista_letras = ['a','b','c','d','e','f','g','h','i']
lista_numeros = [1,2,3,4,5,6,7,8]
class Posicionar:
    def __init__(self, quant_submarino, quant_navio, quant_aviao, tabuleiro):
        self.quant_submarino = quant_submarino
        self.quant_navio = quant_navio
        self.quant_aviao = quant_aviao
        self.tabuleiro = tabuleiro
     
    def verificar_posicao_correta(self, posicao):
        if len(posicao) == 2:
            linha = posicao[1]
            coluna = posicao[0]
            if coluna in lista_letras and linha in lista_numeros:
                return linha, coluna
            else:
                print('Digite uma posição válida')
                return None
        else:
            print(f'Digite uma posição válida')
            return None

    def verificar_posicao_vazia(self, linha, coluna):
        posicao_vazia = self.tabuleiro.tabuleiro[linha][coluna]
        if posicao_vazia == '•':
            return True
        else:
            print('a posição não está vazia!')
            return None

    def posicionar_embarcação(self, embarcacao, linha, coluna):
        posicionar_coluna = lista_letras.index(coluna)
        posicionar_linha = lista_numeros.index(linha)
        self.tabuleiro[posicionar_linha][posicionar_coluna] = embarcacao+self.quantidade
        quantidades = {
            's': self.quant_submarino,
            'n': self.quant_navio,
            'a': self.quant_aviao
        }
        self.quantidades[embarcacao] -= 1
        self.tabuleiro = self.tabuleiro
        

    def posicionar_submarino(self):
        while self.quant_submarino != 0:
            print(f'Esse é o seu tabuleiro  atual:')
            self.tabuleiro.mostrar_tabuleiro()
            print('O submarino ocupa 1 espaço no tabuleiro:')
            print(f'Restam {self.quant_submarino} submarinos!')
            posicao = input('Qual a posição deseja?(Ex:A5):').strip().lower() #tira os espaços e coloca tudo minusculo
            posicao_correta = self.verificar_posicao_correta(posicao)
            if posicao_correta != None:
                linha, coluna = posicao_correta
                posicao_vazia = self.verificar_posicao_vazia(linha, coluna)
                if posicao_vazia == True:
                    embarcacao = 's'
                    quantidade = self.quant_submarino
                    self.posicionar_embarcação(embarcacao, linha, coluna)
                   
