import math
import matplotlib.pyplot as plt
def productomatrices(A, B): #Funcion para calcular la multiplicacion de dos matrices de numeros reales
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            suma = 0
            for k in range(columnas):
                suma = suma + A[i][k] * B[k][j]
            fila += [suma]
        matriz += [fila]
    return matriz

def accionmatrizvector(A,v): #Funcion para calcular la accion de una matriz de numeros reales sobre un vector de numeros reales
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma = suma + A[i][j] * v[j][0]
        matriz = matriz + [suma]
    return matriz

def sumacplx(a, b): #Funcion para calcular la suma de numeros complejos
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

def multcplx(a, b): #Funcion para calcular la multiplicacion de numeros complejos
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)

def modulocplx(a): #Funcion para calcular el modulo de un numero complejo
    return math.sqrt((a[0])**2 + (a[1])**2)

def productomatricesComplex(A, B): #Funcion para realizar el producto entre matrices de numeros complejos
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            suma = (0,0)
            for k in range(columnas):
                suma = sumacplx(suma, multcplx(A[i][k], B[k][j]))
            fila += [(suma)]
        matriz += [fila]
    return matriz

def accionmatrizvectorComplex(A,v): #Funcion para realizar la accion de una matriz de numeros complejos sobre un vector de numeros complejos 
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        suma = (0,0)
        for j in range(columnas):
            suma = sumacplx(suma, multcplx(A[i][j], v[j][0]))
        matriz = matriz + [(suma)]
    return matriz

def numestados(matriz): #Funcion para establecer los estados de la matriz
    estados = []
    for i in range(len(matriz)):
        estados += [i]
    return estados

def graficarvectorestado(estados, v): #Funcion para graficar la probabilidad de los vectores estado en sistemas probabilisticos
    plt.bar(estados, v)
    plt.title("Probabilidades del vector")
    plt.xlabel("Estados")
    plt.ylabel("Probabilidades")
    plt.show()
    plt.savefig('SistemaCuantico.png')


def main(): #Funcion principal
    print("---------------Sistemas clasicos deterministicos---------------")
    print("---------------Matriz Adyacente del sistema---------------")
    matriz = [[0,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,1,0,0,0,1],
            [0,0,1,0,0,0],
            [0,0,0,0,1,0],
            [1,0,0,0,0,0]]
    for i in matriz:
        print(i)
    n = int(input("Numero de Tics: "))
    X = [x[:] for x in matriz]
    for i in range(2,n+1):
        X = productomatrices(X,matriz)
    print("---------------Estado inicial del sistema---------------")
    inicial = [[6],[5],[4],[3],[2],[1]]
    for i in inicial:
        print(inicial)
    posicion = accionmatrizvector(X, inicial)
    print("---------------Numero de canicas en cada caja---------------")
    print(posicion)

    print("---------------Sistemas probabilisticos---------------")
    print("---------------Matriz Adyacente del sistema---------------")
    matriz = [[0, 1/6, 5/6],
              [1/3, 1/2, 1/6],
              [2/3, 1/3, 0]]
    for i in matriz:
        print(i)
    n = int(input("Numero de tics: "))
    X = [x[:] for x in matriz]
    for i in range(2, n + 1):
        X = productomatrices(X, matriz)
    print("---------------Estado inicial del sistema---------------")
    inicial = [[1], [0], [0]]
    for i in inicial:
        print(i)
    posicion = accionmatrizvector(X, inicial)
    print("---------------Probabilidad de que la canica este en cada estado---------------")
    print(posicion)
    graficarvectorestado(numestados(matriz), posicion)

    print("---------------Sistemas cuanticos probabilisticos---------------")
    matriz = [[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(1/math.sqrt(2),0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(1/math.sqrt(2),0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (-1/math.sqrt(6),1/math.sqrt(6)), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (-1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (1/math.sqrt(6),-1/math.sqrt(6)), (-1/math.sqrt(6),1/math.sqrt(6)), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (0,0), (-1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (0,0), (1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (0,0), (0,0), (0,0)]]
    print("---------------Matriz Adyacente del sistema---------------")
    for i in matriz:
        print(i)        
    n = int(input("Numero de Tics: "))
    X = [x[:] for x in matriz]
    for i in range(2, n + 1):
        X = productomatricesComplex(X, matriz)
    print("---------------Estado inicial del sistema---------------")    
    inicial = [[(1,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)]]
    for i in inicial:
        print(i)
    posicion = accionmatrizvectorComplex(X, inicial)
    print("---------------Probabilidades de caer en la posicion---------------")
    probabilidades = []
    for i in range(len(posicion)):
        probabilidades += [(modulocplx(posicion[i]))**2]
    for i in probabilidades:
        print(i)
    graficarvectorestado(numestados(matriz), probabilidades)
main()