for _ in range(int(input())):

    X, Y, K, N = map(int,input().split())
    num_pages = X - Y
    flag = 0
    for i in range(N):
        P, C = map(int,input().split())
        if num_pages <= P and K >= C:
            flag = 1
    if flag == 1:
        print("LuckyChef")
    else:
        print("UnluckyChef")