'''
Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive).
The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.
'''
#Solution
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def Twin_Primes(n, m):
    twin_primes = []
    for i in range(n, m+1):
        if is_prime(i) and is_prime(i+2):
            twin_primes.append((i, i+2))
    return twin_primes

#Sample Testcase
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
