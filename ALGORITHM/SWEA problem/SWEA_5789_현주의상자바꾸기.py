import sys

sys.stdin = open('input_현주상자.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())

    # 상자 N개 만들기
    boxes = [0] * (N)

    # 각각 범위에 1~Q까지 번호매기기
    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        for j in range(0, N):
            if L <= j + 1 <= R:
                boxes[j] = i

    print('#{} '.format(tc), end='')
    print(*boxes)
