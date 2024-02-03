import math

# Función para calcular el mcd
def calcular_mcd(a, b):
    return math.gcd(a, b)

# Función para calcular el mcm
def calcular_mcm(a, b):
    return a * b // math.gcd(a, b)

# Lectura de la entrada
while True:
    X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        break

    monedas = [int(input()) for _ in range(X)]
    alturas = [int(input()) for _ in range(Y)]

    # Iteración a través de las alturas
    for altura in alturas:
        max_longitud = 0
        min_longitud = float('inf')

        # Iterar a través de todas las combinaciones de cuatro monedas diferentes
        for i in range(X):
            for j in range(X):
                for k in range(X):
                    for l in range(X):
                        mcd = calcular_mcd(monedas[i], calcular_mcd(monedas[j], calcular_mcd(monedas[k], monedas[l])))
                        mcm = calcular_mcm(monedas[i], calcular_mcm(monedas[j], calcular_mcm(monedas[k], monedas[l])))
                        
                        longitud = altura * mcd // mcm
                        max_longitud = max(max_longitud, longitud)
                        min_longitud = min(min_longitud, longitud)

        print(max_longitud, min_longitud)