class Cachorro:
    
    def __init__(self, nome, idade, cor, secsu, patas = 4):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.secsu = secsu
        self.patas = patas
        self.fome = 0
        self.felicidade = 70                    
        self.sono = 0
        self.saude = 100
        
    def comer(self):
        if self.fome > 0:
            self.fome -= 20
            self.fome = constrain(self.fome, 0, 200)
            print (self.nome + " esta feliz")
        else:
            print (self.nome + " n quer comer")
    
    def update(self):
        global width
        global height
        x = width/2
        y = height/2
        w = 120
        h = w
        fill (self.cor)
        ellipse(x,y,w,h)
        self.fome += 0.005
        fill(30,30,255)
        rect(10,10,200,30)        
        fill(255,0,0)
        rect(10,10,200,30)
        fill(30,30,255)
        rect(10,60,200,30)
        fill(0,255,0)
        rect(10,60,self.fome,30)
caramelo = color(139, 87, 66)            
dog = Cachorro("Atlas" , 6, caramelo, "Macho")

def setup():
    size(600,400)

def draw():
    background(30,30,255)
    dog.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()