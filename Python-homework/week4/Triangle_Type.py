a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a == b:
    if b == c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if a == c:
        print("Isosceles")
    else:
        if b == c:
            print("Isosceles")
        else:
            print("Scalene")
