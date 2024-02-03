"""""
def negate(num):
    return -num
def large_num(num):
    res=(num>1000)
negate(b)
neg_b=num
print ("b:",b,"neg_b:",neg_b)

Big= large_num(b)
print "b is big" , Big
"""

"""
Se cometen los siguientes errores:
1.Nunca se define la variable b, por ende es inutil usarla
2.en la linea  7 del codigo, se llama num cuando es un parametro y no una variable
3.La funcion large_num no devuelve ningun valor simplemente evalua si es mayor y ya.
"""
##-------------------Solucion---------------------
def negate(num):
    num= (-1)*num
    return num
def large_num(num):
    if num>=1000:
        num= True 
        print(f"the Number is equal an:{num}")   
    else:
        num=False
        print(f"the Number is equal an:{num} ")   

num=int(input("Digit the number: "))
print (negate(num))
print(large_num(num))