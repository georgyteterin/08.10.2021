from random import randint
n=int(input())
k=int(input())
right =(randint(1, n))
while k>0:
    answer =int(input())
    if answer > right:
        print ('right answer < your answer. k = ', k-1)
    elif answer < right:
        print ('right answer > your answer k = ', k-1)
    elif answer == right:
        print ('congrats!! you won')
        break
    k=k-1
