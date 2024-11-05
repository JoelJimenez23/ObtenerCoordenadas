import csv
from utils import Coordenada, haversine

class ObtenerCoordenadasCSV:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv

    def obtener_coordenadas_ciudad(self, ciudad):
        with open(self.archivo_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['city'].lower() == ciudad.ciudad.lower() and row['country'].lower() == ciudad.pais.lower():
                    return Coordenada(float(row['lat']), float(row['lng']))
        raise ValueError(f"Ciudad '{ciudad.ciudad}, {ciudad.pais}' no encontrada en el archivo CSV")  # Lanza una excepción si no se encuentra la ciudad

    def distancia_entre_ciudades(self, ciudad1, ciudad2):
        coordenadas1 = self.obtener_coordenadas_ciudad(ciudad1)
        coordenadas2 = self.obtener_coordenadas_ciudad(ciudad2)
        response =  haversine(coordenadas1.latitud, coordenadas1.longitud, coordenadas2.latitud, coordenadas2.longitud)

        if response == 0:
            raise ValueError("Distancia 0, ciudades iguales")
        else:
            return response
