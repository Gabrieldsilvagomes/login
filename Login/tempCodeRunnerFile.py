import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]


#criando janela

sg.window = sg.window('Login',layout=layout)

#lendo os eventos

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break