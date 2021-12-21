import os
import time

while True:
    os.system("clear")
    print("Temperatura da CPU")
    os.system("sensors")
    print("Uso de Memoria") 
    os.system("free -m")
    time.sleep(0.8)
