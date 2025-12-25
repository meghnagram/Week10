class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y 
        
    def distance(self):
        return (self.x**2+self.y**2)**(.5)
        
    def is_origin(self):
        return ( self.x==0 and self.y==0)
        
    def on_xaxis(self):
        return (self.y==0)
        
    def on_yaxis(self):
        return(self.x==0)
        
    def quadrant(self):
        if self.x>0:
            if self.y>0:
                return 'first'
            else:
                return 'fourth'
        else:
            if self.y>0:
                return 'second'
            else:
                return 'third'
                
    def slope(self):
        return (self.y/self.x)
            
        
