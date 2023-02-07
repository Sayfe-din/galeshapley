import numpy as np

def iftaken_interne(inter,hosp,list_of_taken_hosp,matpref_hosp):
	"""
	inter:numero de l'interne
	hosp:numero de l'hopital
	list_of_taken_hosp: list des hopitaux et des internes qu'ils ont acceptés
	matpref_inter:matrice de preference des hopitaux
	"""
	k=0
	prioofinter=np.where(matpref_hosp[hosp]==inter)[0][0]
	lowest_prio=prioofinter
	lowest_prio_i=-2
	while(list_of_taken_hosp[hosp][k]!=-2):							#Si une place est libre L'etudiant la prendra autrement une recherche sera lancée
		if(list_of_taken_hosp[hosp][k]==-1):
			return (False,True,-1,k)
		if(np.where(matpref_hosp[hosp]==list_of_taken_hosp[hosp][k])[0][0]>prioofinter):	#on initie la recherche de l'etudiant le moins qualifier parmi ceux parcouru dans le sens des preferences des master (matpref_hosp)
			lowest_prio,lowest_prio_i=list_of_taken_hosp[hosp][k],k
			prioofinter=np.where(matpref_hosp[hosp]==list_of_taken_hosp[hosp][k])[0][0]
		k+=1
	if(prioofinter!=lowest_prio):
		return (True,True,lowest_prio,lowest_prio_i)
	return (True,False,-2,0)
			

def interne_GS(matetu,matspe,n,m,cap):
	assert(not np.array_equal(cap,np.array([]))),"Cap est vide"				#array_equal return True if array is same shape

	Tab_interne = np.zeros(n,dtype=np.int32)  						# 1 Si i-eme etudiant a ete accepte 0 sinon
	Tab_hopitaux = np.zeros((m,cap.max()+1),dtype=np.int32)					# indice est le master concerné et la valeur est l'etudiant [len([1])=1,len([4])=1,[5],[1,8]]
	Tab_interne_propositions=np.zeros(n,dtype=np.int32)					# indice: l'etudiant, contenu: le prochain Master a proposer. Si le dernier master a été demander et refuser contenu remis a zero
	
	for i,capi in enumerate(cap):
		Tab_hopitaux[i]=np.add(Tab_hopitaux[i],np.repeat(-2,cap.max()+1))		#-2 Derniere case de chaque sous tableau, cap.max()+1 pour l'équiper au listes ayant pour capacité le maximum de cap
		for k in range(capi):
			Tab_hopitaux[i][k]=-1							#Cases réellement utilisées
	
	while(np.sum(Tab_interne)<n):
	
		for i in range(len(Tab_interne)):
			if(Tab_interne[i] == 0):
				if(Tab_interne_propositions[i]>=m):
					Tab_interne_propositions[i]=0
				taken,cantake,freedstudent,placeinhosp=iftaken_interne(i,matetu[i][Tab_interne_propositions[i]],Tab_hopitaux,matspe)
				Tab_interne_propositions[i]+=1
				
				while(not cantake):
					if(Tab_interne_propositions[i]<m):
						taken,cantake,freedstudent,placeinhosp=iftaken_interne(i,matetu[i][Tab_interne_propositions[i]],Tab_hopitaux,matspe)
					else:
						Tab_interne_propositions[i]=0
						cantake=True
						freedstudent=-2
						
					Tab_interne_propositions[i]+=1
					
				if(not taken):
					Tab_hopitaux[matetu[i][Tab_interne_propositions[i]-1]][placeinhosp]=i
					Tab_interne[i]=1
				if(cantake):
					if(freedstudent>-1):
						Tab_interne[freedstudent]=0
					Tab_hopitaux[matetu[i][Tab_interne_propositions[i]-1]][placeinhosp]=i
					Tab_interne[i]=1
					
	return Tab_hopitaux





