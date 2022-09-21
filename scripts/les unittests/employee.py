# Encapsulation / Information hiding
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return (self.pay * 12)

class Employee:
    # Constructor method with Arguments
    # def __init__(self, firstName, lastName, pay, bonus):
    def __init__(self, **kwargs):
        self.firstname = kwargs['firstName']
        self.lastname = kwargs['lastName']
        self.pay = kwargs['pay']
        self.bonus = kwargs['bonus']
        # Composition
        self.obj_salary = Salary(self.pay)

    def getFullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    # Docstring
    """
    This function calculates and
    returns the annual salary
    """
    @property
    def annualSalary(self):
        return self.obj_salary.get_total() + self.bonus

    def main():
        #  Object
        employee1 = Employee(firstName="Marc", lastName="Rotsaert", pay=6000, bonus=500)
        employee2 = Employee(firstName="Anton", lastName="Diepenhorst", pay=4500, bonus=1000)
        print(f"Annual salary of {employee1.getFullname()} : {employee1.annualSalary}")
        print(f"Annual salary of {employee2.getFullname()} : {employee2.annualSalary}")
        print(f"__name__: {__name__}")

    if __name__ == "main":
        main()

Employee.main()
