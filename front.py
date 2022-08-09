import PySimpleGUI as ps
from back import Escala, CampoHarmonico


while True:
    try:
        tom = input('Escolha um tom: ')
        escala = Escala(tom)
        campo = CampoHarmonico(tom)
        break
    except ValueError:
        print('Digite um tom válido')

print()
print(escala.menorMelodica())
print(campo.campoMaior())
print()