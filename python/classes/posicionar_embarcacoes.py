lista_letras = ['a','b','c','d','e','f','g','h','i']
lista_numeros = [1,2,3,4,5,6,7,8]
class Posicionar:
    def __init__(self):
        self.mapa_computador = None
        self.mapa_usuario = None


    def posicionar_submarino(self, quantidade):
        quant_submarino = quantidade
        print('O submarino ocupa 1 espaço no tabuleiro:')
        print(f'Restam {quant_submarino} submarinos!')
        while True:
            posicao = input('Qual a posição deseja?(Ex:A5):')
            self.verificar_posicao_embarcacao('submarino', posicao)
