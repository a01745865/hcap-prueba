#Funcion que calcula la matriz resultante después de aplicar la operacion Convolusion de A*B.
import numpy as np

def convolusion(A,B):
    
    C2 = []        
    contadorRen = 0
    while (len(B)) + contadorRen <= (len(A)):
        C =[]
        contadorCol = 0
        while (len(B[0]) + contadorCol )<=  (len(A[0])):
            for c in range(len(A)):        
                suma = 0
                for i in range(len(B)):
                    for a in range(len(B[i])):
                        suma += A[i+contadorRen][a+contadorCol]*B[i][a]
            contadorCol += 1
            C.append(suma)
        C2.append(C)
        contadorRen += 1
    return C2
    
Matriz1 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
Filtro = [[1,1,1],[0,0,0],[2,10,3]]

Matriz2 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro2 = [[1,0,2],[5,0,9],[6,2,1]]


A = np.array(Matriz1)
B = np.array(Filtro)

C = np.array(Matriz2)
D = np.array(Filtro2)

print(convolusion(A, B))

print(convolusion(C, D))


