from rich import print
from os import system
from classe import User
from time import sleep
from functions import *

while True:
    options = show_menu()
    if options.isnumeric():
        if options == "0":  # Sair
            menu_sair()
            break
        elif options == "1":  # Cadastrar novo cliente
            menu_cadastro()
        elif options == '2':
            show_menu_cliente()
        elif options == '3':
            menu_edit_cadastro()



    else:
        print('[red] OPÇÃO INVÁLIDA!!![/]')

    if input('Deseja continuar [s]im [n]ao: ') == 'n':
        system('cls')
        break
    system('cls')
