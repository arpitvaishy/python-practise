class Company:
    name = "Apple" #   displays yearly compensations of top executive positions at apple; every data is obtained from the internet.
    def ceo(self):
        return "74,600,000 $"
    def finance(self):
        return "1,000,000 $" 
    def counsel(self):
        return "27,000,000 $"
    def seniorvp(self):
        return "10,000,000 $"
    def coo(self):
        return "6,000,000 $"
a = Company()
print(a.ceo())
b = Company()
print(b.finance())
c = Company()
print(c.counsel())
d = Company()
print(d.seniorvp())
e = Company()
print(d.coo())