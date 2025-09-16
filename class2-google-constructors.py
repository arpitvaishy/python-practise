class Google:
    def __init__(self, position, name, salary, net_worth):
        self.position = position #create an instance attribute of position, name etc and assign it with position, name etc.
        self.name = name
        self.salary = salary
        self.net_worth = net_worth
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The {self.position} of Google is {self.name}, his yearly salary is {self.salary}, his net worth is about {self.net_worth}.")
    
a = Google("CEO", "Sundar Pichai", "10,000,000 $", "1.3 Billion $")
a.get_info() # will always print instance attribute whenever present
b = Google("Senior VP", "Philip Schindler", "47 Million $", "111 Million $" )
b.get_info()