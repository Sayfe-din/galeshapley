import matplotlib.pyplot as plt

def graph_plot_file(filename):

    f = open(filename,"r")

    lines = f.readlines()
    tab_n = []
    tab_times = []
    tab_sqr_n = []

    for l in lines:

        block = l.split(" ")
        tab_n.append(block[0])
        tab_sqr_n.append(int(block[0])**2)
        tab_times.append(block[2])

    #plot calcul du temps GS
    plt.plot(tab_n,tab_times,'r')
    plt.xlabel('Nombres d\'étudiants')
    plt.ylabel('Temps de calcul(s)')
    plt.suptitle('Temps de calcul de GaleShapley en fonction du nombre d\'étudiant')
    plt.show()

    #plot du temps théorique
    plt.plot(tab_n,tab_sqr_n,'b')
    plt.xlabel('Nombres d\'étudiants')
    plt.ylabel('Temps de calcul(s)')
    plt.suptitle('Temps de calcul de GaleShapley en fonction du nombre d\'étudiant')
    plt.show()

    f.close()

graph_plot_file("temps_calcul_GS.txt")