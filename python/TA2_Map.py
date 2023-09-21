##### map() é utilizado para aplicar determinada função em cada item de um objeto iterável.

print("Exemplo")

linguagens = '''Python Java JavaScript'''.split()   #split() sem argumento, por padrão, quebra a string pelos espaços vazios entre os elementos
nova_lista = map(lambda x: x.lower(), linguagens)   #lambda entra como função anônima
print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")
