def iftaken_hopital(inter,hosp,list_of_taken_hosp,matpref_inter):
	"""
	inter:numero de l'interne
	hosp:numero de l'hopital
	list_of_taken_hosp: list des hopitaux et des internes qu'ils ont acceptés
	matpref_inter:matrice de preference des internes
	"""
	k=0
	crowded=len(np.asarray(list_of_taken_hosp[hosp]==-1).nonzero()[0])-1#test si il n'y aura plus de place si l'etudiant accepte (contenu=place restante apres acceptation)
	#Recherche du Master ayant deja accepté l'étudiant
	while(len(np.asarray(list_of_taken_hosp[k]==inter).nonzero()[0])==0):
		k+=1
		if(k>=len(list_of_taken_hosp)):			#boucle permettant de determiner l'hopital qui perdra l'etudiant si il accepte
			k=-1
			break
	if(k==-1):			#si l'etudiant n'a pas ete trouver dans ce cas là aucune consequence apres l'acceptation
		filled=True
		if(crowded>0):																#supposé fonctionnel
			filled=False
		return (True,-1,-1,filled)
	#Determination des emplacements a liberer et à occuper et ordres de priorité
	prevhosp,positionlost=k,np.asarray(list_of_taken_hosp[k]==inter).nonzero()[0][0]
	prionewhosp=matpref_inter[inter][np.asarray(matpref_inter[inter]==hosp).nonzero()[0][0]]
	priooldhosp=matpref_inter[inter][np.asarray(matpref_inter[inter]==prevhosp).nonzero()[0][0]]
	if(prionewhosp<priooldhosp):
		filled=True
		if(crowded>0):
			filled=False
		return (True,prevhosp,positionlost,filled)
	return (False,-1,-1,False) #(accepted,previoushospital,positionlost,filledhosp)	filled hosp represente le boolean disant si l'hopital faisant la demande sera remplit apres acceptation
			
			
			
			
			
			

def hopital_GS(matspe,matetu,n,m,cap):
	assert(not np.array_equal(cap,np.array([]))),"Cap est vide"				#array_equal return True if array is same shape

	Tab_free_hosp = [e for e in range(m)]						# 1 Si i-eme etudiant a ete accepte 0 sinon
	Tab_hopitaux = np.zeros((m,cap.max()+1),dtype=np.int32)					# indice est le master concerné et la valeur est l'etudiant [len([1])=1,len([4])=1,[5],[1,8]]
	Tab_hop_propositions=np.zeros(m,dtype=np.int32)					# indice: l'hopital, contenu: le prochain etudiant a recruter. Si le dernier etudiant a été demander et a refuser, contenu remis a zero
	
	for i,capi in enumerate(cap):
		Tab_hopitaux[i]=np.add(Tab_hopitaux[i],np.repeat(-2,cap.max()+1))		#-2 Derniere case de chaque sous tableau, cap.max()+1 pour l'équiper au listes ayant pour capacité le maximum de cap
		for k in range(capi):
			Tab_hopitaux[i][k]=-1							#Cases réellement utilisées (Places libres: -1 ---> Numero Etudiant sinon; Fin de Liste: -2  )
	
	while(Tab_free_hosp!=[]):
		hosp=Tab_free_hosp[0]
		if(Tab_hop_propositions[hosp]>=n):
			Tab_hop_propositions[hosp]=0
		currentproposition=matspe[hosp][Tab_hop_propositions[hosp]]
		accepted,prevhosp,positionlost,filled=iftaken_hopital(currentproposition,hosp,Tab_hopitaux,matetu)
		Tab_hop_propositions[hosp]+=1
		while((not accepted) and (Tab_hop_propositions[hosp]<n)):
			currentproposition=matspe[hosp][Tab_hop_propositions[hosp]]
			accepted,prevhosp,positionlost,filled=iftaken_hopital(currentproposition,hosp,Tab_hopitaux,matetu)
			Tab_hop_propositions[hosp]+=1
		if(accepted):
			if(prevhosp>-1):
				Tab_hopitaux[prevhosp][positionlost]=-1
				if(len(np.asarray(Tab_free_hosp==prevhosp).nonzero()[0])!=1):
					Tab_free_hosp.append(prevhosp)
			placeinhosp=np.asarray(Tab_hopitaux[hosp]==-1).nonzero()[0][0]
			Tab_hopitaux[hosp][placeinhosp]=matspe[hosp][Tab_hop_propositions[hosp]-1]
			if(filled):
				Tab_free_hosp.pop(0) #Tab_free_hosp[0]=hosp , comme hosp (master) a rempli ses places -> pop(0)
		else:	
			Tab_hop_propositions[hosp]=0
	return Tab_hopitaux
			


def paires_instables(affectation,matEtu,matSpe):

	paires_instables = []
	
	len_affectation = len(affectation)

	for h1 in range(len_affectation):
		for h2 in range(len_affectation):

			if(not np.array_equal(affectation[h1],affectation[h2])):

				for i1 in affectation[h1]:
					for i2 in affectation[h2]:

						if(i1>=0 and i2>=0):

							if(compare(i1,i2,h1,h2,matEtu,matSpe)):
								paires_instables += [(i1,h2)]


	return np.asarray(paires_instables)


def compare(i1,i2,h1,h2,matEtu,matSpe):

	instable = False

	if((list(matEtu[i1]).index(h2)<list(matEtu[i1]).index(h1)) and (list(matSpe[h2]).index(i1)<list(matSpe[h2]).index(i2))):
		instable = True
	
	return instable
			
			
			
			
			
