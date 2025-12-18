import customtkinter as ctk
import random

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

app = ctk.CTk()
app.title("Árvore de Natal 🎄")
app.geometry('400x500')
app.resizable(False,False)

fonte = ctk.CTkFont(family='Courier New ', size=16)

label_arvore = ctk.CTkLabel(app, text='', font = fonte, justify='left')

label_arvore.pack(pady=20)
cores = ['red', 'green','yellow', 'blue', 'magenta']

def gerar_arvore():
    width = 21
    texto = ''

    texto += "★".center(width) + "\n"
    for i in range(20):
        texto += ('*'*i).center(width)+'\n'
    texto += "||".center(27) + "\n"
    texto += "||".center(27) + "\n"
    texto += "======".center(22) + "\n\n"
    texto += "Feliz Natal!!!".center(width)

    return texto

def piscar():
    cor = random.choice(cores)
    label_arvore.configure(text = gerar_arvore(),text_color=cor)
    app.after(500,piscar)

piscar()
app.mainloop()