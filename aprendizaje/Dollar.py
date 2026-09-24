#Cambio de dolar a bolivar
while True:
 tsa_bcv = float(input(f"¿En cuanto esta la tasa bcv?: "))
 dollar = float(input(f"¿Cuanto vas a cambiar?: "))

 sub_total = tsa_bcv * dollar

 print(f"tu retiro es de {sub_total:,.2f}bs")
 break