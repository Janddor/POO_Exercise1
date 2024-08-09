from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        DispositivoEntrada.__init__(self, tipo_entrada, marca)

    def __str__(self):
        return f'Teclado[id: {self.id_teclado} {DispositivoEntrada.__str__(self)}]'



if __name__ =='__main__': # Ejecuta esto si está ejecutándose este programa.
    teclado1 = Teclado('Usb', 'Dell')
    print(teclado1)
    teclado2 = Teclado('Usb C', 'Toshiba')
    print(teclado2)