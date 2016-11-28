'''
Created on 26 de nov de 2016

@author: tenshi
'''
from mensagem import Mensagem
import constantes as f
from random import randint, uniform, random

'''Dados de entrada do problema'''
tam_arquivo = int(input("Digite o tamanho do arquivo: "))
tam_mss = int(input("Digite o tamanho da mensagem: "))
prob_perda = int(input("Digite a probabilidade de perda(entre 0 e 100%): "))
janela = int(input("Digite o tamanho da janela: "))

'''Estas variáveis servem para criar a sequencia dos acks'''
seq_ack = 1
cont_seq_ack = 0

'''gera números aleatórios, e cria as duas listas, remetentes e destinatarios'''
seq_ini = randint(0, 100)
remetentes = []
destinatarios = []

'''O while cria a lista de mensagens do Remetente/cliente'''
while tam_arquivo >= 0:

    if tam_arquivo < tam_mss:
        if tam_arquivo == 0:
            break
        else:
            remetentes.append(Mensagem("Remetente", seq_ini + tam_arquivo, seq_ack, tam_arquivo))
            break
    else:
        remetentes.append(Mensagem("Remetente", seq_ini + tam_arquivo, seq_ack, tam_mss))
    tam_arquivo = tam_arquivo - tam_mss
    cont_seq_ack += 1
    if cont_seq_ack >= janela:
        seq_ack += 1
        cont_seq_ack = 0

'''E aqui se cria o do Destinatario/servidor'''
for i in range(0, len(remetentes) - 1):
    destinatarios.append(Mensagem("Destinatario", remetentes[i].ack, remetentes[i + 1].sequencia, tam_mss))
destinatarios.append(Mensagem("Destinatario", remetentes[len(remetentes) - 1].ack, 0, tam_mss))

'''for m in remetentes:
    print(m)'''

'''for m in destinatarios:
    print(m)'''

janela_destinatario = []
janela_remetente = []


def montar_janelas(lista, lista_janela):
    for m in lista:
        if len(lista_janela) == janela:
            break
        else:
            lista_janela.append(m)


montar_janelas(destinatarios, janela_destinatario)
montar_janelas(remetentes, janela_remetente)

'''print(janela_destinatario)
print(janela_remetente)

for m in janela_remetente:
    print(m)

for m in janela_destinatario:
    print(m)'''

'''amostra_coneccao = uniform(0, 1000)
primeiro = False

lista_perda = []
lista_chegada = []
contador_ack = -1'''


def ultimo_timeout(rrt, mensagem):
    anterio = None
    for i in range(remetentes.index(mensagem) - 1, 0):
        if remetentes[i].chegou:
            anterio = remetentes[i]
            break


    time = 0.0

    if anterio == None:
     time = f.timeOut(rrt, 0.0, 0.0, mensagem)

    else:
     time = f.timeOut((rrt if remetentes.index(mensagem) != 0 else uniform(0.0, 1000)), (
        anterio.rttEstimado if remetentes.index(mensagem) != 0 else 0.0), (
                         anterio.rttDerivado if remetentes.index(
                             mensagem) != 0 else 0.0), mensagem)
    return time


def enviar(janela_remetente, janela_destinatario):
    reenviar = []
    nao_chegou = None
    for m in janela_remetente:
        if prob_perda > randint(0, 101):
            m.chegou = False
        else:
            print(m)
            m.chegou = True
    for m in janela_destinatario:
        par = janela_remetente[janela_destinatario.index(m)]

        if par.chegou:
            print(m) if nao_chegou == None else print(nao_chegou)
            rrt = uniform(0, 1000)
            par.timeout = ultimo_timeout(rrt, par)
            if rrt > par.timeout:
                reenviar.append(par)
            else:
                remetentes.remove(par)
                destinatarios.remove(m)

        else:
            if nao_chegou == None:
                nao_chegou = m
            reenviar.append(par)
    for m in reenviar:
        print(m)
        print(janela_destinatario[janela_remetente.index(m)])
        destinatarios.remove(janela_destinatario[janela_remetente.index(m)])
        remetentes.remove(m)


cont = 1



while destinatarios != [] and remetentes != []:

    cont += 1
    enviar(janela_remetente, janela_destinatario)
    janela_destinatario = []
    janela_remetente = []
    montar_janelas(destinatarios, janela_destinatario)
    montar_janelas(remetentes, janela_remetente)
    '''janela_remetente = []
    janela_destinatario = []
    for m in remetentes:
        if remetentes.index(m) + 1 == len(remetentes):
            janela_remetente.append(m)
        elif m.ack == remetentes[remetentes.index(m) + 1].ack:
            janela_remetente.append(m)

    for m in destinatarios:
        if destinatarios.index(m) + 1 == len(destinatarios):
            janela_destinatario.append(m)
        elif m.sequencia == destinatarios[destinatarios.index(m) + 1]:
            janela_destinatario.append(m)
    janela_remetente.reverse()
    janela_destinatario.reverse()'''
