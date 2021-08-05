class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi i'm {self.name}")


jhon = Person("John Smith")
jhon.talk()

