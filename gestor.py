#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from random import choice
from time import strftime as time
import os, time
import string # para selecionar os caracteres da senha
import pyperclip as pc #https://pypi.org/project/pyperclip/

__title__ = 'gestor-linux'
__version__ = '0.1'
__author__ = 'Vitor Amorim'
__license__ = 'MIT 2020'
__copyright__ = 'Copyright 2020 Vitor Amorim'

cor = '#3803FA'

root = Tk()
root.title(" Gestor Pessoal de Configurações ")
root.geometry("500x500")
#root.configure(bg=cor)
root.resizable(False, False)
#root.iconbitmap(r': icon.ico')

''' FUNÇÔES e VARIAVEIS para uso interno '''

escala = IntVar()

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
    print('senha criada\t' + senha)
    messagebox.showinfo("Senha Gerada", 'senha copiada!!')

'''def atualizar_repos(): #Atualizar Repositorios mais velozes
    sim_s = (sim).get()
    nao_n = (nao).get()
 
    if sim_s == True and nao_n == False:
        
    elif nao_n == True and sim_s == False:
        messagebox.showinfo("!", 'Aguarde alguns segundos ..')
        os.system('pacman-mirrors --country Brazil')
        messagebox.showinfo("!", 'Repositorios Atualizados')
        print('\nRepositorios Atualizados!')
    else:
        messagebox.showwarning("warning","Muitas opções ativas")
        print('\nmais de uma opção ativa')
'''
def setar_hora_manjaro():
    try:
        os.system('timedatectl set-ntp true')
        os.system('timedatectl set-timezone America/Sao_Paulo')
    except Exception:
        os.system('pacman -S ntp')
        return setar_hora_manjaro()
    finally:
        print('\nData e Hora Configurados com sucesso!')

def rmv_blk_arch(): #remover block do pacman
    os.system('rm -rf /var/lib/pacman/db.lck')
    print('\ndb.lck removido!')
    messagebox.showwarning("warning","Trava removida! ")

def rmv_blk_debian(): #remover block do apt-get
    os.system('rm -rf /var/lib/apt/lists/lock')
    print('\nlock removido!')
    messagebox.showwarning("warning","Trava removida! ")

def sair(): # fechar janela
    root.destroy()

def thunar(): # abrir diretorio dos Scripts
    os.system('thunar Scripts/')

def sobre(): # botao sobre do menu
    #messagebox para botoes instantaneos https://www.javatpoint.com/python-tkinter-messagebox
    messagebox.showinfo("Sobre","vhartzamorimg2@gmail.com")

def configurar_zsh(): # instalar e configurar o oh-my-zsh https://github.com/ohmyzsh/ohmyzsh
    try:
        os.system('pacman -S zsh zsh-autosuggestion')
        os.system('sudo sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"')
        os.system('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
        os.system('git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions')
        os.system('')
        os.system('cp Scripts/.zshrc ~/')
        os.system('source ~/.zshrc')
    except Exception:
        os.system('pacman -S wget git')
        return configurar_zsh()
    finally:
        print('\nInstalado e Configurado com Sucesso')

def pacotes_basicos():
    os.system('pacman-mirrors --country Brazil')
    os.system('pacman -Sy && pacman -S htop speedtest-cli cmatrix git wget curl trizen vim ranger')
    print('\tpacotes basicos instalados!')

def pacotes_audio():
    os.system('pacman -S pulseaudio pavucontrol')

'''
def pacotes_e_config_i3wm():
    os.system('pacman -S rofi nitrogen compton ranger pcmanfm')
    #os.system('cp /Scripts/i3.confjdhask ~/.config/i3/ .....')        
'''
        
def janela_decisão_resolução():
    '''Opçoes da janela'''
    def s():
        os.system('./Scripts/resolução.sh')
        os.system('cp Scripts/.resolução.sh ~/')
        os.system('echo "exec ~/.resolução.sh" >> ~/.xinitrc')
        messagebox.showwarning("warning","Setado no .xinitrc")
        print('\nresolução configurada na inicialização com sucesso')
        top.destroy()
    def n():
        os.system('./Scripts/.resolução.sh')
        messagebox.showwarning("warning","Resolução setada")
        print('\nresolução acertada')
        top.destroy()

    top = Toplevel(root)
    top.geometry("180x90")
    bt_s = Button(top, text='Sim', command = s).place(x = 10, y= 10)
    bt_n = Button(top, text='Não', command = n).place(x = 100, y= 10)
    copiar_xinit = Label(top, text='Setar .xinitrc ?', font='bold').place(x = 10, y=60)
    top.mainloop()  

def janela_decisão_repositorios():
    '''Opçoes da janela'''
    def s():
        t = time.ctime()
        messagebox.showinfo("!", 'Aguarde alguns segundos ..')
        os.mkdir('log')
        os.system('pacman-mirrors --country Brazil > log/log_repositorios.txt')
        messagebox.showinfo("!", 'Repositorios Atualizados, log salvo')
        print('\nRepositorios Atualizados , log salvo\t', t)
        top.destroy()
        
    def n():
        t = time.ctime()
        os.system('pacman-mirrors --country Brazil')
        messagebox.showinfo("!", 'Repositorios Atualizados')
        print('\nRepositorios Atualizados\t', t)
        top.destroy()        

    top = Toplevel(root)
    top.geometry("180x90")
    bt_s = Button(top, text='Sim', command = s).place(x = 10, y= 10)
    bt_n = Button(top, text='Não', command = n).place(x = 100, y= 10)
    copiar_xinit = Label(top, text='Gerar log?', font='bold').place(x = 10, y = 60)
    top.mainloop()  

# menu e itens do menu
menu_bar = Menu(root, font='bold')
menu_principal = Menu(menu_bar, tearoff=0, font='bold')
menu_principal.add_command(label='Backup')
menu_principal.add_command(label='Abrir diretorio dos Scripts', command = thunar)
menu_principal.add_command(label='Sobre', command = sobre)
menu_principal.add_separator()
menu_principal.add_command(label='Sair', command = sair)
menu_bar.add_cascade(label='Menu', menu=menu_principal)
root.config(menu=menu_bar)

botao_gerador = Button(root, text='Gerador de Senha', command = gerado_senha).place(x = 10, y = 20)

tamanho_senha = Label(root, text='Tamanho da Senha ', font='bold').place(x = 170, y = 22)

opçao_gerador = Scale(
                     root, variable=escala , from_ = 4, to = 9, orient = HORIZONTAL
                     ).place(x= 350, y = 15)

boao_atualizar_repos = Button(
                             root, text='Atualizar Repositorios', command = janela_decisão_repositorios
                             ).place(x = 10, y = 60)

rmv_arch_btn = Button(root, text='Remover block Pacman', command = rmv_blk_arch).place(x = 10, y = 100)

rmv_deb_btn = Button(root, text='Remover block APT-GET', command = rmv_blk_debian).place(x = 250, y = 100)

setar_hora = Button(root, text='Acertar Hora no Manjaro', command = setar_hora_manjaro).place(x = 10, y = 150)

setar_resolução_btn = Button(root, text='Setar Resolução ', command = janela_decisão_resolução).place(x = 10, y = 180)

root.mainloop()