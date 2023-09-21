##### range() cria um objeto numérico iterável. Usamos o construtor list() para transforma-lo
##### em uma lista com números, que variam de 0 a 20.

numeros = list(range(0, 21)) 

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
#Função que filtra os números divisiveis por 2 e que restam 0, atribuindo o resultado a váriavel
#numeros_pares

print(numeros_pares)










