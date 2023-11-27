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

for fila in laberinto:
    print(' '.join(fila))
