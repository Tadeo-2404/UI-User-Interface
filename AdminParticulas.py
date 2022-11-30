from Particulas import Particula
import json


class AdminParticulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)
    
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)

    def __str__(self):
        return "".join(
            str(v) + "\n" for v in self.__particulas
        )

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                 lista = [particula.to_dict() for particula in self.__particulas]
                 print(lista)
                 json.dump(lista, archivo,indent = 5)
                 return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
        except:
            pass
        try:
            with open(ubicacion, 'r') as archivo:
               lista = json.load(archivo)
               self.__particulas = [Particula(p["id"], p["origen"]["x"], p["origen"]["y"], p["destino"]["x"], p["destino"]["y"], p["velocidad"], p["color"]["red"], p["color"]["green"], p["color"]["blue"]) for p in lista]
               return True
        except:
            return False

    
    def __len__(self):
        return(
            len(self.__particulas)
        )
    
    def __iter__(self):
        self.cont = 0
        return self
    def __next__(self):
        if self.cont < len(self.__particulas):
            avion = self.__particulas[self.cont]
            self.cont += 1
            return avion
        
        else:
            raise StopIteration
    
    def ordenar_id(self):
        self.__particulas.sort(key=lambda particula: particula.id)
    
    def ordenar_distancia(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)
    
    def ordenar_velocidad(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)
