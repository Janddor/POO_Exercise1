from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        DispositivoEntrada.__init__(self, tipo_entrada, marca)

    def __str__(self):
        return f'Raton[id: {self.id_raton} {DispositivoEntrada.__str__(self)}]'

if __name__ =='__main__': # Ejecuta esto si está ejecutándose este programa.
    raton1 = Raton('Usb', 'Dell')
    print(raton1)
    raton2 = Raton('Usb', 'Dell')
    print(raton2)