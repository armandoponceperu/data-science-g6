# ENCAPSULAMIENTO EN POO CON PHYTON
class Usuario:
    
    email = 'admin@gmail.com'
    password = '123'
    
    def __init__(self):
        pass
    
    def login(self,email,password):
        if email == self.usuario_email and password == self.usuario_password:
            print('login exitoso')
        else:
            print('Login fallido')
        
print("LOGIN DE USUARIO")
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')

Usuario = Usuario()
print(Usuario.Usuario_password)
Usuario.login(email, password)