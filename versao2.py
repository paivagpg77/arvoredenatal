from colorama import Fore,Style,init
import time
import os 
import random

init()
widht = 21
cores = [Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA]

while True:
    os.system('cls')
    print(Fore.YELLOW + "★".center(widht))

    for i in range(1,20,2):
        cor = random.choice(cores)
        print((cor + '*'* i).center(widht))
    
    print(Fore.RED + '||'.center(19))
    print(Fore.RED + '||'.center(19))
    print(Fore.YELLOW + '======'.center(19))
    print('\n' + Fore.GREEN + 'Feliz Natal!!!')

    time.sleep(0.5)