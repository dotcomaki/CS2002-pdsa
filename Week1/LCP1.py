def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_product(m):
    if m <= 0:
        return False
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            if is_prime(i) and is_prime(m // i):
                return True
    return False

n = int(input())
print(prime_product(n))