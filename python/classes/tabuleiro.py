class Tabuleiro:
    def __init__ (self):
        self.criar_tabuleiro_vazio()

    def criar_tabuleiro_vazio(self):
        primeira_linha = [' ','A','B','C','D','E','F','G','H','I']
        tabuleiro = []
        tabuleiro.append(primeira_linha)
        for indice in range(1,9):
            linha = [indice, '•', '•', '•', '•', '•', '•', '•', '•', '•']
            tabuleiro.append(linha)
        self.tabuleiro = tabuleiro

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print(*linha) #* tira os caracteres como , '' () das listas