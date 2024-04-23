import sqlite3
import PySimpleGUI as sg

# Função que vai criar a tabela de usuários no banco de dados
def criar_tabela_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        usuario TEXT,
                        senha TEXT
                      )''')
    conn.commit()
    conn.close()
def inserir_usuario(usuario,senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', (usuario, senha))
    conn.commit()
    conn.close()
inserir_usuario('gabriel', '12345')


layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
]

# Criar a janela 
window = sg.Window('Login', layout=layout)

# Criar a tabela de usuários
criar_tabela_usuarios()

#  eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'login': 
        usuario = values['usuario']
        senha = values['senha']
        # Verificar se o usuário e senha correspondem aos registros no banco de dados
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE usuario=? AND senha=?', (usuario, senha))
        if cursor.fetchone():
            window['mensagem'].update('Login bem-sucedido!')
        else:
            window['mensagem'].update('Usuário ou senha incorretos!')
        conn.close()

window.close()
