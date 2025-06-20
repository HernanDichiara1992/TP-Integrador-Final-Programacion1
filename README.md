Comparación de algoritmos de búsqueda en Python:
Este proyecto forma parte del Trabajo Integrador Final de la asignatura Programación I. El objetivo principal es comparar el rendimiento entre los algoritmos de búsqueda lineal y búsqueda binaria, aplicados sobre listas de distintos tamaños, y analizar cómo escalan en términos de eficiencia.

-Contenido del proyecto:
Código fuente principal que genera listas aleatorias, aplica ordenamiento y ejecuta pruebas de búsqueda.
Algoritmos implementados manualmente:
Búsqueda binaria (iterativa)
Búsqueda lineal
Uso del método sort() de Python (Timsort) para ordenar listas grandes.

-Qué hace el script?:
Genera listas aleatorias de diferentes tamaños (1.000, 10.000, 100.000, 1.000.000).
Ordena las listas para aplicar búsqueda binaria.
Busca un elemento central utilizando ambos algoritmos.
Mide e imprime los tiempos de ejecución para cada búsqueda.
Compara resultados y evidencia la diferencia de rendimiento.

-Cómo ejecutar el código:
Clonar el repositorio o descargar el archivo comparacion_busquedas.py.
Asegurarse de tener Python 3 instalado.
Ejecutar desde terminal o IDE

-Reflexiones:
Este experimento demuestra que:
La búsqueda binaria es significativamente más eficiente que la búsqueda lineal, especialmente a gran escala.
En listas muy grandes, la diferencia de rendimiento puede ser de más de 300 veces.
El uso de un método de ordenamiento eficiente (sort()) es clave para trabajar con grandes volúmenes de datos sin afectar los resultados.

-Fuentes consultadas:
Material teórico de la cátedra.
Documentación oficial de Python: https://docs.python.org/3/library/
Apuntes de clase y experimentación propia.
