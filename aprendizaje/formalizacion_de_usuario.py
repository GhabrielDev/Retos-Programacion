def base_de_datos():
    return []

informacion = base_de_datos()

nombre = input("Nombre:")
edad = float(input(f"Ingrese su edad:"))

if edad >= 18:
    cedula = int(input(f"Ingrese su cedula:"))
    datos = {
        "nombre": nombre,
        "edad": edad,
        "cedula":cedula
    }

    informacion.append(datos)
    print("---- Informacion ----")
    for x in informacion:
        print(f"Nombre:{x['nombre']}|Edad:{x['edad']}|Cedula:{x['cedula']}") 
else:
 print("NO eres Mayor de edad")    