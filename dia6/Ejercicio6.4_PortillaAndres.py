# Definir el diccionario con los productos y sus precios
productos = {
    "Arepa e' huevo": 2500,
    "butifarra": 1750,
    "mojarra": 3000000,
    "pastelito de iwana": 2800
}
for x, y in productos.items():
    print(x, y)
# Pedir al usuario que ingrese un producto y la cantidad
producto = input("Ingrese el nombre del producto: ").lower()
cantidad = int(input("Ingrese la cantidad: "))

# Verificar si el producto está en el diccionario
if producto in productos:
    precio_total = productos[producto] * cantidad
    print("El precio total es: ", precio_total)
else:
    print("El producto no está en la lista.")