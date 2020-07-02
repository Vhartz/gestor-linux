#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from random import choice
from time import strftime as time
import os, subprocess
import string
import pyperclip as pc #https://pypi.org/project/pyperclip/

root = Tk()
root.title(" Gestor Pessoal de Configurações ")
root.geometry("500x500")
root.configure(bg='#3803FA')
root.resizable(False, False)
#root.wm_iconbitmap('/icon.ico')

#variaveis para uso interno
sim = IntVar()
nao = IntVar()
escala = IntVar()

''' FUNÇÔES '''

def gerado_senha(): #gerador de senha
    escala_copia = (escala).get()
    tamanho = escala_copia
    letras = string.ascii_lowercase
    numeros = string.digits
    senha = ''
    for i in range(tamanho):
      senha += choice(letras + numeros)
    messagebox.showinfo("Senha Gerada", senha)
    pc.copy(senha)
    messagebox.showinfo("Senha Gerada", 'senha copiada!!')

def atualizar_repos(): #Atualizar Repositorios mais velozes
    sim_s = (sim).get()
    nao_n = (nao).get()

    if sim_s == True and nao_n == False:
        messagebox.showinfo("!", 'Aguarde alguns segundos ..')
        os.system('pacman-mirrors --country Brazil > log_repos.txt')
        messagebox.showinfo("!", 'Repositorios Atualizados, log salvo')
    elif nao_n == True and sim_s == False:
        messagebox.showinfo("!", 'Aguarde alguns segundos ..')
        os.system('pacman-mirrors --country Brazil')
        messagebox.showinfo("!", 'Repositorios Atualizados')
    else:
        messagebox.showwarning("warning","Muitas opções ativas")

def rmv_blk_arch(): #remover block do pcman no manjaro
    os.system('rm -rf /var/lib/pacman/db.lck')
    messagebox.showwarning("warning","Trava removida! ")

def rmv_blk_debian():
    os.system('rm -f /var/lib/apt/lists/lock')
    messagebox.showwarning("warning","Trava removida! ")

def sair(): # fechar janela
    root.destroy()

def thunar(): # mostrar diretorio dos Scripts
    os.system('thunar /home/$USER')

def sobre():
    #messagebox para botoes instantaneos https://www.javatpoint.com/python-tkinter-messagebox
    messagebox.showinfo("Sobre","vhartzamorimg2@gmail.com")

# menu itens do menu
menu_bar = Menu(root, font='bold')
menu_principal = Menu(menu_bar, tearoff=0, font='bold')
menu_principal.add_command(label='Backup')
menu_principal.add_command(label='Abrir diretorio dos Scripts', command=thunar)
menu_principal.add_command(label='Sobre', command=sobre)
menu_principal.add_separator()
menu_principal.add_command(label='Sair', command=sair)
menu_bar.add_cascade(label='Menu', menu=menu_principal)
root.config(menu=menu_bar)

botao_gerador = Button(root, text='Gerador de Senha', command=gerado_senha).place(x=10, y=20)
tamanho_senha = Label(root, text='Tamanho da Senha ', font='bold', bg='#3803FA').place(x=170, y=22)
opçao_gerador = Scale(root, variable=escala , from_ = 4, to = 9, orient = HORIZONTAL, bg='#3803FA').place(x=350, y=15)

#geração de log na atualizar_repos
boao_atualizar_repos = Button(root, text='Atualizar Repositorios', command=atualizar_repos).place(x=10,y=60)
gerar_log = Label(root, text='Gerar log?', font='bold', bg='#3803FA').place(x=180, y=64)

sim_log = Checkbutton(root, text='Sim', bg='#3803FA', font='bold', variable=sim,
                        onvalue = 1, offvalue = 0, activebackground='#3803FA').place(x=280, y=64)

nao_log = Checkbutton(root, text='Não', bg='#3803FA', font='bold', variable=nao,
                        onvalue = 1, offvalue = 0, activebackground='#3803FA').place(x=380, y=64)

rmv_arch_btn = Button(root, text='Remover block arch e manjaro', command=rmv_blk_arch).place(x=10, y=100)
rmv_deb_btn = Button(root, text='Remover block debian e ubuntu', command=rmv_blk_debian).place(x=250, y=100)

root.mainloop()
