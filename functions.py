from time import sleep
from rich import print
from classe import *
from os import system

# Variáveis da classe
clientes = []


# Cadastrar cliente
def cadastrar(nome, idade):
    novo_cliente = User(nome, idade)
    clientes.append(novo_cliente)


# Excluir cliente
def excluir_cliente():
    exibir_clientes_cadastrados()
    nome = input('Qual nome do cliente que deseja remover? ')
    for cliente in clientes:
        if cliente.nome == nome:
            clientes.remove(cliente)
    print(f'[green] cliente {nome} removido com sucesso!![/]')
    exibir_clientes_cadastrados()


def editar_cliente():
    exibir_clientes_cadastrados()
    nome = input('Qual nome do cliente que deseja editar? ')
    novo_nome = input('Qual o novo nome?')
    for cliente in clientes:
        if cliente.nome == nome:
            cliente.nome = novo_nome
    print(f'[green] cliente {nome} editado com sucesso!![/]')
    exibir_clientes_cadastrados()


# Menu cadastro
def menu_cadastro():
    head_clientes_cadastrados()
    nome = input('Qual o nome do cliente: ')
    idade = input('Qual a idade do cliente: ')
    cadastrar(nome, idade)
    print(f' USER ID: {len(clientes)}\n NOME: {nome}\n IDADE: {idade}\n')
    print('[green]Cadastrado com sucesso![/]')
    sleep(3)
    system('cls')


# Consulta de usuário
def menu_consulta():
    head_clientes_cadastrados()
    for cliente in clientes:
        print(f'nome: {cliente.nome}\nidade: {cliente.idade}')


# Menu de buscas de clientes
def show_menu_cliente():
    head_menu_buscar()
    print('''
    [1] Buscar por nome
    [2] Buscar por idade
    [3] Buscar todos os clientes
    [0] Voltar para  o inicio.     
    ''')
    option2 = input('digite sua opção: ')
    if option2 == '1':
        sub_menu_buscar_cliente_nome()
    elif option2 == '2':
        sub_menu_buscar_cliente_idade()
    elif option2 == '0':
        pass
    elif option2 == '3':
        menu_consulta()

    return option2


# Buscar cliente por idade
def clientes_idade(idade):
    clientes_encontrados = []
    for cliente in clientes:
        if cliente.idade == idade:
            clientes_encontrados.append(cliente)
    print('Clientes encontrados:\n')
    for cliente in clientes_encontrados:
        print(f'{cliente.nome}\n')


# Buscar cliente por nome
def cliente_nome(nome):
    clientes_encontrados = []
    for cliente in clientes:
        if cliente.nome == nome:
            clientes_encontrados.append(cliente)
    print('Clientes encontrados:\n')
    for cliente in clientes_encontrados:
        print(f'nome: {cliente.nome} ', end='-> ')
        print(f'idade: {cliente.idade} anos ')


# Criar menu de opções
def show_menu():
    head_sistema_login()
    print('''
[1] Cadastrar novo cliente
[2] Menu de busca
[3] Menu de edição
[0] [red]Sair...[/]
''')
    option = input('digite sua opção:')
    return option


# Sub menu buscar cliente idades
def sub_menu_buscar_cliente_idade():
    idade = ''
    while not idade.isnumeric():

        idade = input('Digite a idade para fazer uma busca: ')
        if idade.isnumeric():
            clientes_idade(idade)
        else:
            print('[red]Idade inválida!![/]')


# Sub menu Buscar cliente por nome
def sub_menu_buscar_cliente_nome():
    system('cls')
    nome = ''
    while not nome.isalpha():
        nome = input('Digite o nome para fazer uma busca: ')
        if nome.isalpha():
            cliente_nome(nome)
        else:
            print('[red]Nome inválido!![/]')


# Menu sair
def menu_sair():
    system('cls')
    print('[bold]saindo do sistema... até logo!![/]')
    sleep(2)
    system('cls')


def menu_edit_cadastro():
    system('cls')
    print('''
        [green][bold]Menu de edição:[/][/]
     [1] Excluir cadastro por nome
     [2] Editar cadastro
     [3] Média clientes
     [4] Ordem letra
     [5] Ordem Nome
     [6] Total idades
     [0] Voltar para  o inicio.     
     ''')

    option = input('digite sua opção: ')

    if option == '1':
        excluir_cliente()
    if option == '2':
        editar_cliente()
    if option == '3':
        cliente_media()
    if option == '4':
        ordem_letra()
    if option == '5':
        ordem_idade()
    if option == '6':
        total_idade()


# Exibi clientes cadastrados no banco
def exibir_clientes_cadastrados():
    system('cls')
    head_clientes_cadastrados()
    for cliente in clientes:
        print()
        print(f'nome: {cliente.nome}\nidade: {cliente.idade}\n')


# Média clientes
def cliente_media():
    total_idades = 0
    media = total_idades / len(clientes)
    for cliente in clientes:
        total_idades += cliente.idade
    print(f'A média de idades entre clientes é {media}')


def ordem_letra():
    total_nomes = []
    total_nomes.sort()
    for cliente in clientes:
        total_nomes.append(cliente.nome)
    print(total_nomes)


def ordem_idade():
    total_idades = []
    total_idades.sort()
    for cliente in clientes:
        total_idades += cliente.idade
    print(total_idades)


def total_idade():
    total_idades = 0
    for cliente in clientes:
        total_idades += cliente.idade
    print(total_idades)


# Cabeçalhos

def head_clientes_cadastrados():
    system('cls')
    print('[green]-----[/]' * 10)
    print()
    texto = 'CLIENTES CADASTRADOS'
    space = '               '  # numero de letras + 5
    print(f'[bold]{space}{texto}\n[/] ')
    print('[green]-----[/]' * 10)
    print()


def head_sistema_login():
    system('cls')
    print('[green]-----[/]' * 10)
    print()
    texto = 'SISTEMA DE LOGIN'
    space = '                   '  # numero de letras + 5
    print(f'[bold]{space}{texto}\n[/] ')
    print('[green]-----[/]' * 10)
    print()


def head_cadastro_cliente():
    system('cls')
    print('[green]-----[/]' * 10)
    print()
    texto = 'CADASTRO DE CLIENTES'
    space = '                   '  # numero de letras + 5
    print(f'[bold]{space}{texto}\n[/] ')
    print('[green]-----[/]' * 10)
    print()


def head_menu_buscar():
    system('cls')
    print('[green]-----[/]' * 10)
    print()
    texto = 'MENU BUSCAR CLIENTES'
    space = '                '  # numero de letras + 5
    print(f'[bold]{space}{texto}\n[/] ')
    print('[green]-----[/]' * 10)
    print()
