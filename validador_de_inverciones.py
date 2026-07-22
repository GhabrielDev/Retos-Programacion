import random as rd
ganancia_aletoria = [0.03,0.010,0.50]
ege = int(input("Ingrese su edad: "))
capital_inversion = float(input("Ingrese su capital inicial: "))
eleccion = rd.choice(ganancia_aletoria)

if ege >= 18 and capital_inversion >= 50:
    total_ganado = eleccion * capital_inversion
    print("inversion hecha con exito")
    print(f"Tu retorno es de {total_ganado}$ con exito")
else:
    print("No cumples con los requisitos de inversion")