import os
import time


def testCPU():
    while True:
        os.system("clear")
        print("Benchmark CPU")
        os.system("sysbench cpu --threads=2 run")


def testGPU():
    while True:
        os.system("glmark2")


def testMEM():
    while True:
        os.system("clear")
        print("Temperatura da CPU")
        os.system("sensors")
        print("Uso de Memoria")
        os.system("free -m")
        time.sleep(0.5)
