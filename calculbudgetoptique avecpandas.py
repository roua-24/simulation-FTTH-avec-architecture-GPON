import pandas as pd
import math

def budget_optique(split_ratio):
    pertes_splitter = 10 * math.log10(split_ratio)
    pertes_totales = 0.35 * 20 + 1.0 + 0.4 + pertes_splitter
    Prx = 3 - pertes_totales
    marge = Prx - (-28)
    return [f"1:{split_ratio}", round(pertes_totales, 2), round(Prx, 2), round(marge, 2)]

df = pd.DataFrame(
    [budget_optique(32), budget_optique(64)],
    columns=["Ratio de Split", "Pertes totales (dB)", "Puissance reçue (dBm)", "Marge (dB)"]
)

print(df)
df.to_csv("budget_optique.csv", index=False)

