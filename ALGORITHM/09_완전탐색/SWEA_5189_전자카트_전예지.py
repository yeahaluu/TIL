# 제일 앞에 수가 1인 순열
def my_perm(idx, check):
    global s_list
    if idx == N:
        # s는 경로 값 더하기
        s = 0
        for i in range(N-1):
            s += golf_root[sel[i]-1][sel[i+1]-1]
        s += golf_root[sel[N-1]-1][sel[0]-1]

        # s들 저장
        s_list.append(s)
        return

    # 1 고정 나머지 2~N 순열
    for j in range(1, N):
        if check & (1<<j): continue
        sel[idx] = arr[j]
        my_perm(idx+1, check | (1<<j))



for tc in range(1, int(input())+1):
    N = int(input())
    golf_root = [[int(i) for i in input().split()] for _ in range(N)]

    arr = [int(i) for i in range(1, N+1)]
    # print(arr)
    sel = [1] + ([0] * (N-1))  # 1을 고정
    s_list = []  # s 저장

    # 굳이 0부터 해줄 필요가 없어
    my_perm(1, 0)

    print(f'#{tc} {min(s_list)}')
