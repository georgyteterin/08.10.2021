#a*x^2+b*x+c
a=int(input())
b=int(input())
c=int(input())
D=b*b-4*a*c
if D>0:
    x1=(-b+D**0.5)/(2*a)
    x2=(-b-D**0.5)/(2*a)
    print('x1= ', x1)
    print('x2= ', x2)
elif D==0:
    x1=x2=(-b)/(2*a)
    print(x1)
elif D<0:
    print('no solutions')

