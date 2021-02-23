import sys

sys.stdin = open('input_Ladder1.txt', 'r')

for _ in range(10):
    tc = int(input())
    # 100*100  사다리 입력
    ladder = [[int(i) for i in input().split()] for _ in range(100)]

    # 도착점2 = 우리가 시작할 곳
    for i in range(len(ladder[99])):
        if ladder[99][i] == 2:
            start = i  # 2의 x 좌표

    # x, y 좌표 입력 (2의 위치)
    x = start
    y = 99

    # y 가  0보다 클때는 계속 돈다 (y가 0일때: 제일 위에 올라올 때)
    while y > 0:
        # 양 옆에 길이 있으면 옆을 감
        if x > 0 and ladder[y][x - 1] == 1:
            x -= 1
        elif x < 99 and ladder[y][x + 1] == 1:
            x += 1
        # 없으면 위를 감
        else:
            y -= 1
        #왔던 길로 돌아가기 방지
        ladder[y][x] = 0

    print('#{} {}'.format(tc, x))
