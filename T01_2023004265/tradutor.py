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


lookahead = proximo()


def match(tipo_esperado):
    global lookahead

    if lookahead is not None and lookahead[0] == tipo_esperado:
        token_atual = lookahead
        lookahead = proximo()
        return token_atual

    raise SyntaxError(f"Esperado {tipo_esperado}, encontrado {lookahead}")

print("Primeiro token:", lookahead)

match("num")
print("Após o primeiro match:", lookahead)

match("+")
print("Após o segundo match:", lookahead)