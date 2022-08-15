import back_tom
from PySimpleGUI import *

theme('DarkTeal4')

def criartxt(pasta, tom) -> bool:
    """
    Recebe a pasta que será salva e cria um .txt com as informações do tom
    """
    texto = []
    escala = back_tom.Escala(tom)
    texto.append(imp_notas(escala.escalaDoTom()))
    texto.append(imp_notas(escala.escalaMaior()))
    texto.append(imp_notas(escala.menorNatural()))
    texto.append(imp_notas(escala.menorMelodica()))
    texto.append(imp_notas(escala.menorHarmonica()))

    txt = ''
    for i in texto:
        if i == texto[-1]:
            txt = txt + f'{i}'
        else:
            txt = txt + f'{i}\n'
    try:
        file = open(f"{pasta}/Escalas.txt", "x")
        file.write(txt)
        return True
    except FileExistsError:
        file = open(f'{pasta}/Escalas.txt', "w")
        file.write(txt)
        return True

def relatorio(tom):
    """
    Janela para o usiário escolher a pasta para salvar o relatório
    """
    lt = [
        [Text(f'_'*300)],
        [Text('Selecione sua pasta:'), InputText(key = 'TargetFolder'), FolderBrowse('Pesquisar')],
        [Submit(), Exit()]
        ]
    wr = Window('Gerar Relatório', layout=lt, size=(600,100))
    evento, dados = wr.read()
    while True:
        if evento == 'Exit' or evento == WIN_CLOSED:
            wr.close()
            break
        elif evento == 'Submit':
            if len(dados['TargetFolder']) > 0:
                criartxt(dados['TargetFolder'],tom)
                popup('Relatório criado com sucesso!')
                wr.close()
                break
            else:
                popup('Escolha uma pasta!')
                wr.close()
                break

def imp_notas(x):
    '''
    Transforma a lista numa string com a sequência de notas
    '''
    txt = ''
    for i in x:
        if i == x[-1]:
            txt = txt + f'{i}'
        else:
            txt = txt + f'{i} - '
    return txt

def escala():
    """
    Função para criar a janela que encontra as escalas
    """

    cromatica_txt = [[Text(' ', k='escala_crom')]]
    crom_fr = [ [Frame('Cromática',cromatica_txt, s=(350,45))]]

    maior_txt = [[Text(' ', k='escalaMaior')]]
    maior_fr = [ [Frame('Maior',maior_txt, s=(350,45))]]

    menorN_txt = [[Text(' ', k='escalaMenorN')]]
    menorN_fr = [ [Frame('Menor Natural',menorN_txt, s=(350,45))]]

    menorM_txt = [[Text(' ', k='escalaMenorM')]]
    menorM_fr = [ [Frame('Menor Melódica',menorM_txt, s=(350,45))]]

    menorH_txt = [[Text(' ', k='escalaMenorH')]]
    menorH_fr = [ [Frame('Menor Harmonica',menorH_txt, s=(350,45))]]



    layout = [
        [Text('Tom: '), Input(s=(2,1),k='tom'),Button('Ok', s=(3,1)), Text('',k='aviso')],
        [crom_fr],
        [maior_fr],
        [menorN_fr],
        [menorM_fr],
        [menorH_fr],
        [Button('Exportar', s=(6,1)), Button('Sair',s=(3,1))]
    ]
    w_esc = Window('Escalas', layout, size=(400,350))
    while True:
        try:
            evento, dados = w_esc.read()
            if evento == 'Ok':
                dados['tom'] = dados['tom'].upper()
                crom = w_esc.find_element('escala_crom')
                esc_crom_txt = imp_notas(back_tom.Escala(dados['tom']).escalaDoTom())
                crom.update(esc_crom_txt, font='Arial 11 bold')

                maior = w_esc.find_element('escalaMaior')
                esc_maior_txt = imp_notas(back_tom.Escala(dados['tom']).escalaMaior())
                maior.update(esc_maior_txt, font='Arial 11 bold')

                menorN = w_esc.find_element('escalaMenorN')
                esc_menorN_txt = imp_notas(back_tom.Escala(dados['tom']).menorNatural())
                menorN.update(esc_menorN_txt, font='Arial 11 bold')

                menorM = w_esc.find_element('escalaMenorM')
                esc_menorM_txt = imp_notas(back_tom.Escala(dados['tom']).menorMelodica())
                menorM.update(esc_menorM_txt, font='Arial 11 bold')

                menorH = w_esc.find_element('escalaMenorH')
                esc_menorH_txt = imp_notas(back_tom.Escala(dados['tom']).menorHarmonica())
                menorH.update(esc_menorH_txt, font='Arial 11 bold')
            
                w = w_esc.find_element('aviso') 
                w.update('')
                w_esc.refresh()
            if evento == 'Exportar':
                relatorio(dados['tom'].upper())
    
            if evento == WIN_CLOSED or evento == 'Sair':
                w_esc.close()
                break
        except ValueError:
            crom = w_esc.find_element('escala_crom')
            crom.update(f'-='*20)

            maior = w_esc.find_element('escalaMaior')
            maior.update(f'-='*20)

            menorN = w_esc.find_element('escalaMenorN')
            menorN.update(f'-='*20)

            menorM = w_esc.find_element('escalaMenorM')
            menorM.update(f'-='*20)

            menorH = w_esc.find_element('escalaMenorH')
            menorH.update(f'-='*20)

            w = w_esc.find_element('aviso')
            w.update('Digite uma nota musical válida!')
            tom = w_esc.find_element('tom')
            tom.update('')
            w_esc.refresh()
            pass

