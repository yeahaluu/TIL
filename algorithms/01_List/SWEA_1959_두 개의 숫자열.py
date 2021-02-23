import sys
sys.stdin = open('input_두개의숫자열.txt','r')


# 최대값 함수
def my_max(nums):
    max_num = nums[0]
    for num in nums:
        if max_num < num:
            max_num = num
    return max_num


for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    # 긴 것 찾기
    if len(A) > len(B):
        long, short= A, B
        l_len, s_len = N, M
    else:
        long, short = B, A
        l_len, s_len = M, N

    # 결과들을 리스트에 넣어서 그 중 max 찾기
    result = [0] * (l_len-s_len+1)
    # 긴 거 인덱스는 끝에서 짧은거 길이만큼 빼고 1더하기, 짧은거는 짧은거만
    # 긴거는 인덱스는 j+i ####
    for j in range(l_len-s_len+1):
        for i in range(s_len):
            result[j] += long[j+i] * short[i]


    print('#{} {}'.format(tc+1, my_max(result)))