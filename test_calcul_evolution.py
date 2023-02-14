from evolution import *
from galeshapley import *
import time as t

def temps_calcul_GS(filename,m,n_start,n_end,n_step,nb_test):
    
    """
    m = 9 # m : nombre de master
    n_start = 200 #(n_start,n_end) intervalle de variation
    n_end = 2000
    n_step = 200 #n_step : pas de la variation
    nb_test = 10
    """

    f = open(filename,"w")

    for n in range(n_start,n_end+n_step,n_step):
        
        mat_etu = gen_pref_etu(n,m)
        mat_spe,cap = gen_pref_master(n,m)

        moyenne = 0.0

        for i in range(nb_test):

            start_time = t.time()
            interne_GS(mat_etu,mat_spe,n,m,cap)
            end_time = t.time()
            moyenne += (end_time-start_time)
        
        moyenne = moyenne/nb_test 
        
        f.write("%d %d %0.3f\n"%(n,m,moyenne))

    f.close()

temps_calcul_GS("temps_calcul_GS.txt",9,200,2000,200,10)