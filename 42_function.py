import math
def area_cir(r):
    area = math.pi * r**2
    circum = 2*math.pi*r
    return area, circum
   
rad = float(input("Enter radius of circle in cm"))
a , c = area_cir(rad)
print("Area is : ", round(a,2) , "Circumference is : ", round(c,2))