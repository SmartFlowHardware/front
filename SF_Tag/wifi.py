import subprocess
redes= subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
ls=redes.split("\n")
ssids = [k for k in ls if 'SSID' in k]
print(ssids)