class family:
    def __init__(self, surname):
        self.surname = surname
class child(family):
    def __init__(self, surname , name):
        super().__init__(surname)
        self.name = name

child = child("gowda", "harshitha")
print(f"{child.name}{child.surname}")