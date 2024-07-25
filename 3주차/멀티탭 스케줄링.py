N , K = map(int, input().split())

arr = list(map(int, input().split()))

tap = [0] * N 

count = 0

for i in range(len(arr)):
    if arr[i] in tap:
        continue
    else:
        if 0 in tap:
            tap[tap.index(0)] = arr[i]
        else:
            re = []
            for j in range(i + 1, len(arr)):
                if arr[j] in tap:
                    re.append(arr[j])
            
            if(re):
                ans = list(dict.fromkeys(re))
                for k in range(len(tap)):
                    if tap[k] not in ans:
                        tap[k] = arr[i]
                        count += 1
                        break
            
                else:
                    tap[tap.index(ans[-1])] = arr[i]
                    count += 1
            else:
                tap[0] = arr[i]
                count += 1
print(count)