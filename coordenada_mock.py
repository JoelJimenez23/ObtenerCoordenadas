from utils import Coordenada,haversine

class ObtenerCoordenadasMock:        
    def obtener_coordenadas_ciudad(self, ciudad1):
        if ciudad1.ciudad.lower() == 'lima' and ciudad1.pais.lower() == 'peru':
            return Coordenada(-12.06, -77.04)
        elif ciudad1.ciudad.lower() == 'bogota' and ciudad1.pais.lower() == 'colombia':
            return Coordenada(4.71, -74.07)
        else:
            return None

    def distancia_entre_ciudades(self,ciudad1,ciudad2):
        coordenadas1 = self.obtener_coordenadas_ciudad(ciudad1)
        coordenadas2 = self.obtener_coordenadas_ciudad(ciudad2)
        return haversine(coordenadas1.latitud,coordenadas1.longitud,coordenadas2.latitud,coordenadas2.longitud)

    
