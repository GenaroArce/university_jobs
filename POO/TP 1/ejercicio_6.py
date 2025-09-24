marca = "Motorola"
modelo = "G8"
memoria = "3"

class Celular:
    def __init__(self, marca: str, modelo: str, memoria: str) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__memoria = memoria
    
    def __str__(self) -> str:
        return "Su celular es el modelo {} de la marca {} y tiene {}GB de RAM".format(self.__modelo, self.__marca, self.__memoria)
    
    def getCelular(self):
        print("Su celular es el modelo {} de la marca {} y tiene {}GB de RAM".format(self.__modelo, self.__marca, self.__memoria))

    def getCelularDict(self):
        return {
            'marca': self.__marca,
            'modelo': self.__modelo,
            'memoria': self.__memoria
        }
    
if __name__ == "__main__":
    print(Celular(marca, modelo, memoria))
    
    mi_celular = Celular(marca, modelo, memoria)
    mi_celular.getCelular()
    
    info = mi_celular.getCelularDict()
    print(f"Su celular es el modelo {info['modelo']} de la marca {info['marca']} y tiene {info['memoria']}GB de RAM")