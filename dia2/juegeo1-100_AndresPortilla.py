import random   # Se importa una funcion global para la funcion aleatoria

#Se crea una funcion donde lleva todo el funcionamiento 
def adivinar_numero():
    print("¡Bienvenido al juego de adivinar el número secreto!")
    print("El número secreto está entre 1 y 100. Tienes 10 intentos para adivinarlo.")

    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0
#Se abre un ciclo while para que analize el numero de intentos y repita el proceso
    while intentos_realizados < 10:
        try:      # Evalua la instruccion para luego analizar si hay un error 
            suposicion = int(input("Intenta adivinar el número: "))
            if suposicion < 1 or suposicion > 100:
                print("Por favor ingresa un número entre 1 y 100.")
                continue
        except ValueError: # es una excepción incorporada (definida por Python) que es lanzada cuando una función espera un valor determinado pero recibe otro.

            print("Por favor ingresa un número válido.")
            continue

        intentos_realizados += 1

        if suposicion < numero_secreto:
            print("El número secreto es mayor.")
        elif suposicion > numero_secreto:
            print("El número secreto es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos_realizados} intentos.")
            return

    print(f"Lo siento, has agotado tus 10 intentos. El número secreto era {numero_secreto}.")

adivinar_numero()