def main():
    
    from agente import Agente
    from ambiente import Ambiente

    tam = 4 #definindo o tamanho para a 
    amb = Ambiente(tam)
    A = amb.crie_matriz()
    'Gerando Agente, Wumpus, Ouro e Poços'
    amb.pos_elem(A, 'A')
    amb.pos_elem(A, 'W')
    amb.pos_elem(A, 'G')
    for i in range(tam-1):
        amb.pos_elem(A, 'H')

    pos_ag = [] #'posicao do agente'
    pos_ag = (0, 0) #'Posição inicial do agente'
    print('Posicao do Ag Inicial\n', pos_ag)

    amb.gen_sensacoes(A)
    amb.imprime(A) #chama a funcao que imprime a matriz
    sen = amb.sens_pos(pos_ag, tam)

    ag = Agente(pos_ag)
    ag.sens(sen)
    


if __name__ == '__main__':
    main()