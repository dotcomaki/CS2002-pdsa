'''
Goldbach's conjecture is one of the oldest and best-known unsolved problems in number
theory. It states that every even number greater than 2 is the sum of two prime numbers.
Write a function Goldbach(n) where n is a positive even integer greater than 2, that returns a list of tuples.
In each tuple(a,b), a and b are prime numbers such that a+b=n.
'''

#Solution
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def Goldbach(n):
    goldbach = []
    for i in range(2, n//2+1):
        if is_prime(i) and is_prime(n-i):
            goldbach.append((i, n-i))
    return goldbach

#Sample Testcase
n=int(input())
print(sorted(Goldbach(n)))
