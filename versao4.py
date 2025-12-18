import customtkinter as ctk
import random


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


app = ctk.CTk()
app.title("Árvore de Natal 🎄")
app.geometry("420x560")
app.resizable(False, False)


fonte = ctk.CTkFont(family="Courier New", size=16)


label_arvore = ctk.CTkLabel(
    app,
    text="",
    font=fonte,
    justify="left"
)
label_arvore.pack(pady=20)

cores = ["red", "green", "yellow", "blue", "magenta"]

rodando = False  # controla o pisca

def gerar_arvore():
    width = 21
    linhas = []

    linhas.append("★".center(width))

    for i in range(1, 20, 2):
        linhas.append(("*" * i).center(width))

    linhas.append("||".center(width))
    linhas.append("||".center(width))
    linhas.append("======".center(width))
    linhas.append("")
    linhas.append("Feliz Natal!!!".center(width))

    return linhas

def piscar():
    if not rodando:
        return

    arvore = gerar_arvore()
    texto_final = ""

    for linha in arvore:
        texto_final += linha + "\n"

    label_arvore.configure(text=texto_final,text_color=random.choice(cores))

    app.after(500, piscar)

def iniciar():
    global rodando
    if not rodando:
        rodando = True
        piscar()

def parar():
    global rodando
    rodando = False


frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10)

btn_iniciar = ctk.CTkButton(frame_botoes,text="▶ Iniciar",command=iniciar,width=120)
btn_iniciar.grid(row=0, column=0, padx=10)

btn_parar = ctk.CTkButton(frame_botoes,text="⏸ Parar",command=parar,width=120)
btn_parar.grid(row=0, column=1, padx=10)

app.mainloop()
