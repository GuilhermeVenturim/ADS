print('Bem vindo(a)! Siga as instruções abaixo para calcular seu IMC.')

#Declaração de variáveis
altura = float(input('Qual é a sua altura? (Em metro e usando . para separar metro e centímetros)'))
peso = float(input('Qual é o seu peso? (Kg)'))
imc = peso / (altura ** 2)

#print(f'') para indicar um valor do tipo float
#"{imc:.1f}" para exibir somente duas casas decimáis após o ponto
print(f'Seu IMC é : {imc:.1f}')












