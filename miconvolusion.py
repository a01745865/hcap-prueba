#Funcion que calcula la matriz resultante después de aplicar la operacion Convolusion de A*B.
import numpy as np

def convolusion(A,B):
    C =[] 
    contador = 0
    for c in range(len(A)):
        suma = 0
        for i in range(len(B)):
            for a in range(len(B[i])):
                if contador == 0:
                    suma += A[i][a]*B[i][a]
                if contador == 1:
                    suma += A[i][a+1]*B[i][a]
                if contador == 2:
                    suma += A[i+1][a]*B[i][a]
                if contador == 3:
                    suma += A[i+1][a+1]*B[i][a]
        contador += 1
        C.append(suma)
    print(C)
Matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]

A = np.array(Matriz1)
B = np.array(Filtro)

convolusion(A,B)


