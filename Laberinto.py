#Laberinto

##Dimensiones

filas=5 
columnas=5

#lista del laberinto con espacios
laberinto=[[' ' for _ in range(columnas)] for _ in range(filas)]

#definir coordenadas de las casillas con muro
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

# 'x' en las casillas
for i, j in muro:
    laberinto[i][j] = 'X'

# inicio y final

laberinto[0][0]='E'
laberinto[4][4]='s'

# Ver el laberinto
for fila in laberinto:
    print(' '.join(fila))

def encontrar_camino(laberinto):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    pila = [(0, 0)]
    visitados = set()

    while pila:
        fila, columna = pila[-1]

        if fila == filas - 1 and columna == columnas - 1:
            break

        visitados.add((fila, columna))

        direcciones = [(1, 0, 'Abajo'), (0, 1, 'Derecha'), (-1, 0, 'Arriba'), (0, -1, 'Izquierda')]
        encontrado = False

        for d_fila, d_columna, movimiento in direcciones:
            siguiente_fila, siguiente_columna = fila + d_fila, columna + d_columna

            if 0 <= siguiente_fila < filas and 0 <= siguiente_columna < columnas and laberinto[siguiente_fila][siguiente_columna] != 'X' and (siguiente_fila, siguiente_columna) not in visitados:
                pila.append((siguiente_fila, siguiente_columna))
                encontrado = True
                break

        if not encontrado:
            pila.pop()

    camino = []
    for i in range(1, len(pila)):
        fila_actual, columna_actual = pila[i - 1]
        siguiente_fila, siguiente_columna = pila[i]
        if siguiente_fila > fila_actual:
            camino.append('Abajo')
        elif siguiente_fila < fila_actual:
            camino.append('Arriba')
        elif siguiente_columna > columna_actual:
            camino.append('Derecha')
        elif siguiente_columna < columna_actual:
            camino.append('Izquierda')

    return camino

laberinto = [[' ' for _ in range(5)] for _ in range(5)]
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
for coordenada in muro:
    fila, columna = coordenada
    laberinto[fila][columna] = 'X'

solucion = encontrar_camino(laberinto)
print(solucion)