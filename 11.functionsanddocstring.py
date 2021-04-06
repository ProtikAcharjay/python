def function1(a,b):
    """this is only work for two number's avg value. Not applicable for three or more numbers"""
    avg=(a+b)/2
    return avg
new_variable= function1(3,7)
print(new_variable)
print(function1.__doc__)