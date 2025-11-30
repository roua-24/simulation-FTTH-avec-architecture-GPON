# Calcul du budget optique GPON
#Paramètres de base
Ptx = 3        # Puissance émise par l'OLT (dBm)
Psens = -28    # Sensibilité du récepteur ONT (dBm)
attenuation_fibre = 0.35  # dB/km
longueur = 20             # km
pertes_connecteurs = 1.0  # dB
pertes_soudures = 0.4     # dB
def budget_optique(split_ratio):   #Fonction de calcul
    pertes_splitter = 10 * __import__('math').log10(split_ratio)
    pertes_totales = (attenuation_fibre * longueur +
                      pertes_connecteurs +
                      pertes_soudures +
                      pertes_splitter)
    Prx = Ptx - pertes_totales
    marge = Prx - Psens

    return {
        "Split": f"1:{split_ratio}",
        "Pertes totales (dB)": round(pertes_totales, 2),
        "Puissance reçue (dBm)": round(Prx, 2),
        "Marge (dB)": round(marge, 2),
        "Statut": "OK" if marge >= 3 else "Limite"
    }
#Calculs pour 1:32 et 1:64
scenarios = [budget_optique(32), budget_optique(64)]
for s in scenarios:
    print(f"\n--- Scénario {s['Split']} ---")
    print(f"Pertes totales : {s['Pertes totales (dB)']} dB")
    print(f"Puissance reçue : {s['Puissance reçue (dBm)']} dBm")
    print(f"Marge : {s['Marge (dB)']} dB")
    print(f"Statut : {s['Statut']}")
