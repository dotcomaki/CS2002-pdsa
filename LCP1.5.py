def sumsquare(L):
    odd_sum = 0
    even_sum = 0
    for num in L:
        if num % 2 == 0:
            even_sum += num ** 2
        else:
            odd_sum += num ** 2
    return [odd_sum, even_sum]
L = eval(input())
print(sumsquare(L))