#labirinto.py

from random import randint

livre = ' '
ocupado = '#'
parede  = '#'

linhas = 7
colunas = 15

inicio = (1,0)
fim = (linhas-2,colunas-1)

def gera_lab(m,n):
	lab = [([parede]*n)]
	for i in range(1,m-1):
		linha = [livre] * n
		for j in range(n):
			if randint(0,7) in [0,1]:
				linha[j] = ocupado
			if j in [0,n-1]:
				linha[j] = parede
		lab.append(linha)
	lab.append([parede]*n)
	lab[inicio[0]][inicio[1]] = livre
	lab[fim[0]][fim[1]] = livre
	return lab

def print_lab(lab):
	for i in lab:
		print("".join(i))

if __name__ == '__main__':
	l = gera_lab(linhas,colunas)
	print_lab(l)