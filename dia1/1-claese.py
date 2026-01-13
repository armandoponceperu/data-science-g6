#PROGRAMACION ORIENTADA A OBJETOS (POO)
#Las clases son plantillas para crear objetos (instancias)
# Una clase puede tener atributos (caracteristicas) y metodos (funciones)

class Automovil:
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    def encender(self):
        print(f"Encendiendo el automovil {self.marca} de color {self.color}")
    
    def avanzar(self):
        print(f"El automovil {self.marca} esta avanzando")
        
    def acelerar (self):
        print(f"El automovil{self.marca} esta acelerando")
        
    def frenar(self):
        print(f"El automovil {self.marca} es frenando")
        
vw = Automovil(1970,'CH-1234' , 'Amarillo' , 'volkwagen')
vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()

tico = Automovil(2005, 'p-5678' , 'Rojo' , 'Tico')
tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()