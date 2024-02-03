##-----------------------------------------
##---------------Basic---------------------
##-----------------------------------------
print("hola mundo") ##imprimir mensajes
a=str(input())##Creacion de variable,Leer datos, y definir la variable
## los tipos de datos son int,double,float,boolean,string
## Example
print("This program determines half your age in 5 years ")
name=str(input("What is your name: "));
age=int(input("enter your age: "))
age= (age+5)/2
print("hello ",name)
print("The result of the operation is: ",age,"years") 
##---------------------------------------------
##-------------if,elif,else--------------------
##------------si,sino,ademas-------------------
##---------------------------------------------h
age = int(input("enter your age: "))
if age>=50:
    print("you are already an older person")
elif  age>=18 and age<=50:
    print("you are already an adult person")
else:
        print("you are already a kid ")
##-------------------------------------------
c=bool(input("enter true or false: "))  
if c:
    print("this is a true")     
else:
    print("this is a false")  
##-------------------------------------------
##-------------------------------------------
##----------------metodosstring--------------
named=input("enter your full name: ")
result=len(name)##longitud de cadena
print(result)
result=name.find("a")##buscar un caracter o palabra
print(result)
result=name.rfind("a")##buscal la posicion del caracter 
print(result)
##---------------------------------------------
##----------------while loop-------------------
##---------------------------------------------
name=str(input("enter your name "))
while name == "":
       print("you did not enter your name")
       name=input("enter your name: ")
print(f"hello {name}")
 ##--------------------------------------------
 ##------------------for-loop------------------
 ##--------------------------------------------
for i in range(1, 11,1): 
    print(i)
##-----------------arrays list-----------------
foods = []
prices= []
total=0 
while True:
    food = str(input("enter a food to buy(q to quit): "))
    if food.lower()=="q":  ## el lower funciona para transformar las mayusculas en minusculas
        break
    else:
        price=float(input(f"Enter the price of a {food}:  $"))##ingresa el precio 
        foods.append(food)##agrega al array
        prices.append(price)
print("-----YOUR CART------")
for food in foods: ##el ciclo for recorrera todos los items del array para asi llenarlos y luego imprimir
    print(food)  ## para organizar un array en horizontal usar : ,end=" "      
    for price in prices:
        total += price
print("")
print(f"your total is; ${total}")
##---------------function------------
#------------------------------------
def happybirthday(name):
    print(f"happy birthday to {name}")
    print("you older")
    print(f"happy birthday to {name}")   
    print() 
happybirthday("bro")               

               