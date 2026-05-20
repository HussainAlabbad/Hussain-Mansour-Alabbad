Number = int(input("Enter number: "))

if Number < -100:
    print("Negative large")
elif Number < 0:
    print("Negative small")
elif Number == 0:
    print("Zero")
elif Number < 100:
    print("Positive small")
else:
    print("Positive large")
