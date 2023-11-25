print('Bem vindo(a)! Siga as instruções abaixo para calcular seu IMC.')

#Declaração de funcão para calcular IMC
def calc_imc():
    
#Declaração de variáveis
    altura = float(input('Qual é a sua altura? (Em metro e usando . para separar metro e centímetros)'))
    peso = float(input('Qual é o seu peso? (Kg)'))
    imc = peso / (altura ** 2)
    print(f'Seu IMC é : {imc:.1f}')
    
#Condicionais
    if imc < 18.5:                                                          #Se IMC estiver abaixo de 18.5, está abaixo do peso normal
        print(f'Seu peso está abaixo do normal!')
    elif imc >= 18.5 and imc <25:                                           #Se IMC estiver maior ou igual a 18.5 e abaixo de 25, está com peso normal
        print(f'Seu peso está normal!')
    elif imc > 25 and imc <= 35:                                            #Se IMC estiver maior ou igual 25 e abaixo de 35, está com sobrepeso
        print(f'Você está com sobrepeso!')
    else:                                                                   #Se IMC estiver acima de 35, está com obesidade
        print('Você está com obesidade mórbida, procure ajuda médica!')

#Chamando função
calc_imc()  
    
    





