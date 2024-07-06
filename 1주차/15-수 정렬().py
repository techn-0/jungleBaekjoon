def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    merged += left[left_idx:]
    merged += right[right_idx:]
    
    return merged

# 입력 받기
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

# 병합 정렬 수행
sorted_arr = merge_sort(arr)

# 결과 출력
for num in sorted_arr:
    print(num)
