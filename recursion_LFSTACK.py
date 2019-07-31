import sys
sys.setrecursionlimit(5000)
def rec(N, stacks, seq):
    if seq == []:
        return True
    for i in range(N):
        if len(stacks[i]) > 1 and stacks[i][-1] == seq[0]:
            stacks_copy = stacks.copy()
            stacks_copy[i] = stacks[i][:-1]
            check_bool = rec(N, stacks_copy, seq[1:])
            if check_bool == True:
                return True
    return False

for _ in range(int(input())):
    N = int(input())
    stacks = []
    for i in range(N):
        stacks.append(list(map(int,input().split())))
    seq = list(map(int,input().split()))
    flag = rec(N, stacks, seq)
    if flag == True:
        print('Yes')
    else:
        print('No')
    