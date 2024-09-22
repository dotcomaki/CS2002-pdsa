'''
Write a function named odd_one(L). Except for one element in list L, they are of the same datatype.
The function returns the datatype of the element that is not of the same datatype as the others.
Note:
1. L has at least 3 elements.
2. Elements can only be int, float, str or bool.
3. The function must return one of these datatypes as strings.
4. type(1) == true
'''

# Solution
def odd_one(L):
    type_count = {}
    for item in L:
        item_type = type(item)
        if item_type in type_count:
            type_count[item_type] += 1
        else:
            type_count[item_type] = 1
    
    for item in L:
        if type_count[type(item)] == 1:
            return type(item).__name__
    
# Sample Testcase
print(odd_one(eval(input().strip())))
