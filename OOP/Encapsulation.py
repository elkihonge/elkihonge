class Base:

    def __init__(self):
        self.a = "I have rights"
        self.c = "and privileges"


class Derived(Base):
    def __init__(self):
        print(self.a)
        print(self.c)

#create an instance of the parennt class

obj1 = Base()
print(obj1.a)
print(obj1.c)


