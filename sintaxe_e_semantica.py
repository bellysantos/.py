"""
Sintaxe: Refere-se à sua estrutura de escrita, não ao significado das palavras.
Composta por um conjunto de regras, que valida a sequência de palavras, símbolos e/
ou instruções que é utilizada. Por exemplo:

# Definição de uma função
def soma(a, b):
    resultado = a + b
    return resultado

# Chamada da função
x = 5
y = 3
z = soma(x, y)

print(z)

Semântica: Trata-se da análise do significado das palavras, expressões, símbolos e
instruções da linguagem. É importante que desenvolvedores saibam precisamente o que
as instruções fazem. Por exemplo:

# Operações matemáticas simples
a = 5
b = 2
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print("A soma é:", soma)
print("A subtração é:", subtracao)
print("A multiplicação é:", multiplicacao)
print("A divisão é:", divisao)
"""

"""
Elementos de sintaxe:
# - Comentário.
Quebra de linhas - Não há ponto e vírgula para encerrar a linha.
Indentação: Recuo entre as funções e as linhas (tab).
Espaços em branco: No meio da linha não há importância.
Parênteses: Precedência de operações (2 x 4 + 3 - qual conta irá ter ordem de
importância), funções e argumentos/parâmetros.
"""

# Define o valor do limiar
limiar = 5

menores = [] # Cria lista menores
maiores = [] # Cria lista maiores

# Divide os números de 1 a 10, os maiores e menores

for i in range(10):
		if(i < limiar):
			menores.append(i)
		elif(i > limiar):
			maiores.append(i)

# Imprime na tela os valores das listas

print('Resultado final:')
print('Menores:', menores)
print('Maiores:', maiores)

# Resultado final
# Menores: [0, 1, 2, 3, 4]
# Maiores: [6, 7, 8, 9]