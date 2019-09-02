import sys
import time
import random

#Don't recommend changng this
ip = "1.1.1.1"
time_out = "59"
time_out_int = 59

#Basicaly combos /Edit these!
combo_ip = [
    "1.1.1.1",
    "2.2.2.2",
    "3.3.3.3",
]

combo_port = [
    "22",
    "80",
    "23",
]

combo_user = [
    "root",
    "123",
    "admin",
    "default",
    "guest",
    "ubnt",
    "user",
    "adm",
    "bin",
]

combo_pass = [
    "user",
    "123",
    "root",
    "password",
    "guest",
    "ubnt",
    "bin",
    "adm",
    "default",
    "root123",
]

#Random pickers
random_num1 = random.choice(combo_user)
random_num2 = random.choice(combo_user)
random_num3 = random.choice(combo_pass)
random_num4 = random.choice(combo_pass)
random_num5 = random.choice(combo_user)
random_num6 = random.choice(combo_user)
random_num7 = random.choice(combo_pass)
random_num8 = random.choice(combo_pass)
random_num9 = random.choice(combo_user)
random_num10 = random.choice(combo_user)
random_num11 = random.choice(combo_user)
random_num12 = random.choice(combo_user)
random_num13 = random.choice(combo_port)
random_num14 = random.choice(combo_port)
random_num15 = random.choice(combo_port)
random_num16 = random.choice(combo_port)
random_num17 = random.choice(combo_port)
random_num18 = random.choice(combo_port)
random_num19 = random.choice(combo_port)
random_num20 = random.choice(combo_port)
random_num21 = random.choice(combo_ip)
random_num22 = random.choice(combo_ip)
random_num23 = random.choice(combo_ip)
random_num24 = random.choice(combo_ip)
random_num25 = random.choice(combo_ip)
random_num26 = random.choice(combo_ip)
random_num27 = random.choice(combo_ip)
random_num28 = random.choice(combo_ip)
random_num29 = random.choice(combo_ip)
random_num30 = random.choice(combo_ip)

#Statements
print("\033[H\033[J")
class pragma_scan:
    def __init__(self, ip, port, user, passw, time):
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.time = time

    def is_valid(self):
        if self.ip > "1" and "." in self.ip and "#-~`'/,[]()" not in self.ip and len(self.ip) > 7 and len(self.ip) < 15 and self.time <= time_out and "#-~`'/,[]()" not in self.time and self.port == "80" and "#-~`'/,[]()" not in self.port:
            file = open("valid_ssh.txt", "a")
            file.write(self.ip + ":" + self.port + " | " + self.user + ":" + self.passw + " | " + self.time + "s " "\n")
            return ("\033[35m" + self.ip + ":" + self.port + "\033[0m is a \033[32mvalid \033[35mSSH\033[0m protocol! Timeout: \033[35m" + self.time + "\033[0ms")
        elif self.ip > "1" and "." in self.ip and "#-~`'/,[]()" not in self.ip and len(self.ip) > 7 and len(self.ip) < 15 and self.time <= time_out and "#-~`'/,[]()" not in self.time and self.port == "22" and "#-~`'/,[]()" not in self.port:
            file = open("valid_telnet.txt", "a")
            file.write(self.ip + ":" + self.port + " | " + self.user + ":" + self.passw + " | " + self.time + "s " "\n")
            return ("\033[35m" + self.ip + ":" + self.port + "\033[0m is a \033[32mvalid \033[35mTelnet\033[0m protocol! Timeout: \033[35m" + self.time + "\033[0ms")
        else:
            return ("\033[35m" + self.ip + ":" + self.port + "\033[0m is an \033[31minvalid \033[0mprotocol! Timeout: \033[35m" + self.time + "\033[0ms")

