from parametros import Parametros

parametros_embarcacoes = Parametros()
submarino = parametros_embarcacoes.quant_submarino
navio = parametros_embarcacoes.quant_navio
aviao = parametros_embarcacoes.quant_aviao

class Posicionar:
    def __init__(self):
        self.mapa_computador = None
        self.mapa_usuario = None


