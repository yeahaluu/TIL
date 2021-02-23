import sys
sys.stdin = open('구간합_input.txt','r')

# 리스트 안의 수 합
def list_sum(nums):
    sum_value = 0
    for num in nums:
        sum_value += num
    return sum_value

# 최소값
def my_min(nums):
    min_num = nums[0]
    for num in nums:
        if min_num > num:
            min_num = num
    return min_num

# 최대값
def my_max(nums):
    max_num = 0
    for num in nums:
        if max_num < num:
            max_num = num
    return max_num

# input
for tc in range(int(input())):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))

    # M개씩 더한 값 넣을 리스트 생성
    result = []

    # 뒤에 수는 더할거니 N-M+1 까지 반복 result에 넣기
    for idx in range(N-M+1):
        sum_value = list_sum(box[idx:idx+M])
        result.append(sum_value)

    # result에서 min과 max 구해서 차 출력
    print('#{} {}'.format(tc+1,my_max(result) - my_min(result)))
