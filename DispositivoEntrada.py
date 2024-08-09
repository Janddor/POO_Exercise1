class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property # get
    def tipo_entrada(self):
        return self._tipo_entrada
    @tipo_entrada.setter # set
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada
    @property # get
    def marca(self):
        return self._marca
    @marca.setter # set
    def marca(self, marca):
        self._marca = marca
    def __str__(self):
        return f'DispositivoEntrada[tipo de entrada: {self.tipo_entrada} marca: {self.marca}]'

if __name__ =='__main__': # Ejecuta esto si está ejecutándose este programa.
    dispo1 = DispositivoEntrada('Usb', 'Dell')
    print(dispo1)