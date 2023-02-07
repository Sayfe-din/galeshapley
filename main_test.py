import numpy as np
from MatPref import *
from galeshapley import *


cap=recup_cap("PrefSpe.txt")
mat_etu=matEtu("PrefEtu.txt")
mat_spe=matSpe("PrefSpe.txt")

#affectation = interne_GS(mat_etu,mat_spe,len(mat_etu),len(mat_spe),cap)

"""
k = affectation[1][0]
z = affectation[4][0]
m = affectation[8][1]

affectation[1][0] = m
affectation[8][1] = z
affectation[4][0] = k
"""

hopi=hopital_GS(mat_spe,mat_etu,len(mat_etu),len(mat_spe),cap)
print(hopi)

#print(affectation)
#print(paires_instables(affectation,mat_etu,mat_spe))