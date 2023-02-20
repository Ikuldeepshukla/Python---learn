from employee_base import Employee
import random

class Tester(Employee):
    
    def __init__(self, name, salary, role = "Trainee Tester"):
        id = "AK"+str(random.randint(20000,30000))
        super().__init__(id, name, salary)
        super().updateRole(role)
        self.department = "IT"

    def display(self):
        super().display()
        print("Department :", self.department)
        print("------------------------------")

    def updateRole(self, role):
        super().updateRole(role)
    
    def updateSalary(self, salary):
        self.salary = salary

    def updateName(self, name):
        self.name = name
    
    def updateDepartment(self, department):
        self.department = department