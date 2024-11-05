from math import radians, sin, cos, sqrt, atan2
#trabajo de Joel Jimenez y Salvador Cordova


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distancia = R * c

    return distancia


class Coordenada:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


class Ciudad:
    def __init__(self,pais,ciudad):
        self.pais = pais.lower()
        self.ciudad = ciudad.lower()

