expressao = "123 + 45 / 5"
posicao = 0


def proximo():
    global posicao

    while posicao < len(expressao) and expressao[posicao] in " \t":
        posicao += 1

    if posicao >= len(expressao):
        return None

    if expressao[posicao] in "0123456789":
        numero = ""

        while posicao < len(expressao) and expressao[posicao] in "0123456789":
            numero += expressao[posicao]
            posicao += 1

        return ("num", numero)

    caractere = expressao[posicao]
    posicao += 1

    return (caractere, caractere)


while True:
    token = proximo()

    if token is None:
        break

    print(token)