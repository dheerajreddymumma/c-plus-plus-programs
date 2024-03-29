'''
JNEXT - Just Next !!!
#ad-hoc-1
DevG likes too much fun to do with numbers. Once his friend Arya came and gave him a challenge, he gave DevG an array of digits which is forming a number currently (will be called as given number). DevG was challanged to find the just next greater number which can be formed using digits of given number. Now DevG needs your help to find that just next greater number and win the challenge.

Input
The first line have t number of test cases (1 <= t <= 100). In next 2*t lines for each test case first there is number n (1 <= n <= 1000000) which denotes the number of digits in given number and next line contains n digits of given number separated by space.

Output
Print the just next greater number if possible else print -1 in one line for each test case.

Note : There will be no test case which contains zero in starting digits of any given number.

Example
Input:
2
5
1 5 4 8 3
10
1 4 7 4 5 8 4 1 2 6

Output:
15834
1474584162
'''
for _ in range(int(input())):
    L = int(input())
    num = list(map(int, input().split()))
    stack = []    
    stack.append(num[-1])
    flag = 0
    for i in range(L-2, -1,-1):
        if num[i] >= num[i+1]:
            stack.append(num[i])
        else:
            for index, val in enumerate(stack):
                if val > num[i]:
                    temp = stack[index]
                    stack[index] = num[i]
                    num[i] = temp
                    break
            num[i+1:] = stack[:]
            flag = 1
            break
    if flag == 0:
        print(-1)
    else:
        print(''.join(str(x) for x in num))
            


