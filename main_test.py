import numpy as np
from MatPref import *
from galeshapley import *


cap=recup_cap("PrefSpe.txt")
matetu=matEtu("PrefEtu.txt")
matspe=matSpe("PrefSpe.txt")

#interne_GS(matetu,matspe,len(matetu),len(matspe),cap)
hopi=hopital_GS(matspe,matetu,len(matetu),len(matspe),cap)
print(hopi)
#affectation = [[1,2],[3],[4],[5],[6],[7],[8],[9],[10,11]]
#paires_instables(affectation,matetu,matspe)
