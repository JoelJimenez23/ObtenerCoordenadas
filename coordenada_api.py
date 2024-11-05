import requests
from utils import haversine, Coordenada

class ObtenerCoordenadasAPI:
    def obtener_coordenadas_ciudad(self,ciudad):
        #pais_nombre = ciudad.pais
        ciudad = ciudad.ciudad
        pais = ciudad.pais
        url = f"https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json"

        response = requests.get(url)
        if response:
            data = response.json()
            lat = data.lat
            lon = data.lon
            cor = Coordenada(lat,lon)
            return cor
        return None  # Si no se encuentra la ciudad
    def distancia_entre_ciudades(self, ciudad1, ciudad2):
        coordenadas1 = self.obtener_coordenadas_ciudad(ciudad1)
        coordenadas2 = self.obtener_coordenadas_ciudad(ciudad2)
        print(coordenadas1)
        print(coordenadas2)
        if coordenadas1 is None or coordenadas2 is None:
            return 0
        return haversine(coordenadas1.latitud, coordenadas1.longitud, coordenadas2.latitud, coordenadas2.longitud)



