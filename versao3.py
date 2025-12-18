from colorama import Fore, Style, init
import time, os, random

init()

width = 21
cores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]

while True:
    os.system('cls') 


    print(Fore.YELLOW + "★".center(17))


    for i in range(1, 20, 2):
        cor = random.choice(cores)
        print((cor + "*" * i).center(width))


    print(Fore.RED + "||".center(18))
    print(Fore.RED + "||".center(18))

    print(Fore.YELLOW + "======".center(18))

  
    print("\n" + Fore.GREEN + "Feliz Natal!!!".center(width))

    time.sleep(0.5)  