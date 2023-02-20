from developer import Developer
from manager import Manager
from tester import Tester
from employee_database import EmployeeDatabase

# create developer data
d1 = Developer("Kuldeep", 10000, "Associate Software Engineer")

# print d1 info
print("d1 info before update")
d1.display()

# update d1 info
d1.updateRole("Software Engineer")
d1.updateSalary(15000)
d1.updateName("Kuldeep Shukla")
d1.updateDepartment("R&D")

# print d1 info post update
print("d1 info post update")
d1.display()

# create manager data
m1 = Manager("Abhishek", 15000, "Technical Lead")

# print d1 info
print("m1 info before update")
m1.display()

# update m1 info
m1.updateRole("Senior Technical Lead")
m1.updateSalary(25000)
m1.updateName("Abhishek Singh")
m1.updateDepartment("R&D")

# print m1 info post update
print("m1 info post update")
m1.display()

# create tester data
t1 = Tester("Hari", 12000)

# print t1 info
print("t1 info before update")
t1.display()

# update t1 info
t1.updateRole("Associate Software Tester")
t1.updateSalary(15000)
t1.updateName("Hari Krishna")
t1.updateDepartment("Web App team")

# print t1 info post update
print("t1 info post update")
t1.display()

# create employee database
empDB = EmployeeDatabase()

# add d1, m1 and t1 to employee database
print("Add d1, m1 and t1 to empDB")
empDB.addEmployee(d1)
empDB.addEmployee(m1)
empDB.addEmployee(t1)

# print employee list
print("empDB post adding d1, m1 and t1")
empDB.displayEmployees()