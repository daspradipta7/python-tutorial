class A:
    label = "A"

class B(A):

    label = "B"

class C(A):
    label = "C"

class D(B, C):
    pass

classd = D()
print(classd.label)