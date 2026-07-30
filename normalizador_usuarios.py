name = input("Ingresa tu Nombre: ")
def arreglar_name(name):
    texto_limpio = name.strip()
    final = texto_limpio.title()
    return final
print(arreglar_name(name))