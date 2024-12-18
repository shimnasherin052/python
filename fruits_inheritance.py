class Fruits:
    def eat(self):
        print("We can eat fruits")
        
class Orange(Fruits):  # Class name should be capitalized
    pass
    # Uncomment the code below if you want to override the method
    #def eat(self):
    #    print("Orange is a sour fruit")

class Apple(Fruits):
    def eat(self):
        print("Apple is sweet")

# Creating objects
org1 = Orange()
app1 = Apple()

# Calling the eat method
org1.eat()  # Will print "We can eat fruits" since Orange doesn't override eat
app1.eat()  # Will print "Apple is sweet"
