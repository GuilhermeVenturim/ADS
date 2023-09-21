#nome = input("Digite um nome: ")
#print (nome)

#print ("Olá, %s, bem vindo ao curso de ADS. Parabéns pelo seu primeiro código em Python!" % (nome))

##### If, Else e Elif

#cor = "Alguma cor"

#if cor == 'verde':
#    print('Acelerar')

#elif cor == 'amarelo':
#    print('Atenção')

#else: 
#    print('Parar')

##### Estruturas condicional booleana

#qtde_faltas = int(input("Digite a quantidade de faltas: "))
#media_final = float(input("Digite a média final: "))

#if qtde_faltas <=5 and media_final >= 7:
#    print("Aluno aprovado!")

#else:
#    print("Aluno reprovado!")

##### Estrutura de repetição WHILE

#numero = 1

#while numero !=0:

#    numero = int(input("Digite um número: "))

#    if numero % 2 ==0:
#        print("Número par!")

#    else:
#        print("Número ímpar!")

##### Estrutura de repetição FOR

#nome = "Guilherme"
#for i, c in enumerate(nome):
#    print(f"Posição = {i}, valor = {c}")

##### Estrutura de repetição RANGE, BREAK e CONTINUE

#nome = "Guilherme"
#for x in range(5):
#    print(x)

##### Usando BREAK: interessante, pois para a execução do trecho de código em execução após atender 
##### a condição estabelecida ('ã').

#disciplina = "Linguagem de programação"

#for c in disciplina:
#    if c == 'ã':
#        break
#    else:
#        print(c)

##### Usando CONTINUE: observado depois da execução do trecho abaixo, que atendido a condição ('ã'), é
##### impresso quase toda a string, menos a condicional ('ã'), e dando continuidade na execução.

#disciplina = "Linguagem de programação"
#for c in disciplina:
#    if c == 'ã':
#        continue
#    else:
#        print(c)

##### EVALUATION

##### Função com parâmetro posicional, obrigatório, com valor default (padrão)
#test
#valor = input("Digite o valor a ser pago: ")
#desconto = input("Digite a porcentagem de desconto: ")


def calcular_desconto(valor, desconto=0):
    #O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) # Não aplicar desconto
valor2 = calcular_desconto(100, 0.25) # Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")





















