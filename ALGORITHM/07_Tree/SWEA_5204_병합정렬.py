
def merge_sort(lst):
    global cnt
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left = lst[0:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    result = [0] * (len(right)+len(left))
    idx = len(result)-1
    idx_L = len(left)-1
    idx_R = len(right)-1
    if left[idx_L] > right[idx_R]:
        cnt+=1
    while idx_L >= 0 or idx_R >= 0:
        if idx_L >= 0 and idx_R >= 0:
            if left[idx_L] >= right[idx_R]:
                result[idx] = left[idx_L]
                idx -= 1
                idx_L -= 1
            else:
                result[idx] = right[idx_R]
                idx -= 1
                idx_R -= 1
        elif idx_L >= 0:
            result[idx] = left[idx_L]
            idx -= 1
            idx_L -= 1
        elif idx_R >= 0:
            result[idx] = right[idx_R]
            idx -= 1
            idx_R -= 1

    return result

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    lst = merge_sort(lst)

    print(f'#{tc} {lst[N//2]} {cnt}')