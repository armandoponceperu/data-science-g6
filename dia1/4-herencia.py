class Persona:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        
class Alumno(Persona):        
        pass
    
class Profesor(Persona):
    def __init__(self, nombre, email, esp):
        super().__init__(nombre , email)
        self.especialidad = esp
        
    def mostrar(self):
        super().mostrar()
        print(f"Especialidad: {self.especialidad}")

Alumno1 = Alumno("Juan Perez", "jperes@gmail.com")
Alumno1.mostrar()

profesor1 = Profesor("Ana Gomez", "ana@gmail.com","Matematicas")
profesor1.mostrar()