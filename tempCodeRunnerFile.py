
def func(lis):
    lis_1 = lis.copy()
    lis_1[1] = lis[1][:-1]
    print(lis_1)
lis = [[2,3,4],[3,4,5]]
func(lis)
print lis