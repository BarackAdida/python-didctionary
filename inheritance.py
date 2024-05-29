class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.logged_in = False
    
    def log_in(self):
        self.logged_in = True

class Student(User):
    def __init__(self, first, last, cohort):
        super().__init__(first, last)  # Initialize first and last name
        self.cohort = cohort
    
    def log_in(self):
        super().log_in()  # Call the log_in method from User
        self.in_class = True

student_1 = Student("barack", "Adida", "SDFT-FT09")
student_1.log_in()

# Verify the attributes
print(student_1.first)       # Output: barack
print(student_1.last)        # Output: Adida
print(student_1.cohort)      # Output: SDFT-FT09
print(student_1.logged_in)   # Output: True
print(student_1.in_class)    # Output: True
