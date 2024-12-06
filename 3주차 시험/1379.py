N = int(input())
arr = []
index = []
for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[2], x[1]))

end = arr[0][2]
index.append(arr[0][0])
count = 1
for i in range(1, N):
    if end <= arr[i][1]:
        count += 1
        end = arr[i][2]
        index.append(arr[i][0])
print(count)
print(index)