# ObtenerCoordenadas


## Casos de Prueba para "Distancia entre Ciudades"

### 1. Caso de Éxito: Distancia entre dos ciudades existentes
| Test Case                                    | Precondition                                                  | Test Steps                                                                                                     | Test Data                                     | Expected Result                                                                 |
|----------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------|
| Verificar distancia entre dos ciudades válidas | Usuario debe tener conexión a internet o archivo CSV disponible | 1. Iniciar la función de cálculo de distancia.<br>2. Ingresar nombres y países de las dos ciudades.<br>3. Ejecutar el cálculo de distancia. | Ciudad 1: Lima, Perú <br> Ciudad 2: Bogotá, Colombia | Debe retornar la distancia correcta entre Lima y Bogotá en kilómetros.           |

### 2. Caso Extremo: Una ciudad no existe
| Test Case                               | Precondition                                                  | Test Steps                                                                                                     | Test Data                                     | Expected Result                                                                 |
|-----------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------|
| Verificar distancia cuando una ciudad no existe | Usuario debe tener conexión a internet o archivo CSV disponible | 1. Iniciar la función de cálculo de distancia.<br>2. Ingresar el nombre de una ciudad inexistente y el país correspondiente.<br>3. Ingresar una ciudad válida para la segunda ciudad.<br>4. Ejecutar el cálculo de distancia. | Ciudad 1: Atlantis, Oceano <br> Ciudad 2: Bogotá, Colombia | Debe lanzar un `ValueError` indicando que una o ambas ciudades no existen.      |

### 3. Caso Extremo: Las mismas ciudades ingresadas dos veces
| Test Case                                   | Precondition                                                  | Test Steps                                                                                                     | Test Data                                     | Expected Result                                                                 |
|---------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------|
| Verificar distancia entre la misma ciudad ingresada dos veces | Usuario debe tener conexión a internet o archivo CSV disponible | 1. Iniciar la función de cálculo de distancia.<br>2. Ingresar la misma ciudad y país para ambas entradas.<br>3. Ejecutar el cálculo de distancia. | Ciudad 1: Lima, Perú <br> Ciudad 2: Lima, Perú | Debe lanzar un `ValueError` indicando que la distancia es cero o que las ciudades son las mismas. |
