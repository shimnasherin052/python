class circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        print("Area of circle:", self.pi * self.radius * self.radius)

class rectangle:
    def __init__(self, length, width):  # Fixed the missing underscore
        self.length = length
        self.width = width
        
    def calculate_area(self):
        print("Area of rectangle:", self.length * self.width)

def area(shape):
    shape.calculate_area()

# Create instances
cir = circle(2)
rect = rectangle(10, 3)

# Calculate and print areas
area(cir)
area(rect)
