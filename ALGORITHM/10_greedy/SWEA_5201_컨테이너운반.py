for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    W = [int(i) for i in input().split()]  # 무게
    T = [int(i) for i in input().split()]  # 적재용량

    W.sort(reverse=True)
    T.sort(reverse=True)

    # print(W)
    # print(T)

    result = 0
    for w in W:
        for t in T:
            if t>=w:
                result += w
                T.pop(0)
            break

    print(f'#{tc} {result}')
