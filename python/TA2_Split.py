##### SPLIT

texto = "Aprendendo Python na disciplina de linguagem de programação."

#Exibi string completa
print(f"Exibindo texto (string) = {texto}")

#Exibe quantidade de itens na sequência
print(f"Tamanho do texto = {len(texto)}")

#Usando a função split sem parâmetro, o corte será em cada espaço em branco no texto.
#Usando ',' como parâmentro, o corte será feito em cada vírgula.
palavras = texto.split()

#Split separa o texto e o transforma em lista
print(f'palavras = {palavras}')

#Exibe quantas itens tem a o valor especificado entre parênteses.
print(f'Tamanho de palavras = {len(palavras)}')















