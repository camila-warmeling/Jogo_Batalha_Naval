class Tabuleiro:
    def __init__ (self):
        self.tamanho = 8
        self.mapa = None

    def criar_mapa_vazio(self):
        primeira_linha = [' ','A','B','C','D','E','F','G','H','I',]
        mapa = []
        mapa.append(primeira_linha)
        for indice in range(1,9):
            linha = [indice, '•', '•', '•', '•', '•', '•', '•', '•', '•',]
            mapa.append(linha)
        self.mapa = mapa

    def mostrar_mapa(self):
        self.criar_mapa_vazio()
        for linha in self.mapa:
            print(*linha)