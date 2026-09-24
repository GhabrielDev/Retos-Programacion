base_de_datos = []
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

def menu_visual():
    print("""---- SopaBook ----
    1.Iniciar secion.
    2.Registrar.""")


menu_visual()
choice = input("Seleccione 1/2 para avanzar: ")

if choice == "1":
     print("--- Inicie Sesion ----")
     name = mensaje("Ingresa tu Nombre: ")
     gmail = mensaje("Ingresa tu gmail: ")

elif choice == "2":
        ege = int(input("Ingrese su edad: "))
        if ege >= 18:
             name = mensaje("Ingrese su nombre: ")
             gmail = mensaje("Ingrese su Gmail: ")
             password = input("Ingrese una contraseña: ")
             base_de_datos.append((ege,name,gmail,password))
             print("Resgistro finalizado")
             print("---- Informacion del registro ----")
             print(f"Edad:{ege} años")
             print(f"Gmail usado:arreglar_gmail({gmail})")
             print(arreglar_name(name))

        else:
             print("No cumples con la mayoria de edad")    
             
else:
     print("listo manorro2")