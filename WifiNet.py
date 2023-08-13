# ALL CREDITS TO JAYTECHPH
# https://github.com/JayTechPH
# https://jaytechph.github.io/about

import subprocess

class WifiNet:
    def __init__(self, ssid, encryption, password):
        self.ssid = ssid
        self.encryption = encryption
        self.password = password

    def generate_powershell_script(self):
        file_content = f'''
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
'''

        subprocess.run(["powershell", "-Command", file_content])

def encryption_type():
    while True:
        encryption = input('Encryption (WPA2 or WPA3): ')
        if encryption in ('2', '3'):
            return encryption
        else:
            print("Invalid encryption value. Please enter 2 or 3.")
            
def password_validation():
    while True:
        password = input('Password: ')
        if len(password) >= 8:
            return password
        else:
            print("Password must be 8 characters or longer. Please try again.")
            
if __name__ == "__main__":
    ssid = input('SSID: ')
    encryption = encryption_type()
    password = password_validation()

    wifi = WifiNet(ssid, encryption, password)
    wifi.generate_powershell_script()
