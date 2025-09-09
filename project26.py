class circle:

    def __init__(self, r):
        self.r = r

    def perimiter(self):
        print("perimiter = ",r * 2 * 3.14)

    def area(self):
        print("area = ",r * r * 3.14)

r = int(input("what would you like the radius to be : "))

circle_area = circle.area(r)
circle_perimiter = circle.perimiter(r)