class Employee:
    def __init__(self, first, last):
        # print(self)
        self.first = first
        self.last = last
        # self.employer = employer

    def hello(self):
        print(f"hello {self.first} {self.last}")

    @property
    def last(self, last):
        return self._last

    @last.setter
    def last(self, last):
        if type(last) == str:
            self._last = last
        else:
            print("last name must be a string")
            self._last = "N/A"      

    # def get_first(self):
    #     return self._first    
    
    # def set_first(self, first):
    #     if type(first) == str:
    #         self._first = first
    #     else:
    #         print("First name must be a string")
    #         self._first = "N/A"

    # first = property(get_first, set_first)    

emp_1 = Employee("1", "Barack")
emp_2 = Employee("Lapilly", "Pilly")
# emp_3 = Employee("Moringa", "School")

print(emp_1.__dict__)
print(emp_2.__dict__)
# print(emp_3.__dict__)
# emp_1.__init__()