import numpy as np
import random

#int*int->tab[int*tab[int]] avec n : nb etudiants et m: nb masters
def gen_pref_etu(n,m):

    """Utilisation d'une méthode numpy (np.random.rand() et de argsort() ) pour la création d'un tableau de préference aléatoire pour 
    chaque étudiants (on évite les boucles for pour avoir une meilleure complexité sur le programme et sur des cas ou il y a un nombre n ou m assez grand)
    """

    mat_etu = np.random.rand(n,m).argsort(axis=-1) 
    
    print(mat_etu)
    
    return mat_etu

#int*int->tab[int*tab[int]],tab[int] avec n : nb etudiants et m: nb masters
def gen_pref_master(n,m):

    #capacité master (aléatoire)
    cap = np.random.randint(n/m,n/m+1,m) 
    
    while(np.sum(cap)<n): #si division avec reste rajouter les derniers place aléatoirement
        cap[random.randint(0,m-1)] += 1
    
    mat_spe = np.zeros((m,n),dtype=np.int32) #matrice preference masters

    for i in range(len(mat_spe)):
        np.copyto(mat_spe[i],np.random.rand(n).argsort(axis=-1))
    
    return mat_spe,cap
