habit: list[str] = ["leer","Ser proactivo","Terder tu cama","Ejercicio"]
points = {
    
    'leer':10,
    "Ser proactivo":20,
    "Terder tu cama":6,
    "Ejercicio":30

}
print("----HABITOS BUENOS -----")
for h in habit:
   valor = points[h]
   print(f"{h} su valor es: {valor}")

print('-' * 24)

pregunta = int(input(f"Cuantos habitos haces de estos mostrados en la pantalla: "))

if pregunta >= 2:
    total = ()
    print(f"Eres una persona productiva y proactiva puntos obtenidos: {total}")

else:
    print("Tienes que tener mas habitos buenos")    