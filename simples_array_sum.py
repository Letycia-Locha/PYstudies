#Dado um conjunto de inteiros, encontre a soma dos seus elementos.
import math
import os
import random
import re
import sys

def simpleArraySum (ar): ##implementa a soma dos elementos da lista 'ar'
    return sum(ar)


    if __name__ == '__main__':
        ftpr = open(os.environ['OUTPUT_PATH'], 'w') ##o HackerRank usa isso para salvar sua resposta em um arquivo temporário
        ar_count = int(input().rstrip()) #recebe a quantidade de elementos do Array
        ar = list(map(int, input().rstrip().rsplit())) ##recebe a entrada de daods - valores do Array
    
        result = simpleArraySum(ar)

        ftpr.write(str(result) + '\n')

        fptr.close()

  