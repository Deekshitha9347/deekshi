#position argument
def calc(a,b):
    print(a-b)
calc(100,200)
calc(200,100)
#keyword arg
def calc(a,b):
    print(a-b)
calc(a=200,b=100)
calc(b=100,a=200)
#default arg
def calc(a,b,c=1):
    print(a+b+c)
calc(1,3,4)
calc(10,30)
#varlenghth arg
def sum(a,*b):
    print("a:",a,"and b:",b)
sum(10,20) 
sum(10,30,40)
sum(10,20,30,40,50)   
