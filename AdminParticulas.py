from Particulas import Particula

class AdminParticulas:
    def __init__(self):
        self.__particulas = []

    def agregarFinal(self, particula:Particula):
        self.__particulas.append(particula)

    def agregarInicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrarParticulas(self):
        if(len(self.__particulas) == 0):
            print("Lista Vacia") 

        for particula in self.__particulas:
            print(particula) 
            print("\n")

    def __str__(self) -> str:
        return "".join(
           str(particula) for particula in self.__particulas
        )

# particula01 = Particula(1, 900, 200, 30, 20, 40 ,54, 21, 84)
# particula02 = Particula(2, 100, 0, 39, 19, 53 ,28, 43, 91)
# admin = AdminParticulas() 
# admin.mostrarParticulas() #VACIO
# admin.agregarInicio(particula01) 
# admin.mostrarParticulas() #PARTICULA 1
# admin.agregarFinal(particula02)
# admin.mostrarParticulas()

