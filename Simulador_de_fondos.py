registro_de_meta = []
meta_ahorro = float(input("Cuanto quieres que tener ahorro en tu fondo de emergencia?:"))
sub_total = 0.0

print("Es un objetivo o una meta alcansable")
while True:
  try:
     money = float(input("Cuanto vas ahorrar hoy:$"))
     sub_total+=money
     registro_de_meta.append(money)
     if sub_total >= meta_ahorro:
      break
  except:
     print("Repitelo no ingreses numeros ")
restante =  max(0,meta_ahorro - sub_total)
print("---- Registro de tus ahorros hechos ----")
for registro in registro_de_meta:
    print(f"Ahorros:${registro}")
print(30 * '-')
print(f"Ahorraste:${sub_total} | Faltante:${restante}")
print("Sigue asi que puedes con mas exitos")
    