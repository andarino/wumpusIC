#!/usr/bin/env python
# coding: utf-8

# In[13]:
import random 

def imprime(l, matriz):
    c = l
    for i in range(l):
        for j in range(c):
            if(j == c - 1):
                print("[%s],\n" %matriz[i][j], end = "")
            else:
                print("[%s]" %matriz[i][j], end = "")
                print(" ", end = "")
    
def crie_matriz(n_linhas):
    n_colunas = n_linhas  
    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha += ['.']
        # coloque linha na matriz
        matriz += [linha]
    return matriz

def num_rand(t):
    return random.randrange(0, t)

def pos_elem(A, ob):
    while 1:
        n1 = num_rand(len(A))
        n2 = num_rand(len(A))
        if A[n1][n2] == '.':
            A[n1][n2] = ob
            break
        else:
            continue
    
def gen_sensacoes(mtz, size):
    #essa e a funcao 
    aux = size #numero de colunas e linhas
    #agora o programa vai procurar em cada linha e em cada coluna 
    for i in range(size):
        for j in range(aux):
            if (mtz[i][j] == 'G'):  #quando o programa achar o ouro (Golden)
                print(f"ouro em l[{i}] c[{j}]\n", end="")
                #Em cada coordenada, uma magia pra não pegar posicoes fora do tabuleiro
                norte = (i, j) if i >= 0 and j >= 0 else None
                sul = (i-1, j) if i-1 >= 0 and j >= 0 else None
                oeste = (i, j+1) if i >= 0 and j+1 >= 0 else None
                leste = (i-1, j)  if i-1 >= 0 and j >= 0 else None
                #uma lista guarda as posicoes da sensacoes que o wumpus deve ler
                brilho = [norte, sul, leste, oeste]
                print("brilho -> ", brilho)
                print("\n\n")
            elif (mtz[i][j] == 'H'):  #quando o programa achar o buraco (Hole)
                print(f"buraco em l[{i}] c[{j}]\n", end="")
                norte = (i, j) if i >= 0 and j >= 0 else None
                sul = (i-1, j) if i-1 >= 0 and j >= 0 else None
                oeste = (i, j+1) if i >= 0 and j+1 >= 0 else None
                leste = (i-1, j)  if i-1 >= 0 and j >= 0 else None
                brisa = [norte, sul, leste, oeste]
                print("brisa -> ", brisa)
                print("\n\n")
            elif (mtz[i][j] == 'W'):  #quando o programa achar o wumpus
                print(f"wumpus em l[{i}] c[{j}]\n", end="")
                norte = (i, j) if i >= 0 and j >= 0 else None
                sul = (i-1, j) if i-1 >= 0 and j >= 0 else None
                oeste = (i, j+1) if i >= 0 and j+1 >= 0 else None 
                leste = (i-1, j)  if i-1 >= 0 and j >= 0 else None
                fedor = [norte, sul, leste, oeste]
                print("fedor -> ", fedor)
                print("\n\n")
    
def main():
    tam = 9 #definindo o tamanho para a matriz
    A = crie_matriz(tam) #funcao retorna a matriz
    pos_elem(A, 'W') #gerando o wumpus
    pos_elem(A, 'G') #gerando o ouro
  
    ###gerando os pocos
    for i in range(tam-1):
        pos_elem(A, 'H')
      
    imprime(tam,A) #chama a funcao que imprime a matriz
    gen_sensacoes(A, tam)
    
if __name__ == '__main__':
        main()

