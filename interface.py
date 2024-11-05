from coordenada_api import ObtenerCoordenadasAPI
from coordenada_csv import ObtenerCoordenadasCSV
from coordenada_mock import ObtenerCoordenadasMock
from utils import Ciudad

def main():

    print("Selecciona el método para obtener las coordenadas:")
    print("1. Leer desde CSV")
    print("2. Usar API de OpenStreetMap")
    print("3. Usar Mock (valores fijos)")
    opcion = input("Ingresa tu opción (1/2/3): ")

    if opcion == "1":
        archivo_csv = './worldcities.csv'  # Asegúrate de tener el archivo CSV en la misma carpeta
        obtener_coordenadas = ObtenerCoordenadasCSV(archivo_csv)
    elif opcion == "2":
        obtener_coordenadas = ObtenerCoordenadasAPI()
    elif opcion == "3":
        obtener_coordenadas = ObtenerCoordenadasMock()
    else:
        print("Opción inválida.")
        return


    print("1. Coordenadas de ciudad")
    print("2. Distancia entre ciudades")
    opcion1 = input("Ingresa tu opción (1/2): ")
    if opcion1 == "1":
        ciudad = input("Ingrese el nombre de la ciudad:")
        pais = input("Ingrese el nombre del pais:")
        city = Ciudad(pais,ciudad)
        coordenadas = obtener_coordenadas.obtener_coordenadas_ciudad(city)
        print("Coordenadas: ")
        print("Latitud :",coordenadas.latitud)
        print("Logitud: ",coordenadas.longitud)

    elif opcion1 == "2":

        ciudad1_nombre = input("Ingresa el nombre de la primera ciudad: ")
        ciudad1_pais = input("Ingresa el nombre del país de la primera ciudad: ")
        ciudad1 = Ciudad(ciudad1_pais,ciudad1_nombre)
        ciudad2_nombre = input("Ingresa el nombre de la segunda ciudad: ")
        ciudad2_pais = input("Ingresa el nombre del país de la segunda ciudad: ")
        ciudad2 = Ciudad(ciudad2_pais,ciudad2_nombre)
        coordenadas1 = obtener_coordenadas.distancia_entre_ciudades(ciudad1,ciudad2)
        print("\n")
        print(f"La distancia entre {ciudad1_nombre} y {ciudad2_nombre} es {coordenadas1:.2f} km")
    print("\n\n")
    main()


if __name__ == "__main__":
    main()


