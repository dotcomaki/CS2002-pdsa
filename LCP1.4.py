def expanding(L):
    for i in range(1, len(L) - 1):
        if abs(L[i] - L[i-1]) >= abs(L[i+1] - L[i]):
            return False
    return True
L = eval(input())
print(expanding(L))