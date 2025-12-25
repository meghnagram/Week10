class Signal():
    def __init__(self,T):
        self.state='red'
        self.v=0
        self.T=T
        
    def sense(self,vden):
        self.v=vden
    
    def update(self):
        if self.v>=self.T:
            self.state='green'
        else:
            self.state='red'
            
            
            
