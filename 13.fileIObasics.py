#file IO basics
"""

"r" - open file for reading - default
"w" - open a file for writing
"x" - creates file if not exsists
"a" - add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write

"""
"""p= open("Protik.txt")
#file=p.read()
#print(file)
for line in p:
    print(line)
p.close()
f=open("Protik.txt","a")
a=f.write("again writing \n",)
b=f.write("dilam kisu akta abr\n")
print(a)
print(b)
f.close()"""

#handel read and write both together
p= open("Protik.txt","r+")
print(p.read())
p.write("Thank you")