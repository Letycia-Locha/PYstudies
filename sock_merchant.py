##Contagem com dicionário
###exemplo: Há uma grande pilha de meias que devem ser pareadas por cor. Dado um array de inteiros representando a cor de cada meia, determine quantos pares de meias com cores correspondentes existem.

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    pares = 0
    contador = {}

    for cor in ar:  # Para cada meia
        if cor in contador:
            contador[cor] += 1  # Soma 1 se já existe
        else:
            contador[cor] = 1  # Começa com 1 se for a primeira

    for quantidade in contador.values():  # Para cada grupo de meias iguais
        pares += quantidade // 2  # Divide por 2 e soma os pares

    return pares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
