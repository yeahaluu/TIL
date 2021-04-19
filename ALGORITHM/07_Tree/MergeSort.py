
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):

    result = [0] * (len(right)+len(left))
    idx = 0
    idx_L = 0
    idx_R = 0
    while idx_L < len(left) or idx_R < len(right):
        if idx_L < len(left) and idx_R < len(right):
            if left[idx_L] <= right[idx_R]:
                result[idx] = left[idx_L]
                idx += 1
                idx_L += 1
            else:
                result[idx] = right[idx_R]
                idx += 1
                idx_R += 1
        elif idx_L < len(left):
            result[idx] = left[idx_L]
            idx += 1
            idx_L += 1
        elif idx_R < len(right):
            result[idx] = right[idx_R]
            idx += 1
            idx_R += 1

    return result

lst = [11, 13,26]
merge_sort(lst)

print(lst)