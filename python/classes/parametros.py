class Parametros:
    def __init__(self):
        self.nivel_dificuldade_escolhido()
        self.quantidade_submarino()
        self.quantidade_navio()
        self.quantidade_aviao()
        self.mostrar_quantidades()

    def nivel_dificuldade_escolhido(self):
        print('Escolha um nível:\nFácil (f) \nDifícil (d)')
        while True:
            nivel = input('Qual o nível de dificuldade escolhido?:').strip().lower()
            dificuldade = {'f': 'Fácil',
                           'd': 'Difícil'} #dicionário: a chave f tem o valor Fácil
            if nivel in dificuldade:
                self.nivel_dificuldade = nivel[dificuldade]
                break

    def verificacao_quant_embarcacoes(self, max, embarcacao, quant_embarcacao):
        print('Mínimo permitido - 1')
        print(f'Máximo permitido - {max}')
        self.quant_embarcacao = None
        while True:
            quant_embarcacao = input(f'Quantos {embarcacao} você deseja?')
            if quant_embarcacao.isdigit():
                quant_embarcacao = int(quant_embarcacao)
                if quant_embarcacao >=1 and quant_embarcacao <= max:
                    return quant_embarcacao
                else:
                    print(f'Digite somente números de 1 a {max}')
            else:
                print('Digite somente números')

    def quantidade_submarino(self):
        print('Submarino - 1 espaço')
        quant_embarcacao = self.verificacao_quant_embarcacoes(4, 'submarinos', ' ')
        self.quant_submarino = quant_embarcacao
        
    def quantidade_navio(self):
        print('Navio - 3 espaço')
        quant_embarcacao = self.verificacao_quant_embarcacoes(4, 'navios', ' ')
        self.quant_navio = quant_embarcacao

    def quantidade_aviao(self):
        print('Avião - 4 espaço em formato de triângulo')
        quant_embarcacao = self.verificacao_quant_embarcacoes(3, 'aviões', ' ')
        self.quant_aviao = quant_embarcacao
        
    def mostrar_parametros(self):
        print(f'''
        Nível Selecionado:{self.nivel_dificuldade}
        Quantidade de Submarinos: {self.quant_submarino}
        Quantidade de Navios: {self.quant_navio}
        Quantidade de Aviões: {self.quant_aviao}''')


