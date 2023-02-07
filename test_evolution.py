from evolution import *
from galeshapley import *

def main():

    nb_master = 9
    
    for n in range(200,2000,200):
        
        mat_etu = gen_pref_etu(n,nb_master)
        mat_spe,cap = gen_pref_master(n,nb_master)
        