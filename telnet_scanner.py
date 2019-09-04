# import requirements
import sys
import time
import random

# important variables {Change These!}
port_int = 23
time_out_int = 3
time_out = str(time_out_int)
port = str(port_int)

# numpy arrays with combos
combo_user = [
    "user",
    "root",
    "admin",
    "guest",
    "default",
    "support",
    "administator",    
]

combo_passw = [
    "",
    "pass",
    "root",
    "123",     
    "1234",
    "ubnt",
    "user",
    "adm",
    "bin",
    "guest",    
    "vizxv",
    "12345",    
    "password",
]

# searching for existing lists
try:
    with open("list.txt", "r") as iplists:
        combo_ip = iplists.readlines()
        combo_ip = [ip.strip() for ip in combo_ip]
except:
    print("\033[31mERRNO! No 'list.txt' found!\033[0m")
    sys.exit()

# register to a .txt file if successfull hit
print("\033[H\033[J")
class pragma_scan:
    def __init__(self, ip, port, user, passw):
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
    def is_valid(self):
        if self.ip > 1 and len(self.ip) >= 7 and time_out_int <= 61 and time_out_int >= 2:
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
                    "\033[35m" + self.ip + ":" + self.port + "\033[0m is \033[31mnot valid\033[0m!\033[35m 'critical error'\033[0m!"
            )

# start scanner
print("\033[H\033[J")
time.sleep(time_out_int)
for ip in combo_ip:
    random_user = random.choice(combo_user)
    random_passw = random.choice(combo_passw)
    ip_conf = (pragma_scan(ip, port, random_user, random_passw))
    print(ip_conf.is_valid())
    time.sleep(time_out_int)
print("\033[32mDone!\033[0m")
sys.exit()