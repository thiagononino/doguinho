from mensagens import Mensageiro
from cachorro import Cachorro
from ui import ui
        
caramelo = color(139, 87, 66) 
           
notif = Mensageiro(0,370)
dog = Cachorro("Karlos" , 10, caramelo, "Macho", notif)
userint = ui(dog)

def setup():
    size(600,400)

def draw():
    background(loadImage('paisagem.jpg'))
    dog.update()
    notif.update()
    userint.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()
def mouseClicked():
    if dog.mouseover():
        dog.carinho()