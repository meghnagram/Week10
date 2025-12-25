class Vector():
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
    
    def print_info(self):
        print(f"({self.x},{self.y})")
        
    def scale(self,s):
        self.x=self.x*s  
        self.y=self.y*s 
        
    def reflect_about_x(self):
        self.y=-1*self.y
        
    def reflect_about_y(self):
        self.x=-1*self.x 
        
    def add(self,secondvector):
        new_x=self.x+secondvector.x 
        new_y=self.y+secondvector.y
        
        return Vector(new_x,new_y)
        
