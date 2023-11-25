import subprocess
import time
import os

while True:
    os.system("clear")
    list_networks_command = "nmcli device wifi list"
    output = subprocess.check_output(list_networks_command, shell=True, text=True)
    print(output)
    time.sleep(3)
