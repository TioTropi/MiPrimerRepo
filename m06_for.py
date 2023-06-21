# Un for tiene muchas funciones, principalmente se usa para iterar una lista de elemntos,
# buscar elementos, realizar operaciones matemáticas etc.

# range es un iterable que devuelve una secuencia númerica desde 0 hasta el número que escribimos -1;
# por ejemplo range(5) devuelve la secuencia de 0, 1, 2, 3, 4.
# En este caso NUMERO va a tomar el valor de cada elemento que indiquemos en range,
# es por eso que el código se ejecuta el número de elementos.
for NUMERO in range(5):
    print(NUMERO, NUMERO * "Hola Mundo! ")

# También podemos hacer más operaciones al imprimir la variable:
# como multiplicarla por sí misma.
for NUMERO in range(5):
    print(NUMERO, NUMERO * "Hola Mundo! ")


# Ejemplo de sintaxis de uso de for para buscar un elemento dentro de una base de datos:
BUSCAR = 34
for NUMERO in range(5):
    print(NUMERO)
    if NUMERO == BUSCAR:
        print("Encontrado", BUSCAR)
        # break detiene la ejecución del código si la comparación se cumple.
        break
# else se ejecuta si la condición de for no se cumple.
# Esta fuuncionalidad será muy util para la escritura de algoritmos.
else:
    print("No encontré el número buscado pipipipi :´v")

# Existen muchos más iterables dentro de phyton, como las listas, las tuplas; los strings, etc.
# Ejemplo de sintaxis de iteración con strings:
for char in "Ultimate Python":  # en este caso char es el string.
    print(char)
