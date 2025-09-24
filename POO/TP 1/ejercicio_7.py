class App:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.check()
    
    def verificacion_caracteres(self):
        return len(self.__usuario) >= 6
    
    def verificacion_letras(self):
        return self.__usuario == self.__usuario.capitalize()
        
    def verificacion_espacios(self):
        return self.__usuario == self.__usuario.strip()
        
    def verificacion_numeros(self):
        return not any(char.isdigit() for char in self.__usuario)

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
        
        if lista_errores:
            print(f"El usuario {self.__usuario} no cumple con las condiciones: ")
            for error in lista_errores:
                print(f' - {error}')
        else:
            print(f"El usuario {self.__usuario} se ha generado sin problemas.")

if __name__ == '__main__':
    App("Pepito")