import math
pi = math.pi
radius = int(input("provide the radius of the cylinder in centinmeters: "))
height = int(input("provide the height of the cylinder in centimeters: "))

volume = pi * height * radius**2

print("%.1f" % round(volume,1) + " centimeters cubed")