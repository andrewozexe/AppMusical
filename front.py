import PySimpleGUI as sg
import commands as cm

sg.theme("DarkTeal4")

def myApp():
    coluna_1 = [
        [sg.Text('Me de o Tom', font='Arial 12 bold')],
        [sg.Text('Bem vindo(a) ao AppMusical,\nvamos te ajudar a achar escalas\ne campos harmonicos!\nClique em uma opção!')]
    ]
    
    coluna_2 = [
    [sg.Button('Escala', s=(14,1))], 
    [sg.Button('Campo Harmonico',s=(14,1))],
    [sg.Button('Sair',s=(14,1))]
    ]

    frame_1 = [[sg.Frame('AppMusical', coluna_1)]]
    frame_2 = [[sg.Frame('Opções', coluna_2, element_justification='center')]]
    
    layout = [[sg.Column(frame_1 ),sg.Column(frame_2)],
    []
    
    ]
    w1 = sg.Window(title='Me de o Tom', layout=layout, size=(400,180),auto_size_buttons=True)
    while True:
        evento, dados = w1.read()
        if evento == 'Escala':
            cm.escala()
        elif evento == 'Campo Harmonico':
            cm.cmHarmonico()
        elif evento == sg.WIN_CLOSED or evento == 'Sair':
            break

myApp()