n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

matriz = [[0 for _ in range(m)] for _ in range(n)]

# Solicitamos el ingreso de los elementos de la matriz
for i in range(n):
    for j in range(m):
        matriz[i][j] = int(input(f"Ingrese el elemento ({i},{j}): "))

for fila in matriz:
    print(fila)

# Se realiza la suma por columna
for i in range(m): # Recorre las columnas
    suma = 0
    for j in range(n): # Recorre las filas
        suma += matriz[j][i]
    if suma > 50:
        print(f"La columna {i+1} ha excedido la cantidad")
        break
    print(f"La suma de la columna {i+1} es {suma}")