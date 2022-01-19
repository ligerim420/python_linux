
import time
from alg import testMEM
from alg import testCPU
from alg import testGPU


def main():
    print('1- Teste Memoria \n2- Teste CPU \n3- Teste GPU')

    teste = int(input('Qual Teste Deseja Fazer?'))

    while teste > 0:

        if teste == 1:
            testMEM()

        if teste == 2:
            testCPU()

        if teste == 3:
            testGPU()
            break


main()
