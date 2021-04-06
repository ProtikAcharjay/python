numbers=[2,5,4,9,3,4,5,7,8,11]
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[2])
num1=[1,2,5,9,11]
print(num1)
num2=num1
print(num1)
num2.reverse()
print(num1)
print(max(numbers))
print(min(numbers))
numbers.append(100)
print(numbers)
print(max(numbers))
numbers.insert(2, 77)
numbers.remove(11)
numbers.pop()
print(numbers)
numbers[1]=11
print(numbers)
t=(1,2,3)
print(t)

a=2
b=5
"""temp=a
a=b
b=temp"""
a,b= b,a
print(a,b)
