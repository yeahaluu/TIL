for tc in range(1, int(input())+1):
    N = int(input())
    time = []
    for _ in range(N):
        s, e = map(int, input().split())
        time.append((s,e,e-s))

    visited = [0]*25
    result = 0
    for tu in sorted(time, key=lambda x : x[2]):
        s, e, t = tu
        tmp = 0
        for i in range(s + 1, e + 1):
            if i in visited:
                tmp = 1
        if tmp == 0:
            for i in range(s+1, e+1):
                visited[i] = i
            result += 1
    print(f'#{tc} {result}')