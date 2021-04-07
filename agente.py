import random

class Agente:

    def __init__(self, pos_agIn):
        self.pos_agIn = pos_agIn

    def sens(self, sensacao):
        sen = sensacao
        c = 0
        for i in range(len(sen)):
            if (sen[i] == '.'):
                print('\nNao consigo sentir nada\n')
            elif (sen[i] == 'B') and (c == 0):
                print('\nEita frio da mulestia!!\n')
                c = c+1
            elif (sen[i] == 'F'):
                print('\nFuuuuum... Que fedor\n')
            elif (sen[i] == 'Br'):
                print('\nEsta sentindo Brilho\n')
            elif (sen[i] == 'W'):
                print('\nYou are dead!\n')
            elif (sen[i] == 'H'):
                print('\nYou are dead!\n')

    def mov(self, matriz): #movimentação aleatória
        campo = matriz
        ln = random.randrange(1) #escolha aleatória da movimentação (Linha(0)/Coluna(1))
        if ln == 0: #Movimenta horizontalmente
            fv = random.randrange(1)#Escolha aleatória (EmFrente/Volta)
            if fv == 0:#Segue em frente, caso sorteio 0
                campo[self.posicao[0]+1][self.posicao[1]]
            else:#Volta, caso sorteio 1
                campo[self.posicao[0]-1][self.posicao[1]]
        if ln == 1: #Movimenta Verticalmente
            fv = random.randrange(1)#Escolha aleatória (Sobe/Desce)
            if fv == 0:#Sobe, caso sorteio 0
                campo[self.posicao[0]][self.posicao[1]+1]
            else:#Desce, caso sorteio 1
                campo[self.posicao[0]-1][self.posicao[1]-1]
        return campo


    def setPos_agIn(self, pos_agIn):
        self.pos_agIn = pos_agIn

    def getPos_agIn(self):
        return self.pos_agIn

    def setPosicao(self, posicao):
        self.posicao = posicao

    def getPosicao(self):
        return self.posicao