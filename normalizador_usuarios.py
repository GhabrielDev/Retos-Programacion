def mensaje(mensaje):
    while True:
        try:
            texto = input(mensaje).strip()
            if not texto:
                raise ValueError("El texto no puede estar vacio")
            return texto
        except ValueError as e:
            print("Error intente de nuevo")

def arreglar_name(name):
    return name.title()

def arreglar_gmail(gmail):
    return gmail.lower().replace(" ","")

name = mensaje("Ingresa tu Nombre: ")
gmail = mensaje("Ingresa tu gmail: ")


print("----- Datos del Usuario -----")
print(arreglar_gmail(gmail))
print(arreglar_name(name))
print(30 * "-")