'''
Created on 26 de nov de 2016

@author: tenshi
'''

class Mensagem:
    '''
    Representa a mensagem
    '''


    def __init__(self, envio, sequencia, sequencia_ack,info):
        '''
        Constroi o objeto da mensagem.
        '''
        self.envio = envio;
        self.sequencia = sequencia;
        self.ack = sequencia_ack;
        self.timeout= None;
        self.rttEstimado = None;
        self.rttDerivado  = None;
        self.info = info;
        self.chegou = False;
        
    def __str__(self):
        return self.envio + " " + str(self.sequencia)+ " "+ str(self.ack) + " " + str(self.timeout) + " " +str(self.info)