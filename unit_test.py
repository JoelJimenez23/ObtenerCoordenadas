import unittest
from utils import Ciudad
from coordenada_csv import ObtenerCoordenadasCSV

class TestDistanciaEntreCiudades(unittest.TestCase):

    def setUp(self):
        self.coordenada_csv = ObtenerCoordenadasCSV('./worldcities.csv')

    def test_distancia_entre_ciudades_existentes(self):
        ciudad1 = "Bogotá"
        pais1 = "Colombia"
        ciudad2 = "Lima"
        pais2 = "Peru"
        city1 = Ciudad(pais1, ciudad1)
        city2 = Ciudad(pais2, ciudad2)
        distancia = self.coordenada_csv.distancia_entre_ciudades(city1, city2)

        self.assertAlmostEqual(distancia, 1893, delta=10)  # Distancia aproximada entre Bogota y Lima en km
        print("\nPRUEBA EXITOSA")

    def test_ciudad_no_existente(self):
        ciudad1 = "marcia"
        pais1 = "marte"
        ciudad2 = "Lima"
        pais2 = "Peru"
        city1 = Ciudad(pais1, ciudad1)
        city2 = Ciudad(pais2, ciudad2)
        distancia = self.coordenada_csv.distancia_entre_ciudades(city1, city2)

        self.assertAlmostEqual(distancia, 1893, delta=10) 
        print("PRUEBA EXITOSA")

    def test_misma_ciudad_dos_veces(self):
        ciudad1 = "Lima"
        ciudad2 = "Lima"
        pais1 = "Peru"
        pais2 = "Peru"
        city1 = Ciudad(pais1, ciudad1)
        city2 = Ciudad(pais2, ciudad2)
        distancia = self.coordenada_csv.distancia_entre_ciudades(city1, city2)

        self.assertAlmostEqual(distancia, 18, delta=10) 
        print("PRUEBA EXITOSA")
        

if __name__ == '__main__':
    unittest.main()

