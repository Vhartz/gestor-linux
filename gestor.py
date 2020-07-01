#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from random import choice
import string
import pyperclip #https://pypi.org/project/pyperclip/

root = Tk()
root.title(" Sett Configs ")
root.geometry("500x500")
root.configure(bg='#3803FA')
root.resizable(False, False)
# gerador de senhas
def gerado_senha():
    tamanho = 8
    letras = string.ascii_lowercase
    numeros = string.digits
    senha = ''
    for i in range(tamanho):
      senha += choice(letras + numeros)
    messagebox.showinfo("Senha Gerada", senha)
    pyperclip.copy(senha)
    messagebox.showinfo("Senha Gerada", 'senha copiada!!')

def sair():
    root.destroy()

def sobre():
    #messagebox para botoes instantanios https://www.javatpoint.com/python-tkinter-messagebox
    messagebox.showinfo("Sobre","vhartzamorimg2@gmail.com")

# menu itens do menu
menu_bar = Menu(root, font='bold')
menu_principal = Menu(menu_bar, tearoff=0, font='bold')
menu_principal.add_command(label='Backup')
menu_principal.add_command(label='Abrir diretorio dos Scripts')
menu_principal.add_command(label='Sobre', command=sobre)
menu_principal.add_separator()
menu_principal.add_command(label='Sair', command=sair)
#menu da barra em cascata
menu_bar.add_cascade(label='Menu', menu=menu_principal)
root.config(menu=menu_bar)

botao_gerador = Button(root, text='Gerador de Senha', command=gerado_senha).place(x=10, y=20)


root.mainloop()
