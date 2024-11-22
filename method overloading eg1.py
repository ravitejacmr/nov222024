def addition(a,b):
    c=a+b
    print(c)
def addition(a,b,c):
    d=a+b+c
    print(d)
addition(3,4,5)

def adder(*num ):
    sum=0
    for n in num:
        sum=sum+n
    print("Sum:",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,4,5)