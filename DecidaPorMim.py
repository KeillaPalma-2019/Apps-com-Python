#Projeto respondendo perguntas aleatoriamente.

import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você pode fazer isso',
            'Não sei, você quem sabe!',
            'Melhor não fazer isso',
            'Acho que está na hora certa',
            'Sim, é isso mesmo'
        ]
    
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Faça uma Pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        #Criar Janela
        self.janela = sg.Window('Decida por mim!', layout = layout)
        while True:
            #Ler os valores
            self.evento, self.valores = self.janela.Read()
            #Utilizar os valores
            if self.evento == 'Decida por mim':
                print(random.choice(self.respostas))                   
                
Decida = DecidaPorMim()
Decida.Iniciar()
