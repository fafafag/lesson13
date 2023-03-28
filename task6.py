# a)
alp = []
def alphabet(alp):
    for i in range(97, 123):
        print(f"{chr(i)}: {i-96}")
alphabet(alp)

# b)
def alphabet():
    d = {}
    for i in range(26):
        d[i+1] = chr(i+97)
    return d
print(alphabet())

