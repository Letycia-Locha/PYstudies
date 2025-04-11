## Um caminhante ávido mantém registros meticulosos de suas caminhadas. Durante a última caminhada que levou exatamente 'step' passos, para cada passo era anotado se era uma subida , `U`, ou uma descida `D` ,passo. As caminhadas sempre começam e terminam no nível do mar, e cada degrau para cima ou para baixo representa uma 1 mudança de unidade em altitude. Definimos os seguintes termos:

##Uma montanha é uma sequência de degraus consecutivos acima do nível do mar, começando com um degrau acima do nível do mar e terminando com um degrau abaixo até o nível do mar.
##Um vale é uma sequência de degraus consecutivos abaixo do nível do mar, começando com um degrau abaixo do nível do mar e terminando com um degrau acima até o nível do mar.
##Dada a sequência de subidas e descidas durante uma caminhada, encontre e imprima o número de vales percorridos.

## Exemplo
### steps = 8path = [DDUUUUDD]

#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    altitude = 0
    vales = 0

    for passo in path:
        if passo == 'U':
            altitude += 1
            if altitude == 0:
                vales += 1  # voltou ao nível do mar: final de um vale
        else:  # passo == 'D'
            altitude -= 1

    return vales

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()