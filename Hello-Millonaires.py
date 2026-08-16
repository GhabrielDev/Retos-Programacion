#hello world and millonaries
def pedir_nombre(mensaje):
   while True: 
     try:
       entrada = input("").strip().title()
       if not entrada:
        raise ValueError("No puede estar vacio")
       return entrada
     except ValueError as e:
        print(f"Se produjo un Error:{e}")

name = pedir_nombre(f"Hi, what your name?:" )
comensar = pedir_nombre("{name} quieres ser millonario?(si/no):" )

if comensar.lower() == "si":
    print(f"Si puedes serlo solo que tienes que creertelo y pensar como ellos y hablar english porque los millonair@s hablan english.")
    print('La cleve del exito es tener constancia')
else:
    print(f"{name} si tienes que ser millonario,\nno digas que no  ")    