class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self._salary = salary  # Protected attribute (single underscore)

    def display(self):
        print(f"Name: {self.name}, Salary: {self._salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


# Creating an instance of Manager
mgr = Manager("Alice", 80000, "HR")
mgr.display()
