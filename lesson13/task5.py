def countdown(S):
    S.sort(reverse = True)
    for i in range(len(S)):
        print(S[i])
    print("Пуск!")


S = [0, 7, 5, 9, 3, 8, 6, 2, 1]
countdown(S)
