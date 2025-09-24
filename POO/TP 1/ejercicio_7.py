class App:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__blacklist = ['admin', 'root', 'user', 'administrador']
        self.check()
    
    def verificacion_caracteres(self):
        return len(self.__usuario) >= 6
    
    def verificacion_letras(self):
        return self.__usuario[0].isupper() and self.__usuario[1:].islower()
        
    def verificacion_espacios(self):
        return self.__usuario == self.__usuario.strip() and " " not in self.__usuario
        
    def verificacion_numeros(self):
        return not any(char.isdigit() for char in self.__usuario)
    
    def verificacion_especial(self):
        return self.__usuario.isalpha()
    
    def verificacion_prohibido(self):
        return self.__usuario.lower() in self.__blacklist

    def check(self):
        lista_errores = []

        if not self.verificacion_caracteres():
            lista_errores.append("El usuario debe contener almenos 6 caracteres.")
        elif not self.verificacion_letras():
            lista_errores.append("El usuario debe empezar con una mayuscula.")
        elif not self.verificacion_espacios():
            lista_errores.append("El usuario no debe de contener espacios.")
        elif not self.verificacion_numeros():
            lista_errores.append("El usuario no debe de contener numeros.")
        elif not self.verificacion_especial():
            lista_errores.append("El usuario no debe de contener caracteres especiales.")
        elif self.verificacion_prohibido():
            lista_errores.append("El usuario esta en la lista negra.")
        
        if lista_errores:
            print(f"El usuario {self.__usuario} no cumple con las condiciones: ")
            for error in lista_errores:
                print(f' - {error}')
        else:
            print(f"El usuario {self.__usuario} se ha generado sin problemas.")

if __name__ == '__main__':
    App("Pepito")