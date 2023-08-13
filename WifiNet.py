# ALL CREDITS TO JAYTECHPH
# https://github.com/JayTechPH
# https://jaytechph.github.io/about

import subprocess
import time
import sys

class WifiNet:
    def __init__(self, ssid=None, encryption=None, password=None):
        self.ssid = ssid
        self.encryption = encryption
        self.password = password

    def generate_powershell_script(self, num):
        file_content = [f'''
$Content = @"
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{self.ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{self.ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA{self.encryption}PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{self.password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
"@

$Content | Out-File -FilePath "WIFINETPROGRAMMATICALLY.xml"
netsh wlan add profile file="WIFINETPROGRAMMATICALLY.xml"
netsh wlan connect name="{self.ssid}" SSID="{self.ssid}"
''',
f"netsh wlan delete profile name={self.ssid}",
"netsh wlan disconnect",
"netsh wlan show profile",
f'netsh wlan connect name="{self.ssid}" SSID="{self.ssid}"',
"netsh wlan show network"
]

        subprocess.run(["powershell", "-Command", file_content[num]])


def encryption_type():
    while True:
        print("Type 'back' to cancel")
        encryption = input('Encryption (WPA2 or WPA3) Enter 2 or 3: ')
        if encryption == "back":
            return
        elif encryption in ('2', '3'):
            return encryption 
        else:
            print("Invalid encryption value. Please enter 2 or 3.")
            
def password_validation():
    while True:
        print("Type 'back' to cancel")
        password = input('Password: ')
        if password == "back":
            return
        elif len(password) >= 8:
            return password
        else:
            print("Password must be 8 characters or longer. Please try again.")
            
def add_network():
    wifi = WifiNet()
    wifi.generate_powershell_script(5)
    print("Type 'back' to cancel")
    ssid = input('SSID: ')
    if ssid == "back": return
    encryption = encryption_type()
    password = password_validation()

    wifi = WifiNet(ssid, encryption, password)
    wifi.generate_powershell_script(0)
    
def connect():
    select = ["""
Select Command
1. Connect Existing Network
2. Add Network
3. Back
""",
"""
 __      __.__  _____.__ 
/  \    /  \__|/ ____\__|
\   \/\/   /  \   __\|  |
 \        /|  ||  |  |  |
  \__/\  / |__||__|  |__|
"""]
    while True:
        print(select[1])
        print(select[0])
        
        select_command = input("Command: ")
        
        if select_command == "1":
            wifi = WifiNet()
            wifi.generate_powershell_script(3)
            print("Type 'back' to cancel")
            ssid = input('SSID: ')
            if ssid == "back": break
            wifi = WifiNet(ssid)
            wifi.generate_powershell_script(4)
            break
        elif select_command == "2":
            disconnect()
            add_network()
            break
        elif select_command == "3":
            break
        else:
            print("Wrong input")
            time.sleep(3)
            
def delete():
    wifi = WifiNet()
    wifi.generate_powershell_script(3)
    print("Type 'back' to cancel")
    ssid = input('SSID: ')
    if ssid == "back": return
    wifi = WifiNet(ssid)
    wifi.generate_powershell_script(1)
    
def disconnect():
    wifi = WifiNet()
    wifi.generate_powershell_script(2)
    input("Press Enter...")
    
def show():
    select = ["""
Select Command
1. Available Network
2. Saved Network
3. Back
""",
"""
 __      __.__  _____.__ 
/  \    /  \__|/ ____\__|
\   \/\/   /  \   __\|  |
 \        /|  ||  |  |  |
  \__/\  / |__||__|  |__|
"""]
    while True:
        print(select[1])
        print(select[0])
        
        select_command = input("Command: ")
        
        if select_command == "1":
            disconnect()
            time.sleep(1)
            wifi = WifiNet()
            wifi.generate_powershell_script(5)
            input("Press Enter...")
            break
        elif select_command == "2":
            wifi = WifiNet()
            wifi.generate_powershell_script(3)
            input("Press Enter...")
            break
        elif select_command == "3":
            break
        else:
            print("Wrong input")
            time.sleep(3)
            
if __name__ == "__main__":
    select = ["""
 __      __.__  _____.__ 
/  \    /  \__|/ ____\__|
\   \/\/   /  \   __\|  |
 \        /|  ||  |  |  |
  \__/\  / |__||__|  |__|
       \/      
""",
"""
Select Command
1. Connect
2. Disconnect
3. DeleteNetwork
4. Show
5. Exit
"""
]

    while True:
        print(select[0])
        print(select[1])
        
        select_command = input("Command: ")
        
        if select_command == "1":
            connect()
        elif select_command == "2":
            disconnect()
        elif select_command == "3":
            delete()
        elif select_command == "4":
            show()
        elif select_command == "5":
            sys.exit()
        else:
            print("Wrong input")
            input("Press Enter...")
        
