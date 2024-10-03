def shuffle(l1, l2):
    result = []
    len_l1, len_l2 = len(l1), len(l2)
    
    for i in range(min(len_l1, len_l2)):
        result.append(l1[i])
        result.append(l2[i])
    
    if len_l1 > len_l2:
        result.extend(l1[len_l2:])
    elif len_l2 > len_l1:
        result.extend(l2[len_l1:])
    
    return result

L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))