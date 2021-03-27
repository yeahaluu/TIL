import sys
sys.stdin = open('input_색칠.txt', 'r')



for tc in range(int(input())):

    # 배경 10*10 만들기
    back = [[0 for _ in range(10)] for _ in range(10)]

    # 각 줄을 입력
    for i in range(int(input())):
        x1, y1, x2, y2, color = map(int, input().split())

        # 만약 빨간색이면 배경에 1 추가. 근데
        if color == 1:
            for x in range(x1 - 1, x2):
                for y in range(y1, y2 + 1):
                    if back[y][x] == 2:
                       back[y][x] = 3
                    else:
                        back[y][x] = 1
        elif color == 2:
            for x in range(x1 - 1, x2):
                for y in range(y1, y2 + 1):
                    if back[y][x] == 1:
                        back[y][x] = 3
                    else:
                        back[y][x] = 2
    count_num = 0
    for i in range(10):
        for j in range(10):
            if back[i][j] == 3:
                count_num += 1
    print('#{} {}'.format(tc + 1, count_num))
