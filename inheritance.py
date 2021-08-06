class Mamal:
    def walk(self):
        print("walk")


class Dog(Mamal):
    def bark(self):
        print("bark")

class Cat (Mamal):
    def purr(self):
        print("purr")


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
cat1.purr()