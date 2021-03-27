import sys
sys.stdin = open('min max_input.txt','r')

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
    input()
    box = list(map(int, input().split()))

    # 최대값 - 최소값 출력
    print('#{} {}'.format(tc+1, my_max(box)-my_min(box)))