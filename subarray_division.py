#Divisão da barra de chocolate
## Duas crianças, Lily e Ron, querem dividir uma barra de chocolate. Cada um dos quadrados tem um inteiro nele.

##Lily decide compartilhar um segmento contíguo da barra selecionada de forma que:

##O comprimento do segmento corresponde ao mês de nascimento de Ron e,
##A soma dos números inteiros nos quadrados é igual ao seu dia de nascimento.

### Você recebe uma lista de inteiros (chocolate), um número d (representando o dia do aniversário) e um número m (representando o mês de nascimento).
###bSeu objetivo é descobrir quantos pedaços consecutivos da lista têm exatamente m números e somam d.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    contagem = 0

    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            contagem += 1

    return contagem

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = birthday(s, d, m)

        fptr.write(str(result) + '\n')

        fptr.close()
