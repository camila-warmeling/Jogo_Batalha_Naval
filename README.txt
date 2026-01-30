BÁSICAS DE COMO SERÁ O JOGO
    computador x usuario
    usuario vai ter que posicionar no máximo: 4 submarinos(1 espaço), 4 navio(3 espaços) e 4 avião (4 espaços dispostos como uma base de 3 e 1 acima no meio)
    tabuleiro 8x8
    níveis:
    fácil - computador joga aleatoriamente as bombas
    médio - computador segue uma lógica tentando seguir o desenho do veículo caso acerte
    difícil - ?
    o ~ é quando acerta a água e o x quando acerta um veículo
    jogador começa jogando sempre      |                    +
    se a embarcação for destruída: --- |  no caso do avião +++

FUNCIONAMENTO SISTEMA
    escolher nível de dificuldade
    posicionar veículos (se é barco, são 3 casas) começando da ponta. Pode ser vertical ou horizontal
    posicionar aleatoriamente os veículos do computador
    mostrar mapa com os veículos do usuário e o do computador com as posições com o • (tecla da vírgula)
    verificação se acertou algum veículo e mostrar os ícones certo para cada ocasião
    posicionamento dos veículos (vertical ou horizontal)
    mapa é uma função já pronta com for 
    função que reincia o mapa do usuário e do computador

FORMA DE ATAQUE DO USUÁRIO
    opção 1 - o mapa deve ter números na linha superior/inferios e letras nas linhas laterais (semelhante ao xadrez)
    opção 2 - ele clica no ponto que deseja para atacar (interface gráfica)

NIVEL 1
    joga números aleatórios de 1 a 8 em cada posição da matriz

NIVEL 2
    joga números aleatórios caso não tenha acertado nenhum veículo ainda ou após tiver destruído um veículo
    caso acerte vai sortear uma posição para seguir (cima, baixo, direito, esquerdo)
    se acertar dois um ao lado do outro segue em linha reta, quando acertar a água ele volta e continua na direção contrária
    se acertar a água e não distruir a embarcação ele vai ou para cima ou para baixo