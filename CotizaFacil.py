productos = []
tasa_dia = int(input("Ingrese la tasa del dia: "))

while True:
 try:
     producto = input("Ingresa el nombre del producto: ")

     precio = float(input(f"Ingrese el precio de {producto}:$"))

     productos.append((producto,precio))

     respuesta = input("¿Quieres agregar otro producto? (s/n): ").strip().lower()

     if respuesta == "n":
        break

 except ValueError:
        print("Error: Por favor ingresa un número válido para el precio.\n")
     
subtotal = 0
for nombre, precio in productos:
    subtotal += precio

iva = subtotal * 0.16
total_usd = subtotal + iva
cambio_tasa = total_usd * tasa_dia
print("-----Detalles de la venta -----")
print(f"Tasa del dia:{tasa_dia}bs")
print(f"Producto:{productos}")
print(f"Subtotal:{subtotal}$")
print(f"Iva (16%):{iva}$")
print(f"Total a pagar:{total_usd}$ en bolivares serian {cambio_tasa:,.2f}")
