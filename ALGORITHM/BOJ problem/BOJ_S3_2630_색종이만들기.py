# 종이 자르는 함수 - 잘라서 확인하고 같은색 아니면 다시!
def cut_paper(N, arr):
    global b_count, w_count

    # 만약 한장짜리면 무슨색 종이인지 확인하고 끝
    if N==1:
        if arr[0][0] == 1:
            b_count += 1
        else:
            w_count += 1
        return

    # 여러장 짜리면 4분할 해서 한가지 색으로 구성되었는지 확인
    for i in (0, N//2):
        for j in (0, N//2):

            n = N // 2
            new_arr = [[] for _ in range(N // 2)]

            tmp = 0
            for row in range(i, i+N//2):
                for col in range(j, j+N//2):
                    # 다시 비교해 줄 new_arr만들기
                    if i == N//2:
                        new_arr[row-(N//2)].append(arr[row][col])
                    else:
                        new_arr[row].append(arr[row][col])

                    # 제일 처음과 (arr[i][j])과 다른 것이 발견되면 tmp를 1로 바꿔줘서 한가지 색이 아님을 알려줌
                    if arr[i][j] == 1:
                        if arr[row][col] ==0:
                            tmp = 1
                    else:
                        if arr[row][col] ==1:
                            tmp = 1

            # 한가지 색이 아니면 다시 잘라줌
            if tmp == 1:
                cut_paper(n,new_arr)
            # 한가지 색이면 무슨 색종이인지 확인
            else:
                if arr[i][j] == 1:
                    b_count +=1
                else:
                    w_count += 1


N = int(input())
arr = [[int(i) for i in input().split()] for _ in range(N)]


w_count = 0
b_count = 0
tmp = 0

# 처음 종이가 전부 한가지 색으로 되어있는지 확인
for row in range(N):
    for col in range(N):
        if arr[0][0] == 1:
            if arr[row][col] == 0:
                tmp = 1
        else:
            if arr[row][col] == 1:
                tmp = 1

# 한가지 색이 아니면 종이자르기 함수(cut_paper) 시작
if tmp ==1:
    cut_paper(N, arr)
# 한가지 색이면 무슨 색인지 확인!
else:
    if arr[0][0] == 1:
        b_count += 1
    else:
        w_count += 1

print(w_count)
print(b_count)