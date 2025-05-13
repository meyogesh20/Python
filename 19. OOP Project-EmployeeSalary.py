from abc import ABC, abstractmethod

# -------------------------------
# ABSTRACT CLASS: EMPLOYEE
# -------------------------------
class Employee(ABC):
    def __init__(self, name, base_salary):
        self._name = name                    # Protected attribute
        self._base_salary = base_salary      # Protected attribute

    @abstractmethod
    def calculate_salary(self):
        pass

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if value:
            self._name = value

    # Getter for base_salary
    @property
    def base_salary(self):
        return self._base_salary

    # Setter for base_salary
    @base_salary.setter
    def base_salary(self, value):
        if value >= 0:
            self._base_salary = value

    # Method to get employee details
    def get_details(self):
        return f"Name: {self._name}, Base Salary: ₹{self._base_salary}"


# -------------------------------
# DEVELOPER CLASS
# -------------------------------
class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self._bonus = bonus  # Encapsulated bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if value >= 0:
            self._bonus = value

    def calculate_salary(self):
        return self.base_salary + self._bonus


# -------------------------------
# MANAGER CLASS
# -------------------------------
class Manager(Employee):
    def __init__(self, name, base_salary, incentives):
        super().__init__(name, base_salary)
        self._incentives = incentives  # Encapsulated incentives

    @property
    def incentives(self):
        return self._incentives

    @incentives.setter
    def incentives(self, value):
        if value >= 0:
            self._incentives = value

    def calculate_salary(self):
        return self.base_salary + self._incentives


# -------------------------------
# DISPLAY FUNCTION
# -------------------------------
def display_employee(emp):
    print("\nEmployee Details:")
    print(emp.get_details())
    print(f"Total Salary: ₹{emp.calculate_salary()}\n")


# -------------------------------
# MAIN APPLICATION LOOP
# -------------------------------
def main():
    employees = []

    while True:
        print("=== Employee Payroll System ===")
        print("1. Add Developer")
        print("2. Add Manager")
        print("3. View All Employees")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter Developer Name: ")
            base_salary = float(input("Enter Base Salary: ₹"))
            bonus = float(input("Enter Bonus: ₹"))
            dev = Developer(name, base_salary, bonus)
            employees.append(dev)
            print("✅ Developer added successfully!\n")

        elif choice == '2':
            name = input("Enter Manager Name: ")
            base_salary = float(input("Enter Base Salary: ₹"))
            incentives = float(input("Enter Incentives: ₹"))
            mgr = Manager(name, base_salary, incentives)
            employees.append(mgr)
            print("✅ Manager added successfully!\n")

        elif choice == '3':
            if not employees:
                print("\nNo employees found.\n")
            else:
                for emp in employees:
                    display_employee(emp)

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please enter 1 to 4.\n")


# -------------------------------
# RUN THE PROGRAM
# -------------------------------
if __name__ == "__main__":
    main()
