
for tc in range(1, int(input())+1):
    # N : 숫자개수
    # M : 이동횟수
    N, M = map(int, input().split())
    Q = list(map(int,input().split()))

    for _ in range(M):
        tmp = Q.pop(0)
        Q.append(tmp)

    print('#{} {}'.format(tc,Q[0]))