class addition:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def input(self):
        x = int(input("Enter the value of x:"))
        print(x)
        y = int(input("Enter the value of y:"))
        print(y)
        z = x+y
        print("Sum is:")
        print(z)

a=addition()
a.input()
