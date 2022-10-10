num=int(input("enter a number:"))
s=0
temp=num
while (temp>0):
    x=temp%10
    s=s+(x*x*x)
    temp=temp//10
    
if num==s:
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")