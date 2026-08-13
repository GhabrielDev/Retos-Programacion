datos= []

money = int(input("Ingresa tu ingreso mensual:$"))

egreso = int(input("Ingresa tus egreso:$"))

datos.append((money,egreso))  

invertir = input("Inviertes? si/no: ")

if invertir == "si":
    sub_total_invercion = int(input("Cuanto inviertes?:$"))
else:
   print("sigamos...")
      
total_semanal = money / 4
total_anual = money * 12

datos.append((money,egreso,total_semanal,total_anual))  

for x in datos:
    print({x})
