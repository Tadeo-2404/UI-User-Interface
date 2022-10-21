import math

def distancia_euclidiana(origen_x=0, destino_x=0 ,origen_y=0, destino_y=0):
    return math.sqrt( pow(origen_x-destino_x) + pow(origen_y-destino_y))