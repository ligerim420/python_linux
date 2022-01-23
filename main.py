
import time
import os
from alg import testMEM
from alg import testCPU
from alg import testGPU
from alg import testDisk


def main():

    while True:
        os.system("clear")
        print('********************')
        print('* 1- Teste Memoria *\n* 2- Teste CPU     * \n* 3- Teste GPU     *\n* 4- Teste HDD/SSD *')
        print('********************')

        teste = int(input('Qual Teste Deseja Fazer?'))

        if teste == 1:
            for x in range(3):
                testMEM()

        if teste == 2:
            for x in range(3):
                testCPU()

        if teste == 3:
            for x in range(3):
                testGPU()

        if teste == 4:
            for x in range(3):
                testDisk()


main()
