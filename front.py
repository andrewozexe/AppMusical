import PySimpleGUI as sg
import commands as cm

sg.theme("DarkTeal4")

def myApp():
    layout = [
    [sg.Text('      AppMusical!  ')],
    [sg.Button('Escala', s=(14,1)), sg.Text()], 
    [sg.Button('Campo Harmonico',s=(14,1))],
    [sg.Button('Sair',s=(14,1))]
    ]
    w1 = sg.Window(title='Me de o Tom', layout=layout, size=(150,180))
    while True:
        evento, dados = w1.read()
        if evento == 'Escala':
            cm.escala()
        elif evento == 'Campo Harmonico':
            cm.cmHarmonico()

        elif evento == sg.WIN_CLOSED or evento == 'Sair':
            break
myApp()