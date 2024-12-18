class Employee:
    company_name = "abcd"
    location = "calicut"
    
    def __init__(self, id, name, salary):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = salary

    def details(self):
        print(self.emp_id, self.emp_name, self.emp_salary)

# Creating Employee objects
emp1 = Employee(101, "Manu", 50000)
emp2 = Employee(102, "Hani", 20000)

# Displaying employee details
emp1.details()
emp2.details()
