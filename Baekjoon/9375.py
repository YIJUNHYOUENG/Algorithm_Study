# Counter를 이용해 같은 부위를 세줌(dict 역할) 
# Counter에 대해 새로 알게되었다.

from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1 

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)