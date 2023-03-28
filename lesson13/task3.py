def honest(lst):
    return [x for x in lst if x % 2 == 0]
lst = list(range(21))
result = honest(lst)
print(result)
