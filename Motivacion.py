import random as rd
import time

print('---- FUTURO MILLONARIO ----')

motivacion = ['si puedes','vamos pa ensima','el proceso','disfruta tu proceso']
obgetivos = ['leer todos los dias asi sea un rato','ser constante con lo que te gusta','ganar tus primeros 50 dolares']

retos = ['']
while True:
  next_go = input('Quieres comenzar tu dia para motivarte? si/no:')
  if next_go.lower() == "si":
     exito = input(f"Como te visualisas: ")
     go =  input(f"{exito},claro que lo puedes lograr con diciplina y \nsiempre con motivacion que dices si comensamos si/no: ")
     print("=" * 60)
     
     if go == 'si':
         print('lo primero que tienes que hacer es ser diciplinado')
         yes_no = input('Eres diplinado si o no?: ') 
    
         if yes_no.lower() == 'si':
             print("=" * 60)
             print("Excelente ya tenemos el 30'%' hecho ")
             print('Ahora tienes que plasmarte una meta')
             meta = input('Tienes alguna me que hacer si o no?: ')
        
    
        
             if meta.lower() == 'si':
                 seleccion = rd.choice(motivacion)
                 objetivo = input(f'Cual es tu meta?: ')
                 print(f'{seleccion}, {objetivo} , tienes que ser constante en eso y se te va a cumplir')
                 print('Good bye')
                 break
             else:
                 print('Cuando no tienes metas.......')
         else: 
            print("=" * 60)
            print('Tienes que ser diciplinado, la primera cosa que\n  tienes que tener es diciplana y\n ser constante y tender tu cama esa es tu primera mision ')
            diciplina = input(f"Te reto pararte todos los dias a la 5am por un mes si lo haces mis respeto,aceptas el reto si o no? no me defraudes: ")
        
            if diciplina.lower() == "si":
                print("Asi me gusta no te rindas,ahora esto es tu proximo reto son estos: ")
                for obgetivo in obgetivos:
                     print(f'Reto: {obgetivos}')
                print('Tienes que cumplir estos retos durante el reto de mes')    
                print('si puedes, si cumples estos retos mis respeto')
                break
        
            else: 
               print("Bueno te voy a dar algo mas sencillo")
               minutos = input(f'Tienes que hacer la regla de 15 minutos en lo que te gusta hacer aceptas?\nsi o no,no te acepto un no: ')
            
               if minutos.lower() == 'si':
                  print('Exelente asi me gusta')
                  print('Sigue adelante')
                  break
               else:
                    print('Hey tienes que tomar accion para hacerte millonario broder  ')    
                    print('No puedes detenerte')
                    break
     else:
         time.sleep(0.7)
         print("hey como que no vamos amigo no puedes\ndecir que no en este momento de tu vida\nte doy un reto y despues vienes")
  else:
     print("-" * 50)
     print(f"Piensalo bien")
     break    

    
