class Persona:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        
class Alumno(Persona):
    
    def __init__(self, nombre, email, Curso):
        super().__init__(nombre, email)
        self.curso = Curso
        
    def mostrar(self):
        print("====== DATOS DEL ALUMNO ======")
        super().mostrar()
        print(f"curso: {self.curso}")        
    
class Profesor(Persona):
    def __init__(self, nombre, email, esp):
        super().__init__(nombre , email)
        self.especialidad = esp
        
    def mostrar(self):
        print("====== DATOS DEL PROFESOR ======")
        super().mostrar()
        print(f"Especialidad: {self.especialidad}")

Alumno1 = Alumno("Juan Perez", "jperes@gmail.com", "fisica")
Alumno1.mostrar()

profesor1 = Profesor("Ana Gomez", "ana@gmail.com","Matematicas")
profesor1.mostrar()