#coding: utf-8
import random
from mensagens import Mensageiro

class Cachorro:
    def __init__(self, nome, idade, cor, secsu, notif, patas = 4):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.secsu = secsu
        self.patas = patas
        self.fome = 50
        self.felicidade = 70                    
        self.sono = 0
        self.saude = 100
        self.notif = notif
        self.experiencia = 0
    
    def carinho(self):
        chance = random.randint(1,10)
        if chance == 1:
            self.notif.novaMsg(self.nome + ' não quer receber carinho!')            
        else:
            self.felicidade += 1
            self.notif.novaMsg(self.nome + ' está mais feliz!')
    def mouseover(self):
        x = width/2
        y = height/2
        d = ((mouseX - x)**2 + (mouseY - y)**2)**(0.5)
        r = 60
        if d < r:
            return True
        else:
            return False
    def mousetop(self, x, y):
        dy = mouseY - y
        dx = mouseX - x
        if dy >= 0 and dy < 51 and dx >= 0 and dx < 51:
            return True
        else:
            return False
    
    def comer(self, food):
        self.fome += food
        self.notif.novaMsg(self.nome + ' comeu!')
        if self.fome > 90:
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
        rect(540, 10, 50, 50)
        fill(255,0,0)
        rect(540, 70, 50, 50)
        fill(0,0,255)
        rect(540, 130, 50, 50)
        
        self.fome -= 0.005
        self.fome = constrain(self.fome, 0, 100)
        self.felicidade -= 0.01
        self.felicidade = constrain(self.felicidade, 0, 100)
        #fill(90,90,90)
        #rect(10,10,200,30)        
        #fill(255,0,0)
        #rect(10,10,self.saude,30)
        #fill(90,90,90)
        #rect(10,60,200,30)
        #fill(0,255,0)
        #rect(10,60,self.fome,30)