from Employee import Employee
# create 5 employees
employee1 = Employee("John", "Doe", 5000, "Software Developer", 2, 3)
employee2 = Employee("Jane", "Smith", 6000, "Project Manager", 3, 4)
employee3 = Employee("Bob", "Johnson", 4500, "Network Administrator", 1, 1)
employee4 = Employee("Alice", "Lee", 5500, "Database Administrator", 4, 5)
employee5 = Employee("Tom", "Wang", 7000, "Senior Software Developer", 6, 7)

# update an employee's experience age and salary based on the new experience age
employee2.update_experience_age(5)

# print the updated employee information
print(employee2)
print('------------------------------------------------------------------------------------')
print(employee3)
print('------------------------------------------------------------------------------------')
print(employee1)
print('------------------------------------------------------------------------------------')
print(employee5)
print('------------------------------------------------------------------------------------')
print(employee4)


