#RRHH Api Magneto

La siguiente api le permite a magneto reclutar mutantes.

### Algoritmo Principal
El archivo mutant.py contiene el algoritmo principal.
Cuenta con las siguientes funciones

 - isMutant(dna): recibe una lista de strings y retorna si es adn mutante. Realiza una sola iteracion, en la cual verfica simultaneamente el adn vertical, horizontal y diagonal. En la primera ocurrencia de adn, termina el ciclo.
 - validDna(dna): verifica que el dato ingresado contenga la sintaxis esperada para el analisis de adn. Las verificaciones son:
    1. Dna tiene que ser una lista
    2. Cada elemento de la lista, debe ser un string
    3. Debe ser NxN, es decir, el tamaño de la lista debe coincidir con el tamaño de cada string.
    4. Solo puede recibir las letras (A,T,C,G)
 - testIsMutant(): es una funcion que ejecuta una serie de validaciones y pruebas sobre las dos funciones previas. Son test para verificar que los algoritmos funcionan correctamente. Este algoritmo se ejecuta una vez cada vez que el servidor se inicia.

### Api RRHH

La direccion para acceder es https://rhmagneto.herokuapp.com

Estan habilitados los siguientes endpoints:
- GET / : Devuelve informacion general de la api
- GET /stats : Devuelve informacion estadisiticas de los registros ingresados
- POST /mutant : Si el registro no estaba en la base de datos, se inserta. Responde 200 (mutante), 403 (humano). Todos los posteos se validan antes de ser analizados, por lo cual, si no se envia correctamente el formato esperado, devuelve un error 400 Formato incorrecto.

### Funcionamiento

Para comparar dierentes DNAs, en la base de datos se crea un hash asociado al dna ingresado. Al enviar un nuevo dna, si el hash no esta en la base de datos, se lo agrega. Indepeneidente mente de si se agrega o no, la api responde 200 (mutante) / 403 (humano).

Al correr la api en un server local, se usa la base de datos sqlite. Pero al correr en el servidor remoto, utiliza postgresql. Para identificar esto, existen dos configuraciones 'development' y 'production', que en base a variables de entorno, configuran un funcionamiento o el otro.

Actualmente se printea por consola, la mayoria de las acciones imortantes del server. Si se requiere mayor velocidad de respuesta, se puede presindir de este output a costa de perder el seguimiento de cada requests.

### Archivos

- main.py : inicializa el servidor y crea las tablas si no existen. Realiza testeos iniciales de funcionamiento de los algoritmos principales
- routes.py : define rutas disponibles del server
- mutant.py : algorimto de verificaciones de mutantes
- models.py : define un modelo ORM que crea y gestiona la tabla DNA
- controller.py : reciben el request desde una ruta, y utiliza diferentes recursos para responder adecuadamente 
- config.py : contiene configuraciones de funcionamiento y base de datos 'development' y 'production'
- Procfile : archivo para correr servidor remoto
- requirements.txt : liberias necesarias