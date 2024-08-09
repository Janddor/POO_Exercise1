from Orden import Orden
from mundo_pc.Computadora import Computadora
from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado

teclado1= Teclado('USB', 'Samsung')
raton1 = Raton('Bluetooth', 'Samsung')
monitor1 = Monitor('Samsung', 15)
computadora1 = Computadora('Samsung', monitor1, teclado1, raton1)

teclado2 = Teclado('USB', 'HP')
raton2 = Raton('Bluetooth', 'HP')
monitor2 = Monitor('HP', 15)
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado3 = Teclado('USB', 'Janus')
raton3 = Raton('Bluetooth', 'Janus')
monitor3 = Monitor('Janus', 27)
computadora3 = Computadora('Janus', monitor3, teclado3, raton3)
print('Agregando un nuevo elemento')
orden1.agregar_computadora(computadora3)
print(orden1)
