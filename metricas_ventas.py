
ventas = [45.0, 80.0, 30.0, 60.0]
def calculos_reporte(ventas):

 total_vendido = 0

 for x in ventas:
    total_vendido+=x

 if total_vendido >= 200:
    comision = total_vendido * 0.15
    
 elif total_vendido >= 100:
    comision = total_vendido * 0.10
    
 else:
    comision = total_vendido * 0.05
 print(f"Total vendido:{total_vendido}$|Ganancia venta:{comision}$")   
    
(calculos_reporte(ventas))
    