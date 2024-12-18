class Car:
    def car_details(self):
        print("Details of car:")
        print("Company Name:", self.company_name)
        print("Color:", self.color)
        print("Price:", self.price)


car1 = Car()
car1.company_name = "BMW"
car1.color = "White"
car1.price = 100000
car1.car_details()

car2 = Car()
car2.company_name = "Shift"
car2.color = "White"
car2.price = 200000
car2.car_details()

car3 = Car()
car3.company_name = "Benz"
car3.color = "Red"
car3.price = 300000
car3.car_details()
