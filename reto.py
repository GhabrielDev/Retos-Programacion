import pandas as pd

datos = {
    "productos":["nike","Adidas","Jordan"],
    "cantidad":[5,10,None],
    "precio":[12,15,70]
}
df = pd.DataFrame(datos)
df["cantidad"] = df["cantidad"].fillna(0)
