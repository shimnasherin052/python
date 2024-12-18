class Employee:
    Basic = 0
    TA = 0
    DA = 0
    
    def salary(self):
        # Calculate the salary by adding the Basic, TA, and DA
        print("Salary:", self.Basic + self.TA + self.DA)

# Create an instance of Employee
emp1 = Employee()

# Assigning values to Basic, TA, and DA
emp1.Basic = 20000
emp1.TA = 500
emp1.DA = 4000

# Calling the salary method to print the total salary
emp1.salary()