def cmHarmonico():
    '''
    Função que Cria a janela para a escolha do Campo Harmonico
    '''
    x = ''
    campo_txt = [[Text('', k='txt_campo',font='Arial 10 italic',auto_size_text=True)],]
    campo_fr = [Frame(f'Campo Harmonico {x}',campo_txt, k='fr_campo')]

    campos = ['Maior', 'Menor Natural', 'Menor Harmonico', 'Menor Melódico']

    layout = [
        [Text('Tom: '), Input(s=(2,1),k='tom'), Combo(campos,'Campo Harmonico', enable_events=True, readonly=True, k='campo')],
        [campo_fr],
        [Button('Ok', s=(4,1)), Text('',k='aviso')],
        [Button('Sair',s=(4,1))]
    ]
    w_cm = Window('Campos Harmônicos',layout, size=(320,150))
    while True:
        evento, dados = w_cm.read()
        if evento == 'Ok':
            fr = w_cm.find_element('fr_campo')
            fr.update(f'Campo Harmonico {dados["campo"]}')
            if dados['tom'] != '':
                if dados['campo'] == 'Maior':
                    nota = back_tom.CampoHarmonico(dados['tom'].upper())
                    txt = w_cm.find_element('txt_campo')
                    txt.update(imp_notas(nota.campoMaior()))
                elif dados['campo'] == 'Menor Natural':
                    nota = back_tom.CampoHarmonico(dados['tom'].upper())
                    txt = w_cm.find_element('txt_campo')
                    txt.update(imp_notas(nota.campoMenorNatural()))
                elif dados['campo'] == 'Menor Harmonico':
                    nota = back_tom.CampoHarmonico(dados['tom'].upper())
                    txt = w_cm.find_element('txt_campo')
                    txt.update(imp_notas(nota.campoMenorHarmonico()))
                elif dados['campo'] == 'Menor Melódico':
                    nota = back_tom.CampoHarmonico(dados['tom'].upper())
                    txt = w_cm.find_element('txt_campo')
                    txt.update(imp_notas(nota.campoMenorMelodico()))
            else:
                aviso = w_cm.find_element('aviso')
                aviso.update('Digite um tom!')
                w_cm.refresh()
        
        elif evento == WIN_CLOSED or evento == 'Sair':
            w_cm.close()
            break


if __name__ == '__main__':
        cmHarmonico()