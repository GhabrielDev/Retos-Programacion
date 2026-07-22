print('Bienvenido al mackro')
print('-' * 40)
bcv = float(input(f'Ingrese la tasa del dia: '))
product = input(f'Ingrese el producto: ').lower()
price = float(input(f'Ingrese del precio de la ropa:$ '))
money = float(input(f'Cuanto efectivo vas a dar en dolares:$ '))
print('-' * 40)
if money > price:
    vuelto = money - price
    print(f'Compra exitosa tu vuelto es de {vuelto:.2f}')
    print('Vuelba pronto gracias por comprar')
elif money < price:
    falta = price - money
    por_pagar = falta * bcv
    print(f"Te falta {falta}$ que serian en bolivares a la tasa del dia {por_pagar:,.2f}bs")

    try: 
      pago = float(input(f'Pago:ingrese el monto para finalizar la compra: '))    
      if pago < por_pagar: 
            print(f'Por favor pague el monto exsacto.Pago incompleto')
      else:
         print(f'Pago movil exitoso.Gracias por tu compra')
    except ValueError:
       print('Error puso una letra,por favor arregle eso y coloque numero')  
else:
    print(f"Compra exitosa.Gracias por comprar en makro vuelva pronto")     
print('Chao amigo')      