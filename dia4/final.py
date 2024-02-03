def es_cousin(numero):
    return sum(int(digito) for digito in str(numero))

def plus_digitos(numero): # Esta funcion coje el numero y suma los digitos, luego lo vuelve una cadena 
    return sum(int(digito) for digito in str(numero))#luego la suma de cada uno lo devuelve en integer

def facts_cousin(numero):
    factores = []
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            factores.append(factor)
            numero //= factor
        else:
            factor += 1
    return factores

def siguiente_numero_smith(numero):
    next = numero + 1
    smith_encontrados = 0
    while smith_encontrados < 3:
        if not es_cousin(next) and plus_digitos(next) == sum(plus_digitos(factor) for factor in facts_cousin(next)):
            print(next, "es un número Smith")
            smith_encontrados += 1
            if smith_encontrados % 3 == 0:  # Si hemos encontrado 5 números de Smith
                print()  # Imprimir una línea en blanco
        next += 1

# Solicitar al usuario que introduzca los números
print("Por favor, introduce los números separados por comas y luego presiona Enter.")
entrada = input().replace(" ", "")  # Eliminar los espacios
numeros = list(map(int, entrada.split(',')))

for numero in numeros:
    siguiente_numero_smith(numero)