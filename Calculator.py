a=float(input())
k=input()
c=float(input())

while True :
    if k=="+":
        print(a+c)
        
    elif k=="-":
        print(a-c)
        
    elif k=="*":
        print(a*c)
        
    elif k==0:
        print("Sifira bolunmez!")
        
    else:
        print(a/c)
    break
