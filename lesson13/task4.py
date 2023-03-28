alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
def cesar(message, shift):
    message = message.upper()
    itog = ''
    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto + shift
        if i in alfavit:
            itog += alfavit[new_mesto]
        else:
            itog += i
    return itog
slovo = input()
print(cesar(slovo, 3))

