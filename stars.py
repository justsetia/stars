x=int(input('enter a odd num greater than 5'))
print('*'*x)
m=1
p=x
while x//2-m>-1:
    for i in range((x//(m+1)),(x//(m+1))-m,-1):
        print('*'*i+" "*(p-(i*2))+'*'*i)
        break
    x=x-2
x=p
m=2
while x//2-m>-1:
    for i in range(m,m+1,1):
        print('*'*i+ " "*(x-(i*2))+'*'*i)
        break
    m=m+1
print('*'*x)
    
    