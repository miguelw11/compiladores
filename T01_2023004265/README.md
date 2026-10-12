# Trabalho 01 - Compiladores

Implementação do Trabalho 01 da disciplina de Compiladores (CC0032)
do curso de Ciência da Computação da UFCA.

## Objetivo

Construir um tradutor dirigido por sintaxe capaz de converter
expressões aritméticas da notação infixa para a notação pós-fixa.

Exemplo:

Entrada:
10 + 20 * 3

Saída:
10 20 3 * +

## Conteúdos abordados

- Tradução dirigida por sintaxe
- Gramáticas livres de contexto
- Eliminação de recursão à esquerda
- Análise sintática descendente recursiva
- Analisador preditivo
- Conjuntos FIRST
- Análise léxica simplificada

## Estrutura

- `tradutor.py`: implementação do tradutor
- `testes.txt`: casos de teste
- `relatorio/`: desenvolvimento da parte teórica do trabalho