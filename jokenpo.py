import PySimpleGUI as sg
from utilities import resultado

sg.theme('Topanga')

def windowStart():
    layout = [
        [sg.Text('Digite seu nome')],
        [sg.Input(key='usuario')],
        [sg.Button('Continuar'), sg.Button('Sair')]
    ]

    return sg.Window('Start Game',layout,finalize=True)

def windowGame(usuario):
    layout = [
        [sg.Text(f'Faça sua joganda {usuario}!')],
        [sg.Button('Pedra'), sg.Button('Papel'), sg.Button('Tesoura')],
        [sg.Text(key='resultado')]
    ]

    return sg.Window('Jokenpô',layout,finalize=True)

windowStart_, windowGame_ = windowStart(), None

def main():
    while True:
        window, event, values = sg.read_all_windows()
        if event in ['Sair', sg.WIN_CLOSED]:
            break
        elif window == windowStart_:
            if event == 'Continuar':
                if values['usuario']:
                    windowStart_.close()
                    windowGame_ = windowGame(values['usuario'])
                else:
                    sg.popup('Por favor. Digite seu nome!')
                    
        elif window == windowGame_:
            if event in ['Pedra','Papel','Tesoura']:
                resultado_, color = resultado(event)
                window['resultado'].update(resultado_, font=('',12), text_color=color)

if __name__ == '__main__':
    main()