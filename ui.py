#coding: utf-8

class ui:
    def __init__(self, cachorro):
        self.cachorro = cachorro
        self.comidas = [
                        {'nome':'biscoito', 'valor': 5}
                        {'nome':'pipoca', 'valor': 8}
                        {'nome':'ração', 'valor': 10}
                        {'nome':'banana', 'valor': 5}
                        ]
        
    def update(self):
        self.barrinha(10, 10, self.cachorro.saude, color(255,0,0))
        self.barrinha(10, 40, self.cachorro.fome, color(0,255,0))
        self.barrinha(10, 70, self.cachorro.felicidade, color(255,255,0))
        self.barrinha(10, 100, self.cachorro.experiencia, color(0,0,255))
        
        y = 10
        for comida in self.comidas:
            self.botao(540,y,self.cachorro.comer(),arg = comida.valor, color(0,255,0))
            y += 60
        
    
    def barrinha(self, x, y, qtd, cor):
        tamanho = 200
        grossura = 20
        pre = map(qtd,0,100,0,tamanho)
        
        stroke(30)
        strokeWeight(1)
        fill(90, 90, 90)
        rect(x, y, tamanho, grossura)  
        
        noStroke()      
        fill(cor)
        rect(x, y, pre, grossura)
        
    def botao(self,x,y,callback,cor = color(200,200,255)):
        stroke(30)
        strokeWeight(1)
        fill(cor)
        rect(x,y,50,50)
        dy = mouseY - y
        dx = mouseX - x
        
        if mousePressed:
            if dy >= 0 and dy < 51 and dx >= 0 and dx < 51:
                callback(arg)
    