from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado
from mundo_pc.Monitor import Monitor

class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @staticmethod
    def contar():
        Computadora.contador_computadoras = Computadora.contador_computadoras + 1
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'''
        {self.nombre}: {self._id_computadora}
            Monitor: {self._monitor}
            Teclado: {self._teclado}
            Raton:   {self._raton}
        
        '''

if __name__ == '__main__':
    teclado1= Teclado('USB', 'Dell')
    raton1 = Raton('Bluetooth', 'Dell')
    monitor1 = Monitor('Samsung', 15)
    computadora1 = Computadora('Gei', monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = Teclado('USB', 'Dell')
    raton2 = Raton('Bluetooth', 'Dell')
    monitor2 = Monitor('Samsung', 15)
    computadora2 = Computadora('Gei', monitor2, teclado2, raton2)
    print(computadora2)