import subprocess
import os


def enable_wifi():
    os.system("sudo rfkill unblock wifi")
    os.system("sudo ifconfig wlan0 up")
    os.system("sudo nmcli radio wifi on")


if __name__ == "__main__":
    enable_wifi()
