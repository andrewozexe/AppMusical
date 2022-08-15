
from multiprocessing.sharedctypes import Value
import back_tom
from PySimpleGUI import *

theme('DarkTeal4')

def imp_escala(x):
    txt = ''
    for i in x:
        if i == x[-1]:
            txt = txt + f'{i}'
        else:
            txt = txt + f'{i} - '
    return txt

def escala():
    layout = [
        [Text('Tom: '), Input(s=(2,1),k='tom'),Button('Ok', s=(3,1)), Text('',k='aviso')],
        [Text('Cromatica: ', k='escala_crom')],
        [Text('Maior: ', k='escalaMaior')],
        [Text('Menor Natural: ', k='escalaMenorN')],
        [Text('Menor Melodica: ', k='escalaMenorM')],
        [Text('Menor Harmonica: ', k='escalaMenorH')],
        [ Button('Sair',s=(3,1))]
    ]
    w_esc = Window('Escalas', layout, size=(400,200))
    while True:
        try:
            evento, dados = w_esc.read()
            if evento == 'Ok':
                dados['tom'] = dados['tom'].upper()
                crom = w_esc.find_element('escala_crom')
                esc_crom_txt = imp_escala(back_tom.Escala(dados['tom']).escalaDoTom())
                crom.update(f'Cromatica: {esc_crom_txt}')

                maior = w_esc.find_element('escalaMaior')
                esc_maior_txt = imp_escala(back_tom.Escala(dados['tom']).escalaMaior())
                maior.update(f'Maior: {esc_maior_txt}')

                menorN = w_esc.find_element('escalaMenorN')
                esc_menorN_txt = imp_escala(back_tom.Escala(dados['tom']).menorNatural())
                menorN.update(f'Menor Natural: {esc_menorN_txt}')

                menorM = w_esc.find_element('escalaMenorM')
                esc_menorM_txt = imp_escala(back_tom.Escala(dados['tom']).menorMelodica())
                menorM.update(f'Menor Melodica: {esc_menorM_txt}')

                menorH = w_esc.find_element('escalaMenorH')
                esc_menorH_txt = imp_escala(back_tom.Escala(dados['tom']).menorHarmonica())
                menorH.update(f'Menor Harmonica: {esc_menorH_txt}')
                
                tom = w_esc.find_element('tom')
                tom.update('')
                w = w_esc.find_element('aviso')
                w.update('')
                w_esc.refresh()
    
            if evento == WIN_CLOSED or evento == 'Sair':
                w_esc.close()
                break
        except ValueError:
            crom = w_esc.find_element('escala_crom')
            crom.update(f'Cromatica: ')

            maior = w_esc.find_element('escalaMaior')
            maior.update(f'Maior:')

            menorN = w_esc.find_element('escalaMenorN')
            menorN.update(f'Menor Natural: ')

            menorM = w_esc.find_element('escalaMenorM')
            menorM.update(f'Menor Melodica:')

            menorH = w_esc.find_element('escalaMenorH')
            menorH.update(f'Menor Harmonica:')

            w = w_esc.find_element('aviso')
            w.update('Digite uma nota musical válida!')
            tom = w_esc.find_element('tom')
            tom.update('')
            w_esc.refresh()
            pass

def cmHarmonico():
    pass


if __name__ == '__main__':
    escala()