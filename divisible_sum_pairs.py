#Dado um conjunto de inteiros e um inteiro positivo 'k' , determine o número de (i,j) pares onde i<j e ar[j] divisível por k.
##Exemplo
## ar = [1, 2, 3, 4, 5, 6]
## k = 5


#Descrição da função
##Parâmetros
### int n : o comprimento do array 'ar'
### int ar[n] : uma matriz de inteiros
### int k: o divisor inteiro

### retorna - int: o numero de pares

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
