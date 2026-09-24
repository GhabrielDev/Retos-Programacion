print("---- Cursos de alta Calidad ----")
print("Curso:Empresas Polar 1000 Empresas")
print("Precio:$50")
print("-" * 30)
print("Curso:Edutin Academy")
print("Precio:$23")
print("-" * 30)
cost = float(input("Pago Curso:Ingrese el Monto a pagar:$"))

if cost  >= 50:
    descuento = 0.20
    print("Tienes un descuento del 20%")
elif cost >= 23:
    descuento = 0.07
    print("Tienes un descuento de 7%") 
else:
    print("Coloque el Monto a pagar")

subtotal = descuento * cost

print({subtotal})

