#Projeto App - Chute o número
#Objetivo: Criar um algoritmo que gera valor aleatório e a pessoa deve adivinhar qual número foi esse, através de dicas do app, até acertar.

import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Seu Chute', size=(39,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))]
        ]
        #Criar uma janela
        self.janela = sg.Window('Chute o Número!',layout = layout)              
        self.GerarNumeroAleatorio()        
        try:  
            while True:     
                #Receber valores
                self.evento, self.valores = self.janela.Read()                 
                #Utilizar os valores      
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:        
                        if int (self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')                            
                            break
                        elif int (self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')                            
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!!')
                            break
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
