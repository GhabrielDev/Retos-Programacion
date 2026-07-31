name = input("Ingresa tu Nombre: ")
gmail = input("Ingresa tu gmail: ")

def arreglar_name(name):
    return name.strip().title().replace(" ","")

def arreglar_gmail(gmail):
    return gmail.lower().replace(" ","")

print("----- Datos del Usuario -----")
print(arreglar_gmail(gmail))
print(arreglar_name(name))
print(30 * "-")