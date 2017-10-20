#coding: utf-8

from mensagens import Mensageiro
from cachorro import Cachorro
        
caramelo = color(139, 87, 66)            
notif = Mensageiro(0,370)
dog = Cachorro("Karlos" , 10, caramelo, "Macho", notif)
def setup():
    size(600,400)

def draw():
    background(loadImage('paisagem.jpg'))
    dog.update()
    notif.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()