def iterative_factiorial(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)

    return fac
# num=int(input("Enter a number for having factorial"))
# print(iterative_factiorial(num))

def recursive_factiorial(n):
    # fac=1
    # for i in range(n):
    #     fac=fac*(i+1)
    # print("factorial:")
    # return fac

    if n==1:
        return 1
    else:
        return n*recursive_factiorial(n-1)

num=int(input("Enter a number for having factorial"))
print("iterative factorial: ",iterative_factiorial(num))
print("recursive factorial: ",recursive_factiorial(num))