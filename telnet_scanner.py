import sys
import time
import random

sec_int = 0
port_int = 23
time_out_int = 59
time_out = "59"
port = "23"
sec = "0"

combo_user = [
    "root",
    "admin",
    "default",
    "guest",
    "1234",
    "12345",
    "password",
    "ubnt",
    "user",
    "support",
    "default",
    "adm",
    "bin",
    "vizxv",
]

combo_passw = [
    "root",
    "admin",
    "default",
    "guest",
    "1234",
    "12345",
    "password",
    "ubnt",
    "user",
    "support",
    "default",
    "adm",
    "bin",
    "vizxv",
]

try:
    with open("list.txt", "r") as iplists:
        combo_ip = iplists.readlines()
        combo_ip = [ip.strip() for ip in combo_ip]
except:
    print("\033[31mERRNO! No 'list.txt' found!\033[0m")
    sys.exit()

print("\033[H\033[J")
class pragma_scan:
    def __init__(self, ip, port, user, passw):
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
    def is_valid(self):
        if self.ip > "1" and len(self.ip) >= 7 and "#-~`'/,[]()" not in self.ip and self.port == port and "#-~`'/,[]()" not in self.port and time_out_int < 61:
            file = open("telnet.txt", "a")
            file.write(self.ip + ":" + self.port + " " + self.user + ":" + self.passw + "\n")
            return(
                    "Successfully registered \033[35m" + self.ip + ":" + self.port + "\033[0m | \033[35mTimeout: \033[0m" + time_out + "\033[0m"
            )
        elif self.port != "23":
            return (
                    "\033[35m" + self.ip + ":" + self.port + "\033[0m has an \033[31minvalid \033[0m| \033[35mTelnet \033[0m| \033[0mprotocol!\033[0m"
            )
        else:
            return (
                    "\033[35m" + self.ip + ":" + self.port + "\033[0m is \033[31mnot valid\033[0m!\033[35m 'critical value'\033[0m!"
            )

for user in combo_user:
    if combo_user != "":
        print("\033[35mScanning for possible combos \033[0m| \033[35mTimeout: \033[0m" + time_out + "\033[0m")
        sec_int += 1
        if sec_int == time_out_int:
            break
    else:
        print("\033[31mERRNO! Nothing to scan with!\033[0m")
for passw in combo_passw:
    if combo_passw != "":
        print("\033[35mScanning for possible combos \033[0m| \033[35mTimeout: \033[0m" + time_out + "\033[0m")
        sec_int += 1
        if sec_int == time_out_int:
            break
    else:
        print("\033[31mERRNO! Nothing to scan with!\033[0m")

print("\033[H\033[J")
for ip in combo_ip:
    random_user = random.choice(combo_user)
    random_passw = random.choice(combo_passw)
    ip_conf = (pragma_scan(ip, port, random_user, random_passw))
    print(ip_conf.is_valid())
    time.sleep(2)
print("\033[32mDone!\033[0m")
sys.exit()