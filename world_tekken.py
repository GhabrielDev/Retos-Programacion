#GAME for tekken in Spañish
import random as rd

world = ["Peligro eter","Cervt","Qasderf","Dubayenin"]
Boss =  [ 
   {"Boss":"MEGATRON","DIFICULTY":"facil"},
   {"Boss":"SERPENTI","DIFICULTY":"normal"},
   {"Boss":"Astronworld","DIFICULTY":"dificil"}   
]
enemys = ["perte","mende","borrego"]
damage_list = [2,3,6,10,20,22,76,83,11,34,61,23,43,87,32,50,100]

choice = rd.choice(world)
select = rd.choice(Boss)
damage = rd.choice(damage_list)
print ("** Bienvenido a la Campaña tekken **")
player = input(f"¿Como quieres Llamarte?: ").lower()
yes_no = input(f"{player.capitalize()} estas preparado para la batalla?: ")
print('-' * 40)


if yes_no.lower() == "si":
  print(f"{player} preparate para el Mundo {choice} good luck|Boss final {select['Boss']}|diciculatad {select['DIFICULTY']}\nTe enfrentaras a estos personajes antes de llegar al \njefe final de la mision   ")
  for x in enemys:
    print(f"Enemigos:{x}")
    while True:
          damege = rd.choice(damage_list)
          print(f"1.Golpe | 2.Patada ")
          enemigo = {x}
          seleccion = input("Accion 1/2: ")  
else:
  print(f"Entonces preparate {player}")    
  
