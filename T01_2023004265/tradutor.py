expressao = input("Digite uma expressão matemática: ")
posicao = 0
saida = []

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

    if caractere in "+-*/()":
        posicao += 1

        return (caractere, caractere)
    raise SyntaxError(f"Caractere inválido: {caractere}")

lookahead = proximo()

def match(tipo_esperado):
    global lookahead

    if lookahead is not None and lookahead[0] == tipo_esperado:
        token_atual = lookahead
        lookahead = proximo()
        return token_atual

    raise SyntaxError(f"Esperado {tipo_esperado}, encontrado {lookahead}")

def fact():
    if lookahead is not None and lookahead[0] == "num":
        token = match("num")
        saida.append(token[1])

    elif lookahead is not None and lookahead[0] == "(":
        match("(")
        expr()
        match(")")
    
    else:
        raise SyntaxError(f"Esperado um número, encontrado {lookahead}")

def term():
    fact()
    T()

def T():
    if lookahead is not None and lookahead[0] == "*":
        match("*")
        fact()
        saida.append("*")
        T()

    elif lookahead is not None and lookahead[0] == "/":
        match("/")
        fact()
        saida.append("/")
        T()

def expr():
    term()
    R()

def R():
    if lookahead is not None and lookahead[0] == "+":
        match("+")
        term()
        saida.append("+")
        R()

    elif lookahead is not None and lookahead[0] == "-":
        match("-")
        term()
        saida.append("-")
        R()

expr()

if lookahead is not None:
    raise SyntaxError(f"Token inesperado: {lookahead}")

print(" ".join(saida))