import math

def budget_optique(Ptx, Psens, att, dist, n_split, conn, soudures):
    perte_fibre = att * dist
    perte_splitter = 10 * math.log10(n_split)
    pertes_totales = perte_fibre + perte_splitter + conn + soudures
    Prx = Ptx - pertes_totales
    marge = Prx - Psens
    return round(Prx, 2), round(marge, 2)

print(budget_optique(3, -28, 0.35, 20, 32, 1, 0.4))
print(budget_optique(3, -28, 0.35, 20, 64, 1, 0.4))
