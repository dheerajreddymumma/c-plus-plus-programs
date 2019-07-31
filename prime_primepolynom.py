import math
def prime_checker(num):
    if num <= 1:
        return False
    sqrt_number = int(math.sqrt(num))
    for i in range(2,sqrt_number+1):
        if num % i == 0:
            return False
    return True

def method(a,b,c):
    for i in range(0,81):
        value = (i * i * a) + (i * b) + c
        if prime_checker(value) == False:
            return i
    return -1

a = int(input())
b = int(input())
c = int(input())
print(method(a,b,c))

print(7//2)