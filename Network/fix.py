import subprocess
import os


def enable_wifi():
    os.system("sudo rfkill unblock wifi")
    os.system("sudo ifconfig wlan0 up")
    os.system("sudo nmcli radio wifi on")


def switch_network_manager():
    try:
        subprocess.run("sudo systemctl enable NetworkManager", shell=True)
    except:
        subprocess.run("sudo apt-get install network-manager -y", shell=True)

    subprocess.run("sudo systemctl stop dhcpcd", shell=True)
    subprocess.run("sudo systemctl disable dhcpcd", shell=True)
    subprocess.run("sudo systemctl enable NetworkManager", shell=True)
    subprocess.run("sudo systemctl start NetworkManager", shell=True)


if __name__ == "__main__":
    switch_network_manager()
    enable_wifi()
