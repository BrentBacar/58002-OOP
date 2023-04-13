class Circle:
    def __init__(self, rad=None, diameter=None):
        if rad:
            self.rad = rad
        elif diameter:
            self.rad = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided")

    def peri(self):
        return 2 * 3.14 * self.rad
    def area(self):
        return 3.14 * self.rad ** 2

r = float(input("Enter the radius of the circle: "))
c = Circle(rad=r)
print("perimeter:", c.peri())
print("area:", c.area())

