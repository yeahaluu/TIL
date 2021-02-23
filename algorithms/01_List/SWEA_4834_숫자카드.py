import sys
sys.stdin = open('숫자카드_input.txt','r')

# 최대값 구하는 함수
def my_max(nums):
    max_num = nums[0]
    for num in nums:
        if max_num < num:
            max_num = num
    return max_num

# 최대값의 인덱스 출력 함수
def my_max_idx(nums):
    max_num = nums[0]
    max_idx = 0
    for idx in range(len(nums)):
        if max_num < nums[idx]:
            max_num = nums[idx]
            max_idx = idx
        elif max_num == nums[idx]:
            max_idx = idx
    return max_idx


for tc in range(int(input())):
    N = int(input())
    cards = list(input())

    # 리스트 안에 것 숫자로 어째 바꾸냐... 숫자 잘라서 넣는거 이거밖에 방법이 없나?
    new_cards = []
    for card in cards:
        new_cards.append(int(card))


    # idx = 각 카드의 수 라고 할 때, 몇개 있는지 숫자 세서 넣기
    count = [0] * (my_max(new_cards)+1)
    for idx in range(N):
        count[new_cards[idx]] += 1


    print('#{} {} {}'.format(tc+1, my_max_idx(count), my_max(count)))