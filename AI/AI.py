import sys


def get_jogadas():
    return [[[1, 0], [0, 1]], [[-1, 0], [0, -1]]]


def joga_jogada(jogada):
    return [[]]


def avalia_tabuleiro(tabuleiro, maximizando_player1):
    return 1


def min_max_root(tabuleiro, profundidade, maximizando_player1):
    # Limite da profundidade atingido
    if profundidade == 0:  # TODO: Ou jogada é final
        return avalia_tabuleiro(tabuleiro, maximizando_player1)

    if maximizando_player1:
        max_h = - sys.maxsize - 1  # Menor inteiro
        max_jogada = None

        fronteira = get_jogadas()
        explorado = []

        for jogada in fronteira:
            fronteira.remove(jogada)

            if jogada not in explorado:  # Para cada jogada
                explorado.append(jogada)

                tabuleiro = joga_jogada(jogada)  # Vê resultado dela

                # Vê resultado do resto da árvore
                resultado = min_max(tabuleiro, profundidade - 1, not maximizando_player1)

                # Escolhe o melhor
                if resultado > max_h:
                    max_h = resultado
                    max_jogada = jogada

        return max_jogada
    else:
        min_h = sys.maxsize  # Maior inteiro
        min_jogada = None

        fronteira = get_jogadas()
        explorado = []

        for jogada in fronteira:
            fronteira.remove(jogada)

            if jogada not in explorado:  # Para cada jogada
                explorado.append(jogada)

                tabuleiro = joga_jogada(jogada)  # Vê resultado dela

                # Vê resultado do resto da árvore
                resultado = min_max(tabuleiro, profundidade - 1, not maximizando_player1)

                # Escolhe o melhor
                if resultado > min_h:
                    min_h = resultado
                    min_jogada = jogada

        return min_jogada


def min_max(tabuleiro, profundidade, maximizando_player1):
    # Limite da profundidade atingido
    if profundidade == 0:  # Ou jogada é final
        return avalia_tabuleiro(tabuleiro, maximizando_player1)

    if maximizando_player1:
        max_h = - sys.maxsize - 1  # Menor inteiro

        fronteira = get_jogadas()
        explorado = []

        for jogada in fronteira:  # Para cada jogada
            fronteira.remove(jogada)

            if jogada not in explorado:
                explorado.append(jogada)

                tabuleiro = joga_jogada(jogada)  # Vê resultado dela

                # Vê resultado do resto da árvore
                resultado = min_max(tabuleiro, profundidade - 1, not maximizando_player1)

                # Escolhe o melhor
                if resultado > max_h:
                    max_h = resultado

        return max_h
    else:
        min_h = sys.maxsize  # Maior inteiro

        fronteira = get_jogadas()
        explorado = []

        for jogada in fronteira:  # Para cada jogada
            fronteira.remove(jogada)

            if jogada not in explorado:

                tabuleiro = joga_jogada(jogada)  # Vê resultado dela

                # Vê resultado do resto da árvore
                resultado = min_max(tabuleiro, profundidade - 1, not maximizando_player1)

                if resultado > min_h:
                    min_h = resultado

        return min_h
