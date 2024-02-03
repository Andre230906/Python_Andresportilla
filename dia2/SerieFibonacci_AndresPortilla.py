def fibonacci(x):
     a=0
     b=1
     for i in range (x):
        c=a+b
        a=b
        b=c
     return b


print("-------------¡Bienvenido al explorador de la Secuencia de Fibonacci!-------------")
print("La Secuencia de Fibonacci es una serie matemática fascinante que comienza con 0 y 1, y cada término subsiguiente es la suma de los dos anteriores.")
print("¡Diviértete descubriendo los misterios matemáticos de Fibonacci")
while True:
    a = str(input("Ingresa la letra (a) para obtener mas informacion sobre fibonacci//(para abandonar la pagina oprime (q)): "))
    if a.lower()=="q":  ## el lower funciona para transformar las mayusculas en minusculas
        print("Muchas gracias por visitar nuestra pagina")
        break
  
    elif   a.lower()=="a":
            opciones=[]
            opciones.append( print("¿Quien fue fibonacci?"  " (1)"))
            opciones.append( print("¿Por que la secuencia empieza con 0 y 1?" " (2)"))
            opciones.append( print("Probar la secuencia fibonacci"  " (3)" ))
            print("Escoje un numero para continuar leyendo sobre fibonacci")
            h=int(input())
            if h==1:
                  print("Leonardo de Pisa, también conocido como Fibonacci, fue un matemático italiano nacido alrededor del año 1170. Es conocido por introducir la secuencia de Fibonacci al mundo occidental a través de su libro Liber Abaci (El libro del ábaco) publicado en 1202. Este libro introdujo al mundo occidental al sistema de numeración hindú-arábigo, así como a numerosos conceptos matemáticos, incluida la famosa secuencia que lleva su nombre.")
                  print("")
            if h==2:
                print("La Secuencia de Fibonacci comienza con 0 y 1 debido a la definición matemática inicial de la secuencia")  
                print("La secuencia comienza con estos dos números iniciales, 0 y 1, y a partir de ahí, cada término subsiguiente es la suma de los dos términos anteriores. Matemáticamente, se define de la siguiente manera:")    
                print("1.El primer término (n=0) es 0.")
                print("2.El segundo término (n=1) es 1.")
                print("3.Para n ≥ 2, el n-ésimo término es la suma de los dos términos anteriores: F(n) = F(n-1) + F(n-2).")
                print("Para evidenciar un ejemplo presiona (j)//para ignorar el ejemplo presiona (p) ")
                z=str(input())
                if z.lower()=="j":
                        print("Este ejemplo lleva la secuencia hasta su quinto termino")
                        for i in range (6):
                            print(fibonacci(i))
                        print("Esta definición inicial de la secuencia con 0 y 1 como se eviedencia en el ejemplo es fundamental para su naturaleza matemática y su relación con muchos fenómenos naturales y estructuras en la ciencia y la naturaleza.")
                                    
                elif z.lower()=="p":
                        print("Esta definición inicial de la secuencia con 0 y 1 es fundamental para su naturaleza matemática y su relación con muchos fenómenos naturales y estructuras en la ciencia y la naturaleza.")
                                       
                else:
                        print("Por favor ingresar una intruccion correcta")
            if h==3:
                 num= int(input("Ingresa hasta que numero (n) deseas que llegue ala secuencia fibonacci: "))
                 for i in range (num):
                    print(fibonacci(i))
                        
            else:
             print("ingresa un numero que este en el rango")
                 
    else: 
            print(" Por favor ingresa una instruccion valida ")             
            
        
