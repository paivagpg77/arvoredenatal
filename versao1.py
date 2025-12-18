import os
import time

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def arvore(simbolo):
    print('★'.center(20))
    for i in range(1,20,2):
        print((simbolo*i).center(20))
    for _ in range(2):
        print('||'.center(20))
    print('======'.center(20))
    print()
    print('Feliz Natal!!!')

while True:
    limpar()
    arvore('*')
    time.sleep(0.5)

    limpar()
    arvore('*')
    time.sleep(0.5)