class Escala:
    def __init__(self, tom:str) -> None:
        tom = tom.upper()
        self.CROM = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
                    # 0   1    2   3    4   5   6    7    8   9   10   11 
        if tom in self.CROM:
            self.tom = tom   
        self.grau = self.CROM.index(tom)
        self.escalaTom = []
        self.__intevalos = {
            'Maior':    [0,2,4,5,7,9,11],
            'Natural':  [0,2,3,5,7,8,10], 
            'Harmonica':[0,2,3,5,7,8,11], 
            'Melodica': [0,2,3,5,7,9,11]
        }
    def escalaDoTom(self):
        while len(self.escalaTom) != 12:
            if self.grau == 11:
                self.escalaTom.append(self.CROM[self.grau])
                self.grau = 0
            else:
                self.escalaTom.append(self.CROM[self.grau])
                self.grau += 1
        return self.escalaTom
    def escalaMaior(self):
        escalaMaior = []
        for j in self.__intevalos['Maior']:
            escalaMaior.append(self.escalaDoTom()[j])
        return escalaMaior
    def menorNatural(self):
        menorNatural = []
        for i in self.__intevalos['Natural']:
            menorNatural.append(self.escalaDoTom()[i])
        return menorNatural
    def menorHarmonica(self):
        menorHarmonica = []
        for i in self.__intevalos['Harmonica']:
            menorHarmonica.append(self.escalaDoTom()[i])
        return menorHarmonica
    def menorMelodica(self):
        menorMelodica = []
        for i in self.__intevalos['Melodica']:
            menorMelodica.append(self.escalaDoTom()[i])
        return menorMelodica

class CampoHarmonico(Escala):
    def __init__(self, tom: str) -> None:
        super().__init__(tom)
        self.campo = {
            'Maior' :     ['','m','m','','','m','°'],
            'Natural' :   ['m7', '°','','m','m','',''],
            'Harmonico' : ['m7M', '°','7M(#5)','m7','7','7M','°'],
            'Melodico' :  ['m7M', 'm7','7M(#5)','7','7','°','°']
        }
    def campoMaior(self):
        campoMaior = []
        for i,j in zip(self.escalaMaior(),self.campo['Maior']):
            campoMaior.append(i+j)
        return campoMaior
    def campoMenorNatural(self):
        menorNatural = []
        for i,j in zip(self.menorNatural(),self.campo['Natural']):
            menorNatural.append(i+j)
        return menorNatural
    def campoMenorHarmonico(self):
        menorHarmonico = []
        for i,j in zip(self.menorHarmonica(),self.campo['Harmonico']):
            menorHarmonico.append(i+j)
        return menorHarmonico
    def campoMenorMelodico(self):
        menorMelodico = []
        for i,j in zip(self.menorMelodica(),self.campo['Melodico']):
            menorMelodico.append(i+j)
        return menorMelodico


class ModosGregos(Escala):
    def __init__(self, tom: str) -> None:
        super().__init__(tom)

class Acorde(Escala):
    def __init__(self, tom: str) -> None:
        super().__init__(tom)


if __name__ == '__main__':
    pass