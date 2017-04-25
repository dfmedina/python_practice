# Python Training
Repositorio para ejercicios del training de Python

Emular Sets
Crear una clase para representar y manipular un Set (conjunto). La clase Set debe proveer las siguientes operaciones:

- Agregar un elemento al Set.
- Remover un elemento del Set.
- Diferencia entre un Set y otro Set. 
- Intersección entre un Set y otro Set.
- Un método que determine si un Set está incluído en otro Set. Es decir, si todos los elementos de un Set pertenecen al otro Set.
- Diferencia simétrica entre un Set y otro Set.
- Producto cartesiano entre un Set y otro Set.
- Conjunto potencia de un Set.

Nota: recuerda que un Set no permite elementos duplicados, solo mantiene elementos únicos.
Se puede definir un Set y sus elementos al momento de crear una instancia de la clase, como se muestra a continuación:
Set([1,2,3,4,5,6,1,4])
No usar el tipo 'set' ya incluído en el lenguaje en su implementación.

Referencia de Conjuntos:
https://es.wikipedia.org/wiki/Diferencia_sim%C3%A9trica
https://es.wikipedia.org/wiki/Producto_cartesiano
https://es.wikipedia.org/wiki/Conjunto_potencia


##Cálculo Matricial
Crear una clase que permita representar una matriz de cualquier orden o forma (n x n, n x m). 
También debe permitir realizar las siguientes operaciones con matrices.

- Suma de matrices
- Producto de un escalar por una matriz
- Producto de matrices
- Traspuesta de una matriz
- Determinante de la matriz
- Matriz adjunta
- Matriz inversa

Agregar métodos adicionales:

- Un método para obtener una filas de una matriz. No devolver filas repetidas.
Por ejemplo, se puede indicar que se desean la filas 1, 3, 8 de una matriz de 20 x 10.

- Un método para obtener una columnas de una matriz. No devolver columnas repetidas.
Por ejemplo, se puede indicar que se desean las columnas 2, 4, 10 de una matriz de 20 x 10.

- Un método para obtener una parte de la matriz a partir de una columna cualquiera. 
Por ejemplo de una matriz de 10 x 10, se quiere obtener la matriz de 10 x 2 a partir de la columna 5.

- Un método para mostrar en pantalla la matriz, en forma de matriz.

Se puede definir una matriz de 3 x 6 al momento de instanciar la clase como se muestra a continuación:
Matrix([[1,2,3,4,5,6],
	[10,11,12,13,14,15],
	[-1,-2,-3,-4,-5,-6]])

Referencia de Cálculo Matricial:
http://matematicasbachiller.com/videos/2-bachillerato/introduccion-al-algebra-de-lo-lineal/01-calculo-matricial-6

Sistema de archivos: Implementar el comando tree
El comando tree muestra la estructura de carpetas con una estructura de árbol partiendo de la carpeta donde se ejecuta el comando e incluyendo todos los archivos, subcarpetas, archivos y carpetas en las subcarpetas y continúa recursivamente.

A continuación se puede ver un ejemplo de salida de la ejecución de un comando tree.

.
├── config.dat
├── data
│   ├── data1.bin
│   ├── data2.sql
│   └── data3.inf
├── images
│   ├── background.jpg
│   ├── icon.gif
│   └── logo.jpg
├── program.exe
└── readme.txt
ETL
Procesando el archivo con datos de 5000 películas extraídas de IMDB, contestar las preguntas o consultas que aparecen más abajo. Mostrar los resultados obtenidos en un documento HTML(simple). Adicionalmente, agregar el tiempo que toma el procesar los datos para lograr los requerimientos.

- ¿Cuantas peliculas a "color" y "blanco y negro" hay en la lista?
- ¿Cuantas películas produjeron cada director?
- ¿Cuáles son las 10 películas menos criticadas?
- ¿Cuáles son las 20 películas con mayor duración?
- ¿Cuáles son las 5 películas que recaudaron más dinero?
- ¿Cuáles son las 5 películas que recaudaron menos dinero?
- ¿Cuáles son las 3 películas que gastaron mayor cantidad de dinero para producirse?
- ¿Cuáles son las 3 películas que gastaron menor cantidad de dinero para producirse?
- ¿En qué año se lanzaron más películas?
- ¿En qué año se lanzaron menos películas?
- Crear un ranking de actores donde aparezca:
	- la cantidad de películas en las que participó el actor
	- su influencia en las redes sociales
	- su mejor película
	- ordenado por cantidad de actuaciones
- Crear un tag cloud usando los tags o keywords de las películas. 
Para hacer esto solo basta con crear y mostrar un ranking de palabras y su peso (cantidad de apariciones de la palabra), ordenado de mayor a menor.
- ¿Que genero de películas recaudó más dinero para cada año?
- ¿Que genero de películas recaudó menos dinero para cada año?
- Mostrar el ranking de actores ordenado por actuaciones y popularidad.
- ¿Que genero les gusta más a las personas?
- ¿Cuales son los 5 directores con mejor reputación?

Archivo con datos de películas: 
https://drive.google.com/open?id=0B7BCSacG-KJgUE1YRW9wUEQwUDQ

