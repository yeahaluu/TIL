import sys

sys.stdin = open('input_GNS.txt', 'r')

for _ in range(int(input())):
    tc, N = input().split()
    arr = list(map(str, input().split()))

    # 다른 행성의 숫자 표시
    other_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # other_number로 되어있는 arr을 우리의 숫자로 바꾸자!
    number_lst = []
    for s in arr:
        for on_idx in range(len(other_number)):
            if s == other_number[on_idx]:
                number_lst.append(on_idx)

    # number_lst 정렬 - 난 카운팅 정렬 써볼거닷
    # count_lst 생성
    count_lst = [0] * (9+1)
    for num in number_lst:
        count_lst[num] += 1

    # 누적합 만들기
    for i in range(9):
        count_lst[i+1] += count_lst[i]

    # sort_lst (정렬 리스트) 만들기
    sort_lst = [-1] * len(number_lst)
    for num in number_lst:
        sort_lst[count_lst[num]-1] = num
        count_lst[num] -= 1

    # 다시 우리 숫자를 other_number로 바꾸자
    result = []
    for i in sort_lst:
        for on_idx in range(len(other_number)):
            if i == on_idx:
                result.append(other_number[on_idx])
    print('{} '.format(tc),end='')
    print(*result)