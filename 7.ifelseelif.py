print("Enter your age")
age=int(input())
if 18<age<=100:
    print("You can drive")
elif age==18:
    print("Come for verification")
elif 5<=age<18:
    print("You can not drive")
elif 0<age<5:
    print("Grow up fast")
else:
    print("Entered something wrong")