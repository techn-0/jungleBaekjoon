a = []
for i in range(9):
    a.append(int(input()))  # 사용자로부터 9명의 난쟁이 키를 입력받습니다.

a.sort()  # 입력받은 키들을 정렬합니다.

a_sum = sum(a)  # 리스트 a의 모든 요소의 합을 구합니다.

# 두 명의 키를 제외한 나머지 다섯 명의 키의 합이 100이 되는 경우를 찾습니다.
for i in range(9):
    for j in range(i+1, 9):
        if a_sum - a[i] - a[j] == 100:
            # 결과를 출력합니다. 키가 100이 되는 7명을 찾아서 출력합니다.
            for k in range(9):
                if k != i and k != j:
                    print(a[k])
            # 문제에서는 하나의 유일한 답이 존재하므로, 한 번 찾으면 반복을 종료합니다.
            break
    else:
        continue
    break
