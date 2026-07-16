import random as rd
motivacion_dia = [
    "Cada línea de código escrita hoy es un paso más cerca de tu meta."
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día."
    "Sigue con tu programación, así sea un poco, pero sin dejarlo."
]

print(f"Hola soy tu asistente personal como te fue en tu dia?")
frese_del_dia = rd.choice(motivacion_dia)
live = input("Cuentame: ")
with open('Diario_personal.txt','a' ,encoding='utf-8') as archivo:
    archivo.whrite(50 * "=")
    archivo.whrite(f"frase de hoy:{frese_del_dia}\n")
    archivo.write(f"Reporte del dia:{live}\n")
    archivo.whrite(50 * "=")

print('Diario Guardado con exito =)')