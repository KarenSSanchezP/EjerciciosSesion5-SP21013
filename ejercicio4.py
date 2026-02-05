dim = int(input("Ingrese el número de dimensiones de la matriz: "))

# Creamos una matriz identidad de tamaño dim x dim
matriz = [[0 for _ in range(dim)] for _ in range(dim)]

# Llenamos la matriz identidad
for i in range(dim):
            matriz[i][i] = 1

print(f"La matriz identidad de {dim} dimensiones es:")
for fila in matriz:
    print(fila)