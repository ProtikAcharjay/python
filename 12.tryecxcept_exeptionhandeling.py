print("enter 1st number")
num1=input()
print("enter 2nd number")
num2=input()
try:
    print("the sum of those number is" ,
          int(num1)+int(num2))
except Exception as e:
    print(e)
print("very important data that we have to show in program must")
