import math

# Definir las posiciones y radios de las bolas
print("introduce las cordenas de la primera ball")
bola1_x =int(input("Digita la posicion de (x))."))
bola1_y = int(input("Digita la posicion de (y)) "))
bola1_radio = int(input("Ingresa el radio de la bola "))
print("introduce las cordenas de la segunda ball")

bola2_x =  int(input("Digita la posicion de (x)) "))
bola2_y = int(input("Digita la posicion de (y)) "))
bola2_radio = int(input("Ingresa el radio de la bola "))

# Calcular la distancia entre los centros de las bolas
distancia_centros = math.sqrt((bola2_x - bola1_x)**2 + (bola2_y - bola1_y)**2)

# Calcular la suma de los radios de las bolas
suma_radios = bola1_radio + bola2_radio

# Determinar si las bolas chocarán
chocaran = distancia_centros <= suma_radios

# Imprimir el resultado
if chocaran:
    print(True)
else:
    print(False)