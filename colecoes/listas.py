#Manipulação de array com python
numeros = [10, 20, 30, 17, 58, 3, 7]
#print(numero[5])

carros = ['Pálio', 'Gol', 'Astra', 'Ka', 'Onix']
print(len(carros)) #retorna o tamanho
print('1.', carros)

carros.append('Kombi')
print('2.', carros)

carros.remove('Gol')
print('3', carros)

del carros[3]
print('4.', carros)

carros = sorted(carros)
print('5.', carros)

