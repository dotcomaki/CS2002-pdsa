from collections import Counter

def histogram(L):
    counts = Counter(L)
    result = [(n, r) for n, r in counts.items()]
    result.sort(key=lambda x: (x[1], x[0]))
    return result
L=eval(input())
print(histogram(L))