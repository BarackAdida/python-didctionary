class Employee:
    def __init__(self, first, last, employer="N/A"):
        self.first = first
        self._last = last
        self.employer = employer

    def hello(self):
        if isinstance(self.first, int):
            print("First name must be a string")
        else:
            print(f"hello {self.first} {self._last}")

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        if type(last) == str:
            self._last = last
        else:
            print("last name must be a string")
            self._last = "N/A"

# Instances of Employee
emp_1 = Employee("1", "Barack", "White House")
emp_2 = Employee("Lapilly", "Pilly")
emp_3 = Employee("Moringa", "School")

# Calling hello method
emp_1.hello()  # Output: First name must be a string
emp_2.hello()  # Output: hello Lapilly Pilly
emp_3.hello()  # Output: hello Moringa School
