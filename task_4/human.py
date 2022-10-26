'''
Class "human" with next methods which can accept,get and store values:
    - name
    - gender
    - position
    - salary
'''

class Human:

    # Initializes the atttributes(hiden) of class

    def __init__(self, name, gender, position, salary_per_hour):
        self.name = name
        self.gender = gender
        self.position = position
        self.salary_per_hour = salary_per_hour

    # Set methods for accept the argument

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_position(self, position):
        self.position = position

    def set_salary_per_hour(self, salary_per_hour):
        self.salary_per_hour = salary_per_hour

    # Get methods that return values

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_position(self):
        return self.position

    def get_salary_per_hour(self):
        return self.salary_per_hour

class Employee(Human):
    def __init__(self, name, gender, position, salary_per_hour):

        # Call superclass Human method and pass the require arguments
        Human.__init__(self, name, gender, position, salary_per_hour)

    def wake_up(self):
        print(f"{self.name} wake up")

    def sit_down(self):
        print(f"{self.name} sit down")

    def to_rest(self):
        print(f"{self.name} is going rest")

    def to_work(self):
        print(f"{self.name} go to work")

    def log_time(self, log_time):
        return log_time
