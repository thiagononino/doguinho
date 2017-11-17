class ui:
    def __init__(self, cachorro):
        self.cachorro = cachorro
        
    def update(self):
        self.barrinha(10, 10, self.cachorro.saude, color(255,0,0))
        self.barrinha(10, 40, self.cachorro.fome, color(0,255,0))
        self.barrinha(10, 70, self.cachorro.felicidade, color(255,255,0))
        self.barrinha(10, 100, self.cachorro.experiencia, color(0,0,255))
    
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
    