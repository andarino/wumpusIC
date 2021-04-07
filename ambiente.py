
import random

list_pos = [] #Lista vazia de sensações

class Ambiente:
    
    def __init__ (self, tam):
        self.tam = tam

    def imprime(self, matriz):
        l = self.tam
        c = self.tam
        for i in range(l):
            for j in range(c):
                if(j == c - 1):
                    print("[%s],\n" % matriz[i][j], end="")
                else:
                    print("[%s]" % matriz[i][j], end="")
                    print(" ", end="")


    def crie_matriz(self):
        l = self.tam
        c = self.tam
        matriz = []  # lista vazia
        for i in range(l):
            # cria a linha i
            linha = []  # lista vazia
            for j in range(c):
                linha += ['.']
            # coloque linha na matriz
            matriz += [linha]
        return matriz



    def pos_elem(self, A, ob):  # Evitar que gere poço na casa [0,0] (Diego)

        if ob == 'A':
            A[0][0] = ob
        else:
            while 1:
                n1 = random.randrange(len(A))
                n2 = random.randrange(len(A))
                if A[n1][n2] == '.':
                    A[n1][n2] = ob
                    break
                else:
                    continue


    def gen_sensacoes(self, A):  # Tem que arrumar as sensações em Norte (Diego)
        l = self.tam
        c = self.tam
        global list_pos
        list_bril = []
        list_brisa = []
        list_fedor = []
        # agora o programa vai procurar em cada linha e em cada coluna
        for i in range(l):
            for j in range(c):
                if (A[i][j] == 'G'):  # quando o programa achar o ouro (Golden)
                    
                    print(f"ouro em l[{i}] c[{j}]\n", end="")
                    centro = (i, j)
                    brilho = [centro]
                    list_bril = brilho
                    #print("brilho -> ", brilho)
                    # uma lista guarda as posicoes da sensacoes que o wumpus deve ler
                    print("\n\n")

                elif (A[i][j] == 'H'):  # quando o programa achar o buraco (Hole)
                    print(f"buraco em l[{i}] c[{j}]\n", end="")
                    norte = (i+1, j) if i < (l-1) else None
                    sul = (i-1, j) if i > 0 else None
                    leste = (i, j+1) if j < (c-1) else None
                    oeste = (i, j-1) if j > 0 else None
                    brisa = [norte, sul, leste, oeste]
                    list_brisa += [brisa]
                    #print("brisa -> ", brisa)
                    print("\n\n")

                elif (A[i][j] == 'W'):  # quando o programa achar o wumpus
                    print(f"wumpus em l[{i}] c[{j}]\n", end="")
                    norte = (i+1, j) if i < (l-1) else None
                    sul = (i-1, j) if i > 0 else None
                    leste = (i, j+1) if j < (c-1) else None
                    oeste = (i, j-1) if j > 0 else None
                    fedor = [norte, sul, leste, oeste]
                    list_fedor += [fedor]
                    #print("fedor -> ", fedor)
                    print("\n\n")
                    
                elif (A[i][j] == 'A'):  # quando o programa achar o agente
                    print(f"\nagente em l[{i}] c[{j}]\n", end="")
                    print('\n\n')

        list_pos = [list_bril, list_brisa, list_fedor]
    
    def sens_pos(self, pos_ag, tam): #Função para identificar se o Ag está sentindo Brisa, Fedor ou Brilho
        global list_pos
        sen = []
        brisa = []
        fedor = []
        brilho = []

        for i in range(1):
            #print('Casa: ',list_pos[i])
            brilho += list_pos[i]
            for i in range(len(brilho)):
                if (brilho[i] == pos_ag):
                    sen += 'Br'

        for i in range(1, len(list_pos)-1, 1):
            for j in range(tam-1):
                brisa += list_pos[i][j]
                for k in range(len(brisa)):
                    #print('Casa: ', brisa[k])
                    if (brisa[k] == pos_ag):
                        sen += 'B'
                    if(sen == 'B'): break

        for i in range(len(list_pos)-1, len(list_pos), 1):
            for j in range(1):
                fedor += list_pos[i][j]
                for k in range(len(fedor)):
                    #print('Casa: ', fedor[k])
                    if (fedor[k] == pos_ag):
                        sen += 'F'
        return sen