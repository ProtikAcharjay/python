print("how many rows you want to take?")
row=int(input())
print("Type 1 for soja type 2 for ulta")
num=int(input())
bol= bool(num)
if bol==True:
    for i in range(1,row+1) :
        # for j in range(1,i+1):
        #     print("*", end=" ")
        # print()
        print("*"*int(i))
if bol==False:
    for i in range(row, 0, -1) :
        print("*" * int(i))
