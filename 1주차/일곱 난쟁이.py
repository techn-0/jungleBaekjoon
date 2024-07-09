a = []
for i in range(9):
    a.append(int(input()))
a.sort()
a_sum =  sum(a)
for i in range(9):
    for j in range(i+1, 9):
        if a_sum - a[i] - a[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(a[k])
            exit()