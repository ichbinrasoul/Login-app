class Karmand:
    raise_amnt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def get_email(self):
        return f'{self.first}{self.last}@gmail.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)

    def __str__(self):
        return 'Employee is ("{}" , "{}" , {})'.format(self.first, self.last, self.pay)

    def __str__(self):
        return 'Employee is ("{}" , "{}" , {})'.format(self.first, self.last, self.pay)

################################################


class Developer(Karmand):
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

    def __str__(self):
        return 'Developer is ("{}" , "{}" , {})'.format(self.first, self.last, self.pay)

    def __repr__(self):
        return 'Developer is ("{}" , "{}" , {})'.format(self.first, self.last, self.pay)

################################################


class Manager(Karmand):
    def __init__(self, first, last, pay, emps=None):
        super().__init__(first, last, pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def remove_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)

    def print_emp(self):
        for emp in self.emps:
            print('----->', emp.get_email())

    def __str__(self):
        return 'Manager is ("{}" , "{}" , {})'.format(self.first, self.last, self.pay)

    def __repr__(self):
        return 'Manager is ("{}" , "{}" , {})'.format(self.first, self.last, self.pay)


dev1 = Developer('rasoul', 'hejazi', 7000, 'python')
emp1 = Karmand('ali', 'zand', 6200)
emp2 = Karmand('mitra', 'hajjar', 5800)
mng1 = Manager('afsane', 'pakrou', 10000, [dev1])

######################################################

# print(repr(dev1))
# print(str(dev1))
