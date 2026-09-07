class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 1 <= age <= 10:
            self._age = age
        else:
            raise ValueError("Tea leaf must between 1 and 10 years")

leaf = TeaLeaf(3)
print(leaf.age)
leaf.age = 12
print(leaf.age)