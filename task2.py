# a)
s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
s = ('     '.join(s))
print(s.title())

# b)
def clean_names(names):
    cleaned_names = []
    for name in names:
        cleaned_name = ''
        for char in name:
            if char.isalpha():
                cleaned_name += char
        cleaned_names.append(cleaned_name.title())
    return cleaned_names

s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
cleaned_s = clean_names(s)
print(cleaned_s)


