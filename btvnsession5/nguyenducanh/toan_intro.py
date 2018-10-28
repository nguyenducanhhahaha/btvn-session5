a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b**2 - 4*a*c 


if delta > 0:
    print ("phuong trinh co 2 nghiem phan biet")
    x1 = (-b + (delta**0.5))/2*a
    x2 = (-b - (delta**0.5))/2*a
    print (x1)
    print (x2)
elif delta == 0:
    print ("phuong trinh co mot nghiem duy nhat")
    x3 = -b/ 2*a
    print (x3)
else:
    print ("phuong trinh khong co nghiem")