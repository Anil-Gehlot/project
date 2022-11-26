a = int(input("enter first number = "))
b = int(input("enter second number= "))
c = int(input("enter third number = "))

if (a==b==c):
    print(" first,second & third numbers are equal")
elif (a==b and c>a):
    print(" third number is greatest")
elif(a==b and c<a):
    print("first and second number are equals")

elif(a==c and b>a):
    print(" second number is greatest")
elif(a==c and b<a):
    print("first and third numbwe are equals")

elif(b==c and a>b):
    print("first number is greatest")
elif(b==c and a<b):
    print("second and third number are equals")

elif a>b and a>c:
    print("first number is greatest")
elif b>a and b>c:
    print("second number is greatest")
elif c>a and c>b:
    print("third number is greatest")
else:
    print("no one is greatest🤣")
