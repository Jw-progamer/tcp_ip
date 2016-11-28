'''
Created on 26 de nov de 2016

@author: tenshi
'''
alfa = 0.125
beta = 0.25

def modulo(numero):
    if numero <= 0 :
        return numero * -1
    else:
        return numero

def rttEstimado(amostra_rtt, rrt_anterior):
    return (1 - alfa) * rrt_anterior + alfa * amostra_rtt

def rttDerivado(derivado_anterior, amostra_rtt, rtt_estimado):
    return (1 - beta) * derivado_anterior + beta * modulo((amostra_rtt - rtt_estimado))

def timeOut(amostra_rtt, estimado_anterior, derivado_anterior , mensagem):
    rtt_estimado = rttEstimado(amostra_rtt, estimado_anterior)
    rtt_derivado = rttDerivado(derivado_anterior, amostra_rtt, rtt_estimado)
    mensagem.rttEstimado = rtt_estimado
    mensagem.rttDerivado = rtt_derivado
    return rtt_estimado + 4 * rtt_derivado