import sys
sys.stdin = open('input_부분집합의합.txt', 'r')

for tc in range(int(input())):
    n, k = list(map(int, input().split()))

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    count = 0

    # 부분집합 개수만큼 돌리기
    for i in range(1 << 12):  # 2**12 부분 집합의 개수
        lst = []
        sum_num = 0
        for j in range(12 + 1):  # 원소의 수만큼 비트 비교:
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
                #부분집합 만들기
                lst.append(A[j])
                sum_num += A[j]

        #만약 부분집합의 합이 k 길이가 n이면 count +1
        if sum_num == k and len(lst) == n:
            count += 1

    print('#{} {}'.format(tc+1, count))
