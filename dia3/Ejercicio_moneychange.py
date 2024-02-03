contador=0;dividir = lambda n: (n // 10, *divmod(n % 10, 5)); numero = int(input("")); monedas_10, monedas_5, monedas_1 = dividir(numero);suma = "".join(["10+"*monedas_10,"5"*monedas_5,"+1"*monedas_1]);contador+= monedas_10+monedas_5+monedas_1;print(f"{contador}");print(f"{suma} ")


"""
---------lambda--------------
Funcion lambda o mas conocida como funcion anonima nos permite crear funciones mas cortas y resumidaas
Ejemplo: 
def suma(n1,n2):
    a=n1+n2
    return(a)
print(suma(5,2))
# Cuando simplemente con lambda se podria hacer
suma = lambda n1, n2: n1 + n2;print(suma(5, 2))
-----------Division de piso--------------------
la division de piso o // nos permite que cuando se relize una division entre dos numeros nos 
entregue el conciente entero (redondea hacia abajo)
Ejemplo:
             42/10=4,2---->42//10=4
--------------------DivMod-------------------------
La funcion divmod
   Nos sirve para que nos entregue el valor del consciente y el residuo respectivamente
   ejemplo: DivMod(9,2)
   Nos imprimiria los valores de 4 y 1
----------------------------------------------------
Luego se almacenan variables en su orden respectivo
---------------------------------------------------
 join se usa para unir las partes de la cadena   
"""
