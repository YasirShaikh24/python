def maxThree(x,y,z):
    if x>y:
        if x>z:
            return x
    elif y>x:
        if y>z:
            return y
    else:
        return z
n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
n3=int(input('Enter third number:'))
m=maxThree(n1,n2,n3)
print('Maximum of three number is:',m)