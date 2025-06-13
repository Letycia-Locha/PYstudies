print('Olá mundo!')
## tipos de variáveis
idade: int
salario : float
altura: float
genero: str
nome: str

## exemplos
idade = 20
salario = 5800.50
altura = 1.63
genero = 'F'
nome= 'Maria Silva'
x = 30

## saída de dados 
print(f"IDADE = {idade}") ##cocatenação de funções, frase + variável

print('Bom dia', end='') ##saída sem quebra de linha
print('  Saída sem quebra de linha')

print("{:.2f}".format(x))   ##coloca o numero com no máximo duas casas decimáis

##Processamento de dados e casting

x:int 
y:float 
x = 5
y = 2*x

y = int(x) ##pega somente o resultado inteiro de qualquer expressão

d = x//y ##somente o resultado inteiro da divisão


