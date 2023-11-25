import bluetooth
import time
import os

nearby_devices = bluetooth.discover_devices(lookup_names=True)

while True:
    time.sleep(1)
    os.system("clear")
    for addr, name in nearby_devices:
        print(f"{addr} - {name}")
