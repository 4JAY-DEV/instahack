import subprocess as sub
import random
os.system("clear")

print("\t8888888b.  Y88b   d88P 888b    888 \t")
print("\t888   Y88b  Y88b d88P  8888b   888 \t")
print("\t888    888   Y88o88P   88888b  888 \t")
print("\t888   d88P    Y888P    888Y88b 888 \t")
print("\t8888888P      Y8888    888  Y8b888 \t")                                                                               
print("\t888 T88b     d88888b   888  Y88888 \t")
print("\t888  T88b   d88P Y88b  888   Y8888 \t")
print("\t888   T88b d88P   Y88b 888    Y888 \t")                                                                                                       
print("")
print("\t \33[94m⊰᯽⊱┈──╌❊ CODED BY R3X1N ❊╌──┈⊰᯽⊱ \t")

print("\t  \033[36m┏━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┓\t")
print("\n\t   \033[93m[#] \033[94mAUTHOR   :  \033[92mPS7CH0 R3X1N                                                          \t ")
print("\t  \033[93m [#] \033[94mGITHUB  : \033[92mgithub.com/PSYCHO-REXIN                                                   \t  ")
print("\t  \033[93m [#] \033[94mINSTA  : \033[92mpsycho_rexin_ofc_                                                         \t")
print("\t  \033[36m┗━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┛\t")
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
def start():

#there educational persposes
#and banner

         sceltadisc = input("\033[93m\033[1m\n\n[!]Use this program  for educational purposes only? [y/n]: ")

         if sceltadisc == "y":
             print("\n")
             os.system("clear")
             print("\t 8888888b.  Y88b   d88P 888b    888   \t")
             print("\t 888   Y88b  Y88b d88P  8888b   888  \t")
             print("\t 888    888   Y88o88P   88888b  888  \t")
             print("\t 888   d88P    Y888P    888Y88b 888  \t")
             print("\t 8888888P     d888b     888 Y88b888  \t")
             print("\t 8888888b  Y88b   d88P 888b    888   \t")
             print("\t 888  T88b   d88P Y88b  888   Y8888  \t")
             print("\t 888   T88b d88P   Y88b 888    Y888  \t")
             print("")
             print("\t \33[94m⊰᯽⊱┈──╌❊ CODED BY R3X1N ❊╌──┈⊰᯽⊱ \t")
             print("")
             print("\t  \033[36m┏━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┓\t")
             print("\n\t   \033[93m[#] \033[94mAUTHOR   :  \033[92mPS7CH0 R3X1N                                                        \t ")
             print("\t  \033[93m [#] \033[94mGITHUB  : \033[92mgithub.com/PSYCHO-REXIN                                                       \t  ")
             print("\t  \033[93m [#] \033[94mINSTA  : \033[92mpsycho_rexin_ofc_                                                          \t")
             print("\t  \033[36m┗━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┛\t")
         else:
                     os.system("xdg-open 'https://instagram.com/psycho_rexin_ofc_?igshid=YmMyMTA2M2Y=/")
                     os.system("clear")
                     print("\t  [#] Insta psycho_rexin_ofc_\t")
                     print("\t  [#]Whatsapp : +1 (706) 514-8680\t")

                     exit()


def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\033[1m\033[92m[?]ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD: ')
        wl = input("[?]Enter the PassList along The Path: ")
        sleepp = int(input("\033[1m\033[91m\n[!]Type the sleep time for login(sec) (Rec:900): "))
        while True:
            sub.call("clear")
            procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
            if procedere == "y":
                veri_break = "si"
                break
            elif procedere == "modify":
                print("\nReturn...")
                break
            elif procedere == "break":
                exit()
            else:
                pass