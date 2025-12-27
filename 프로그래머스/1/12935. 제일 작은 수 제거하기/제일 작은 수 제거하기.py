def solution(arr):
    if len(arr) <= 1:
        return [-1]
    min = arr[0]
    for i in range(1, len(arr)):
        if min > arr[i]:
            min = arr[i]
    arr.remove(min)
    return arr