N1 = int(input())
N2 = int(input())

R1 = N1 * (N2%10)
R10 = N1 * ((N2%100)//10)
R100 = N1 * ((N2//100))

print(R1)
print(R10)
print(R100)
print(N1*N2)