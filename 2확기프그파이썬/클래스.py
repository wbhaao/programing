class People:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def s_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        else:
            return "C"

p1 = People("name", 90)
print(p1.name)
print(p1.s_grade())

class FishCakeMaker:
    def __init__(self, **kwargs):
        self.size=10
        self.flavor="팥"
        self.price = 100

        if "size" in kwargs:
            self.size = kwargs.get("size")
        if "flavor" in kwargs:
            self.flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self.price = kwargs.get("price")