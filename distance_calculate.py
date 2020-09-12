import math


class Calculate:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculate(self):
        distance = math.sqrt((self.x2 - self.x1) * (self.x2 - self.x1) + (self.y2 - self.y1) * (self.y2 - self.y1))
        return distance


print "--- Distance Calculate From 2 Point ---"
x1 = input("Set X1 :")

x2 = input("Set X2 :")

y1 = input("Set Y1 :")

y2 = input("Set Y2 :")

total = Calculate(x1, x2, y1, y2)
print "Distance = " + str(total.calculate())