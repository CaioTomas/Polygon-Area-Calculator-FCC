class Rectangle:
    #!object initialized with width and height attributes
    #!methods: set_width, set_height, get_area, get_perimeter, get_diagonal, get_picture, get_amount inside
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
        
        
    def get_perimeter(self):
        return 2*self.width + 2*self.height
        
        
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5
        
        
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            picture = ''
            for i in range(self.height):
                line = ''
                line = line + '*'*self.width
                picture = picture + line + '\n'
            
            return picture
        
    
    def get_amount_inside(self, shape):
        amount = self.get_area()//shape.get_area()
        
        return amount
        

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')' 


class Square(Rectangle):
    #!subclass of Rectangle, set_side method
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def __str__(self):
        return 'Square(side=' + str(self.side) + ')'
    
    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width
        
    def set_height(self, height):
        self.side = height
        self.height = height
        self.width = height