# O jogo consiste em chegar a finais diferentes das histórias conforme as respostas a determinadas perguntas.
# Objetivo: Descobrir em qual região do Brasil a pessoa mora.

import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você gosta de criar animais? (S/N) ' #Sim = Norte/Nordeste ou Não = Sul/Sudeste
        self.pergunta2 = 'O que gosta de Comer? (Churrasco/Frutos do mar) ' #Frutos do mar = Norte/Nordeste, Churrasco = Sul/Sudeste, 
        self.pergunta3 = 'Prefere o calor ou o frio? (Calor/Frio) ' #calor = Norte/Nordeste, frio = Sul/Sudeste
        self.finaldahistoria1 = 'Você é da região Sul do Brasil!'
        self.finaldahistoria2 = 'Você é da região Norte do Brasil'
        self.finaldahistoria3 = 'Você é da região Nordeste do Brasil'
        self.finaldahistoria4 = 'Você é da região sudeste do Brasil'
    
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Output(size=(30,0))],
            [sg.Input(size=(25,0), key='escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder')]
            ]
        #Criar Janela
        self.janela = sg.Window('Jogo das Regiões!', layout = layout)
        while True:
            #Ler os dados
            self.LerValores()       
            #Utilizar os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)  
                self.LerValores()      
                if self.valores['escolha'] == 'N':
                    print(self.pergunta2)      
                    self.LerValores()       
                    if self.valores['escolha'] == 'Churrasco':
                        print(self.finaldahistoria1)
                    if self.valores['escolha'] == 'Frutos do mar':
                        print(self.finaldahistoria2)
                if self.valores['escolha'] == 'S':
                    print(self.pergunta3)
                    self.LerValores() 
                    if self.valores['escolha'] == 'Calor':
                        print(self.finaldahistoria3)
                    if self.valores['escolha'] == 'Frio':
                        print(self.finaldahistoria4)
            
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()
       