#coding: utf-8

from mensagens import Mensageiro

class Cachorro:
    def __init__(self, nome, idade, cor, secsu, notif, patas = 4):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.secsu = secsu
        self.patas = patas
        self.fome = 100
        self.felicidade = 70                    
        self.sono = 0
        self.saude = 100
        self.notif = notif
       
        
    def comer(self):
        if self.fome < 180:
            self.fome += 20
            self.notif.novaMsg(self.nome + ' comeu!')
        else:
            self.notif.novaMsg(self.nome + ' não quer comer')
    
    def update(self):
        global width
        global height
        x = width/2
        y = height/2
        w = 120
        h = w
        fill (self.cor)
        ellipse(x,y,w,h)
        if self.fome > 0:
            self.fome -= 0.005
        fill(90,90,90)
        rect(10,10,200,30)        
        fill(255,0,0)
        rect(10,10,200,30)
        fill(90,90,90)
        rect(10,60,200,30)
        fill(0,255,0)
        rect(10,60,self.fome,30)