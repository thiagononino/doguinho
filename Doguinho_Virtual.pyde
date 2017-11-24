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
    
#def keyPressed():
#    if key == ' ':
#        dog.comer(10)

def mouseClicked():
    if dog.mouseover():
        dog.carinho()
#    if dog.mousetop(540, 10):
#        dog.comer(10)
#    if dog.mousetop(540, 70):
#        dog.comer(5)
#    if dog.mousetop(540, 130):
#        dog.comer(2)
#    dog.botao(540,10,dog.comer(10), color(0,255,0))
#    dog.botao(540,70,dog.comer(5), color(100,100,0))
# dog.botao(540,130,dog.comer(2), color(0,100,100))