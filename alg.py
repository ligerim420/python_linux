import os
from signal import pause
import time


def testCPU():

    os.system("clear")
    print("Benchmark CPU")
    os.system("sysbench --test=cpu --num-threads=4 --cpu-max-prime=9999 run")
    os.system("stress --cpu 4 --timeout 300s")


def testGPU():

    os.system("glmark2")


def testMEM():

    os.system("clear")
    print('Criando partição na RAM')
    os.system('sudo mount tmpfs -t tmpfs RAM_teste/')
    os.system('cd RAM_teste')
    time.sleep(3.0)
    print('Realizando testes de escrita na RAM')
    os.system('dd if=/dev/zero of=arquivo_tmp bs=1M count=512 ')
    time.sleep(3.0)
    print('Realizando testes de leitura na RAM')
    os.system('dd if=arquivo_tmp of=/dev/null bs=1M count=512')
    time.sleep(3.0)
    print("Uso de Memoria")
    os.system("free -m")
    os.system('rm arquivo_tmp')
    time.sleep(8.5)


def testDisk():

    os.system("clear")
    print("Velocidade de Escrita")
    os.system('dd bs=16k count=102400 oflag=direct if=/dev/zero of=arquivo_teste')
    print("Velocidade de Leitura")
    os.system('dd bs=16K count=102400 iflag=direct if=arquivo_teste of=/dev/null')
    print('Teste de Desempenho')
    os.system('sudo hdparm -t /dev/sda')
    os.system('rm arquivo_teste')
    time.sleep(3.0)
