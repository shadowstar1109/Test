#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
#Modulos
from time import sleep
from sys import stdout, exit
import multiprocessing
from wget import download
from urllib import urlopen
from platform import system as systemos, architecture
from os import system, path
#   Echo por: Shadow Town
#   Version: 1.0
#Colores
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
#Funciones
def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False:
    print '''
    
███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃   No Estas Conectado a Una Red.
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤... '''.format(GREEN, END)
     exit(0)
