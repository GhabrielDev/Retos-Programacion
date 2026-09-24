import time

def limpiar_registo(texto):
    return texto.lower().strip().title()

time.sleep(1.0)
name = input("Ingresa tu nombre: ")
producto = input("Ingrese el nombre del producto: ")

time.sleep(0.5)
precio = float(input("Ingrese el precio del producto: "))

if precio <= 0 :
    print("El precio debe ser un número mayor a cero")
    print("Venta cancelada")

else:
    print("Procediendo venta")

    subtotal = precio * 0.10
    total_pagar = max(0,precio - subtotal )    

    nombre_arreglado = limpiar_registo(producto)
    name_cliente = limpiar_registo(name)

    time.sleep(0.9)
    print("--- Factura ---")    
    print(f"Cliente:{name_cliente}")
    print(f"Producto:{nombre_arreglado}")
    print(f"Precio:{precio}$")
    print(f"Descuento:{subtotal:.2f}")
    print(f"Total a Pagar:{total_pagar}$")
    print(30 * '-')