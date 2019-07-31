dict_1 = {}
for _ in range(int(input())):
    num = int(input())
    if num not in dict_1:
        n_fact = int((num - 2) // 2)
        dict_1[num] = int((n_fact * ( n_fact + 1 ) ) // 2)
    print(dict_1[num])
        