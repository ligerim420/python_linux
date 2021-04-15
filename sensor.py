import os
import time

sensor = 1
while sensor == 1:
    os.system("clear")
    print("Temperatura")
    os.system("sensors")
    print("Uso de Memoria") 
    os.system("free -m")
    time.sleep(0.8)
