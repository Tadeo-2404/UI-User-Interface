from Particulas import Particula
import json

class Admin:
    def __init__(self):
        self.particulas = []

    def agregar_final(self, particula:Particula):
        self.particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.particulas.insert(0,particula)

    def mostrar(self):
        for particula in self.particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(v) + "\n" for v in self.particulas
        )
    def __len__(self):
        return(
            len(self.particulas)
        )
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.particulas):
            particula = self.particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
        
    def guardar(self, ubicacion):
        try:
            with open(ubicacion,'w') as archivo: # La w es el modo de escritura
                lista = [particula.to_dict() for particula in self.particulas]
                print(lista)
                json.dump(lista,archivo,indent=5)
                return 1
        except:
            return 0
        
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo: # La r es el modo de lectura
                lista = json.load(archivo)
                self.particulas = [Particula(**particula) for particula in lista] 
                return 1                                            
        except:                                                         
            pass
        try:
            with open(ubicacion, 'r') as archivo:
                lista=json.load(archivo)
                self.particulas = [Particula(p["id"],p["origen"]["x"],p["origen"]["y"],p["destino"]["x"],p["destino"]["y"],p["velocidad"],p["color"]["red"],p["color"]["green"],p["color"]["blue"]) for p in lista]
            return True
        except:
            return False
    


