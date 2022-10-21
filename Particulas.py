from algoritmos import distancia_euclidiana

class Particula :
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red = 0, green=0, blue=0, distancia=0.0):
         self.__id  = 0
         self.__origen_x = 0 
         self.__origen_y = 0
         self.__destino_x = 0
         self.__destino_y = 0
         self.__velocidad = 0
         self.__red = 0
         self.__green = 0
         self.__blue = 0
         self.__distancia = distancia_euclidiana(self.__origen_x, self.__destino_x, self.__origen_y, self.__destino_y)

    def __str__(self):
        return (
            "INFORMACION" + "\n" +
            "ID: " + str(self.__id) + "\n" +
            "OrigenX: " + str(self.__origen_x) + "\n" +
            "OrigenY: " + str(self.__origen_y) + "\n" +
            "DestinoX: " + str(self.__destino_x) + "\n" +
            "DestinoY: " + str(self.__destino_y) + "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "Red: " + str(self.__red) + "\n" +
            "Green: " + str(self.__green) + "\n" +
            "Blue: " + str(self.__blue) + "\n" +
            "Distancia: " + str(self.__distancia)
        )

# particula = Particula(1,2,3,4,5,6,7,8,9,10.0)
# print(particula)