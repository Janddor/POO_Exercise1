class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        Monitor.contar()
        self.id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def __str__(self):
        return f'Monitor[id: {self.id_monitor} marca: {self.marca} tamaño: {self.tamanio}]'
    @staticmethod
    def contar():
        Monitor.contador_monitores = Monitor.contador_monitores + 1

if __name__ =='__main__': # Ejecuta esto si está ejecutándose este programa.
    monitor1 = Monitor('Samsung', '18 in')
    print(monitor1)
    monitor2 = Monitor('Samsung', '18 in')
    print(monitor2)