class employee:
    amt_raise = 1.25
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first+'_'+self.last+'@gmail.com'
        self.pay = pay
    def introduction(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay*self.amt_raise
        return self.pay

class developer(employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language=language

    def lang_out(self):
        return f"I can use {self.language}"

class manager(employee):
    def __init__(self, first, last, pay, empl=None):
        super().__init__(first, last, pay)
        if empl is None:
            self.empl = []
        else:
            self.empl = empl

    def add_emp(self, emp):
        if emp not in self.empl:
            self.empl.append(emp)

    def remove_emp(self, emp):
        if emp in self.empl:
            self.empl.remove(emp)

    def display(self):
        for emp in self.empl:
            print("-->: ",emp.introduction())

obj1 = developer("naresh", "dhami", 20000, "Python")
obj2 = developer("uma", "khadayat", 50000, "C#")
obj3 = manager("sarita", "dhami", 60000, [obj1])
obj3.add_emp(obj2)
obj3.remove_emp(obj1)
obj3.display()