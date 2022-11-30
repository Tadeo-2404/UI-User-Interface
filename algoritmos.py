import math

def distancia_euclidiana(origen_x=0, destino_x=0 ,origen_y=0, destino_y=0):
    return math.sqrt( pow(origen_x-destino_x, 2) + pow(origen_y-destino_y, 2))

def puntos_mas_cercanos(puntos_list)->list:
    resultado = []
    for punto_i, red, green, blue in puntos_list:
        x1: punto_i[0]
        y1: punto_i[1]
        min = 1000
        cercano = (0,0)
        for punto_j,r,g,b in puntos_list:
            if(punto_i)