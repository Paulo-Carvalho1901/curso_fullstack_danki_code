# Em Python, as variáveis funcionam como "caixas" ou espaços de memória para armazenar
# dados. Elas são criadas de forma simples, atribuindo um nome ao valor desejado usando o
# sinal de igual (=), e possuem tipagem dinâmica — o Python identifica o tipo do dado
# automaticamente

# Para criar uma variável, basta escrever o nome escolhido, seguido de = e do valor. 
# Não é necessário especificar o tipo de dado (como em outras linguagens)

nome = "Ana"       # O Python entende que é um texto
idade = 25         # O Python entende que é um número inteiro
altura = 1.65      # O Python entende que é um número decimal
ativo = True       # O Python entende que é um booleano (verdadeiro/falso)

# Regras e Boas Práticas

# Para nomear suas variáveis corretamente, você deve seguir 
# algumas regras essenciais

# * Letras, números e underline: O nome só pode conter esses caracteres.

# * Comece com letras: Não pode iniciar com um número (Ex: 1idade é inválido, mas
# idade1 é permitido).

# * Case sensitive: Maiúsculas e minúsculas fazem diferença (Nome e nome são duas
# variáveis diferentes).

# * Sem palavras reservadas: Não use termos que já são comandos do Python (como
# print, for, if).

# print(dir(__builtins__))

# * Padrão Snake Case: É boa prática separar nomes compostos com underline para
# facilitar a leitura (Ex: taxa_juros em vez de taxaxjuros).


num1 = 5 # (=) sinal de atribuilção, num1 recebe o valor 5
num2 = 3.5


nome = 'Paulo'
nome = "Carvalho"

a = b = c = 'Python'

# Operador "+" sendo usado fazendo soma e concatenando

#############################################################################
# Resultado

print(num1)
print(num2)
print(nome)
print(a)
print(b)
print(c)
print(nome + a)
print(num1 + num2)
