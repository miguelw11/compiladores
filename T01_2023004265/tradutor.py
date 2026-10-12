
import sys

# Variáveis que guardam o estado da expressão que está sendo analisada.
expressao = ""
posicao = 0
saida = []
lookahead = None


def proximo():
    # Lê o próximo elemento da expressão e avança a posição.
    global posicao

    # Ignora espaços e tabulações entre os elementos.
    while posicao < len(expressao) and expressao[posicao] in " \t":
        posicao += 1

    # Retorna None quando chega ao final da expressão.
    if posicao >= len(expressao):
        return None

    # Se encontrar um número, lê todos os seus dígitos.
    if expressao[posicao] in "0123456789":
        numero = ""

        while posicao < len(expressao) and expressao[posicao] in "0123456789":
            numero += expressao[posicao]
            posicao += 1

        # Identifica o elemento como um número.
        return ("num", numero)

    # Caso não seja um número, verifica se é um operador ou parêntese.
    caractere = expressao[posicao]

    if caractere in "+-*/()":
        posicao += 1
        return (caractere, caractere)

    # Impede a leitura de caracteres que não fazem parte da linguagem.
    raise SyntaxError(f"Caractere inválido: {caractere}")


def match(tipo_esperado):
    # Confere se o próximo elemento é o que o analisador esperava.
    global lookahead

    if lookahead is not None and lookahead[0] == tipo_esperado:
        token_atual = lookahead
        lookahead = proximo()
        return token_atual

    # Informa o erro quando o elemento encontrado é diferente do esperado.
    raise SyntaxError(
        f"Esperado {tipo_esperado}, encontrado {lookahead}"
    )


def fact():
    # Um fator pode ser um número ou uma expressão entre parênteses.
    if lookahead is not None and lookahead[0] == "num":
        token = match("num")

        # Números são adicionados à saída assim que são reconhecidos.
        saida.append(token[1])

    elif lookahead is not None and lookahead[0] == "(":
        match("(")
        expr()  # Analisa a expressão que está dentro dos parênteses.
        match(")")

    else:
        raise SyntaxError(
            f"Esperado um número, encontrado {lookahead}"
        )


def term():
    # Primeiro analisa um fator e depois as operações * e /.
    fact()
    T()


def T():
    # Processa multiplicações e divisões antes de somar ou subtrair.
    while lookahead is not None and lookahead[0] in ("*", "/"):
        operador = lookahead[0]
        match(operador)
        fact()

        # O operador é colocado depois dos operandos na saída pós-fixa.
        saida.append(operador)


def expr():
    # Analisa um termo e depois as operações + e -.
    term()
    R()


def R():
    # Processa somas e subtrações da esquerda para a direita.
    while lookahead is not None and lookahead[0] in ("+", "-"):
        operador = lookahead[0]
        match(operador)
        term()

        # Na notação pós-fixa, o operador aparece depois dos operandos.
        saida.append(operador)


def traduzir(linha):
    # Reinicia as variáveis para analisar uma nova expressão.
    global expressao, posicao, saida, lookahead

    # Remove apenas as quebras de linha do final.
    expressao = linha.rstrip("\r\n")
    posicao = 0
    saida = []
    lookahead = proximo()

    # Inicia a análise sintática da expressão.
    expr()

    # Se sobrar algum elemento, a expressão não foi totalmente reconhecida.
    if lookahead is not None:
        raise SyntaxError(f"Token inesperado: {lookahead}")

    # Junta os elementos da saída, separados por espaços.
    return " ".join(saida)

def main():
    # Se um arquivo foi informado, abre-o para leitura.
    if len(sys.argv) > 2:
        print("Uso: python3 tradutor.py [arquivo.txt]", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1], encoding="utf-8") as arquivo:
                processar_entrada(arquivo)
        except OSError as erro:
            print(f"Erro ao abrir arquivo: {erro}", file=sys.stderr)
            sys.exit(1)
    else:
        # Sem argumento, lê as expressões da entrada padrão.
        processar_entrada(sys.stdin)


def processar_entrada(arquivo):
    # Lê uma expressão por linha e ignora linhas vazias.
    for numero_linha, linha in enumerate(arquivo, start=1):
        if not linha.strip():
            continue

        try:
            print(traduzir(linha))
        except SyntaxError as erro:
            print(
                f"Erro na linha {numero_linha}: {erro}",
                file=sys.stderr
            )


if __name__ == "__main__":
    main()

