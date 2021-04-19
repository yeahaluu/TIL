arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 10

sel = [0] * N


def powerset(idx):
    # 만약에 idx가 N과 같아지면 print를 하고, return 해야함.
    if idx == N:

        # print 하기
        # arr의 합이 10이 되는 부분집합 만들기!
        tmp = 0
        lst = []
        for i in range(N):
            if sel[i]:
                tmp += arr[i]
                lst.append(arr[i])
        if tmp == 10:
            print(lst)

        # return!
        return

    # 재귀 만들기
    sel[idx] = 0
    powerset(idx + 1)
    sel[idx] = 1
    powerset(idx + 1)


powerset(0)
