import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return math.sqrt(pow((x_2-x_1),2)+(pow((y_2-y_1),2)))

def get_puntos(particulas) -> list:
    puntos = []

    for p in particulas:
        x=p.origen_x
        y=p.origen_y
        r=p.red
        g=p.green
        b=p.blue
        punto = ((x,y),r,g,b)
        puntos.append(punto)
        x=p.destino_x
        y=p.destino_y
        r=p.red
        g=p.green
        b=p.blue
        punto = ((x,y),r,g,b)
        puntos.append(punto)

    return puntos

def puntos_mas_cercanos(puntos_list)->list:
    resultado = []
    for punto_i,red,green,blue in puntos_list:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 1000
        cercano = (0,0)
        for punto_j,r,g,b in puntos_list:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distancia_euclidiana(x1,y1,x2,y2)
                if d < min:
                    min = d
                    cercano = (x2,y2)

        resultado.append((punto_i,cercano,red,green,blue))
    return resultado
