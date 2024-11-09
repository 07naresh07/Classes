class employee:

    amt_raise=1.05

    def __init__(self,first, last, pay):

        self.first=first
        self.last=last
        self.email=first+'_'+last+'@gmail.com'
        self.pay=pay

    def intro_self(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.amt_raise)

class developer(employee):

    def __init__(self,first,last,pay,lang):

        super().__init__(first,last,pay)
        self.lang=lang

class manager(employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        #employee.__init__(first, last, pay)    ANOTHER METHOD TO INITIALIZE THE PARENT CLASS
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_list(self):
        for emp in self.employees:
            print('--> ',emp.intro_self())



obj1=developer('Naresh', 'Dhami', 50000, 'Python')
obj2=developer('Uma', 'Khadayat', 52000, 'C#')

man1=manager('Radha', 'Krishna', 100000, [obj1])

#print(man1.email)

man1.add_emp(obj2)
man1.remove_emp(obj1)
man1.print_list()

#print(issubclass(manager, employee))


#print(obj1.email,obj2.email)
#print(obj1.intro_self())


#print(obj1.lang)
#print(obj2.lang)


