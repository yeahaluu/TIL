import sys
sys.stdin = open('input_의석이.txt', 'r')

for tc in range(int(input())):
    arr = [[s for s in input()] for _ in range(5)]

    _15_lst = [i for i in range(15)]
    lst = []
    for col in _15_lst:
        for row in range(5):
            try:
                lst.append(arr[row][col])
            except:
                pass
    print('#{} {}'.format(tc+1,''.join(lst)))