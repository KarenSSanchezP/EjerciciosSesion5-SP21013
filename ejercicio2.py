A = [[1, 0, -3], 
     [2, 0, 1], 
     [-1, -1, 0]]
B = [[-1, -2, 0], 
     [-2, 3, 0], 
     [0, 0, -3]]

m, n = len(A), len(A[0])# numero de filas y columnas de la matriz A
n2, p = len(B), len(B[0]) # numero de filas y columnas de la matriz B

if n == n2:
    C = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m): # Recorre filas de A
        for j in range(p): # Recorre columnas de B
            for k in range(n): # Recorre columnas de A / filas de B
                C[i][j] += (A[i][k] * B[k][j])

    for fila in C:
        print(fila)
else:
    print("No se puede realizar la operación, pues las dimensiones de las matrices no coinciden.")