#!/usr/bin/python
def imprime(l, c, matriz):
    for i in range(l):
        for j in range(c):
            if(j == c - 1):
                print("[%s]\n" %matriz[i][j], end = "")
            else:
                print("[%s]" %matriz[i][j], end = "")
                print(" ", end = "")

def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha += [valor]

        # coloque linha na matriz
        matriz += [linha]

    return matriz

def c_cantos(l, c):
    se = [0, 0]  #superior superior esquerdo
    sd = [0, c]  #superior direito
    ie = [l, 0]  #inferior esquerdo
    id = [l, c]  #inferior direito

#-----------------------

def main():
    A = crie_matriz(5,5,0)
    A[0][0] = 'b'
    A[0][1] = 'c'
    A[1][2] = 'x'
    A[1][3] = 'x'
    A[1][4] = 'x'
    imprime(5,5,A)

if __name__ == '__main__':
        main()
