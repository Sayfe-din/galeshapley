import numpy as np
import sys

def matEtu(name):
	f=open(name,'r')
	lines=f.readlines()
	
	nbetu=int(lines[0])
	mat=np.zeros((nbetu,len(lines[1][:-1].split("\t")[2:])),dtype=np.int32)
	
	for i in range(1,nbetu+1): #parcours
		np.copyto(mat[i-1],list(map(int,lines[i][:-1].split("\t")[2:])))
	f.close()
	#print(mat)
	return mat

def matSpe(name):
	f=open(name,'r')
	lines=f.readlines()
	
	nbetu = int((lines[0].split(" ")[1])[:-1])
	nbspe = len(lines)-2
	mat=np.zeros((nbspe,nbetu),dtype=np.int32)
	
	for i in range(2,nbspe+2): #parcours
		np.copyto(mat[i-2],list(map(int,lines[i][:-1].split("\t")[2:])))
	f.close()
	#print(mat)
	return mat

def recup_cap(name):

	f=open(name,'r')
	f.readline() #lecture 1er ligne
	line = f.readline() #lecture de la ligne contenant les cap
	if("Cap" not in line):
		return np.array([])
	return np.asarray(list(map(int,line[:-1].split(" ")[1:])))

#print(recup_cap("PrefEtu.txt"))
#print(recup_cap("PrefSpe.txt"))
#matEtu("PrefEtu.txt")
#matSpe("PrefSpe.txt")
