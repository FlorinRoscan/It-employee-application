class Employee:
    def __init__(self, name, surname, salary, position, seniority, experience_age):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.position = position
        self.seniority = seniority
        self.experience_age = experience_age

    def increase_salary(self):
        if self.seniority < 5:
            self.salary += 300
        else:
            self.salary += 500

    def update_seniority(self, new_seniority):
        self.seniority = new_seniority

    def update_experience_age(self, new_experience_age):
        self.experience_age = new_experience_age
        if self.experience_age < 5:
            self.salary += 300
        else:
            self.salary += 500

    def __str__(self):
        return f"{self.name} {self.surname} ({self.position}) - Seniority: {self.seniority}, Experience Age: {self.experience_age}, Salary: {self.salary}"
