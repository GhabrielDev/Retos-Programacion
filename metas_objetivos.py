metas = []
vision = input(""" ---- Cuaderno Digital ----
                  1.Anotar Meta y objetivo.
                  2.Visualizar exito.
            
                                            """)

decision = int(input('Que quieres hacer?,la opcion 1 o 2?:'))

if decision == "1":
    nueva_hoja = {"METAS":progress,"OBJETIVO":aim}
    progress = input("Cual es tu meta?,Cuentame:")
    aim = input("Cual es tu objetivo para lograrla?:")
    
else:
    print("---- MI CUADERNO DE VISIÓN ----")  
    print(f"Meta:{progress}")
    print(f"Objetivo:{aim}")
    print('-' * 40)
     