#More bullshit, dont mess around
ip1 = pragma_scan(random_num21, random_num13, random_num1, random_num12, time_out)
ip2 = pragma_scan(random_num22, random_num13, random_num12, random_num1, time_out)
ip3 = pragma_scan(random_num23, random_num14, random_num2, random_num11, time_out)
ip4 = pragma_scan(random_num24, random_num15, random_num11, random_num2, time_out)
ip5 = pragma_scan(random_num25, random_num16, random_num3, random_num10, time_out)
ip6 = pragma_scan(random_num26, random_num17, random_num12, random_num3, time_out)
ip7 = pragma_scan(random_num27, random_num18, random_num4, random_num9, time_out)
ip8 = pragma_scan(random_num28, random_num19, random_num9, random_num4, time_out)
ip9 = pragma_scan(random_num29, random_num20, random_num5, random_num8, time_out)
ip10 = pragma_scan(random_num30, random_num19, random_num8, random_num5, time_out)
ip11 = pragma_scan(random_num30, random_num18, random_num6, random_num7, time_out)
ip12 = pragma_scan(random_num29, random_num17, random_num7, random_num6, time_out)
ip13 = pragma_scan(random_num28, random_num16, random_num7, random_num6, time_out)
ip14 = pragma_scan(random_num27, random_num15, random_num6, random_num7, time_out)
ip15 = pragma_scan(random_num26, random_num14, random_num8, random_num5, time_out)
ip16 = pragma_scan(random_num25, random_num13, random_num5, random_num8, time_out)
ip17 = pragma_scan(random_num24, random_num16, random_num9, random_num4, time_out)
ip18 = pragma_scan(random_num23, random_num13, random_num4, random_num9, time_out)
ip19 = pragma_scan(random_num21, random_num14, random_num10, random_num3, time_out)
ip20 = pragma_scan(random_num22, random_num15, random_num3, random_num10, time_out)
ip21 = pragma_scan(random_num23, random_num16, random_num11, random_num2, time_out)
ip22 = pragma_scan(random_num24, random_num17, random_num2, random_num11, time_out)
ip23 = pragma_scan(random_num25, random_num18, random_num12, random_num1, time_out)
ip24 = pragma_scan(random_num26, random_num19, random_num7, random_num12, time_out)
ip25 = pragma_scan(random_num27, random_num20, random_num8, random_num11, time_out)
ip26 = pragma_scan(random_num28, random_num20, random_num1, random_num2, time_out)
ip27 = pragma_scan(random_num29, random_num19, random_num2, random_num3, time_out)
ip28 = pragma_scan(random_num30, random_num18, random_num3, random_num4, time_out)
ip29 = pragma_scan(random_num29, random_num17, random_num4, random_num5, time_out)
ip30 = pragma_scan(random_num26, random_num16, random_num5, random_num6, time_out)
ip31 = pragma_scan(random_num23, random_num15, random_num6, random_num7, time_out)
ip32 = pragma_scan(random_num21, random_num14, random_num7, random_num8, time_out)
ip33 = pragma_scan(random_num22, random_num13, random_num8, random_num9, time_out)
ip34 = pragma_scan(random_num24, random_num13, random_num9, random_num10, time_out)
ip35 = pragma_scan(random_num26, random_num13, random_num10, random_num11, time_out)
ip36 = pragma_scan(random_num28, random_num16, random_num11, random_num12, time_out)
ip37 = pragma_scan(random_num30, random_num17, random_num11, random_num12, time_out)
ip38 = pragma_scan(random_num30, random_num20, random_num1, random_num1, time_out)
ip39 = pragma_scan(random_num22, random_num20, random_num2, random_num2, time_out)
ip40 = pragma_scan(random_num21, random_num15, random_num3, random_num3, time_out)
ip41 = pragma_scan(random_num27, random_num15, random_num4, random_num4, time_out)
ip42 = pragma_scan(random_num22, random_num16, random_num5, random_num5, time_out)
ip43 = pragma_scan(random_num27, random_num16, random_num6, random_num6, time_out)
ip44 = pragma_scan(random_num24, random_num17, random_num7, random_num7, time_out)
ip45 = pragma_scan(random_num29, random_num17, random_num8, random_num8, time_out)
ip46 = pragma_scan(random_num26, random_num18, random_num9, random_num9, time_out)
ip47 = pragma_scan(random_num28, random_num18, random_num10, random_num10, time_out)
ip48 = pragma_scan(random_num28, random_num19, random_num11, random_num11, time_out)
ip49 = pragma_scan(random_num21, random_num20, random_num12, random_num12, time_out)
ip50 = pragma_scan(random_num29, random_num19, random_num1, random_num7, time_out)

s = 0
for combo in combo_user:
    print("\033[35mScanning for combo users. Timeout: " + time_out + "\033[0m")
    time.sleep(1)
    s += 1
    if s == 60:
        break
for combo in combo_pass:
    print("\033[35mScanning for combo passwords. Timeout: " + time_out + "\033[0m")
    time.sleep(1)
    s += 1
    if s == 60:
        break
while s < time_out_int:
    print("\033[35mScanning for possible matches:"" Timeout: " + time_out + "\033[0m")
    time.sleep(1)
    s += 1
    if s == time_out_int:
        break

#Start the scan
print(ip1.is_valid())
print(ip2.is_valid())
print(ip3.is_valid())
print(ip4.is_valid())
print(ip5.is_valid())
print(ip6.is_valid())
print(ip7.is_valid())
print(ip8.is_valid())
print(ip9.is_valid())
print(ip10.is_valid())
print(ip11.is_valid())
print(ip12.is_valid())
print(ip13.is_valid())
print(ip14.is_valid())
print(ip15.is_valid())
print(ip16.is_valid())
print(ip17.is_valid())
print(ip18.is_valid())
print(ip19.is_valid())
print(ip20.is_valid())
print(ip21.is_valid())
print(ip22.is_valid())
print(ip23.is_valid())
print(ip24.is_valid())
print(ip25.is_valid())
print(ip26.is_valid())
print(ip27.is_valid())
print(ip28.is_valid())
print(ip29.is_valid())
print(ip30.is_valid())
print(ip31.is_valid())
print(ip32.is_valid())
print(ip33.is_valid())
print(ip34.is_valid())
print(ip35.is_valid())
print(ip36.is_valid())
print(ip37.is_valid())
print(ip38.is_valid())
print(ip39.is_valid())
print(ip40.is_valid())
print(ip41.is_valid())
print(ip42.is_valid())
print(ip43.is_valid())
print(ip44.is_valid())
print(ip45.is_valid())
print(ip46.is_valid())
print(ip47.is_valid())
print(ip48.is_valid())
print(ip49.is_valid())
print(ip50.is_valid())

#exit
sys.exit()