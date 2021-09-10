# 한 마을에 모험가가 n명이 있습니다. 모험가 길드에서는 n명의 모험가를 대상으로 '공포도'를 측정했는데, 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.

# 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. n명의 모험가에 대한 정보가 주어졌을때, 여행을 떠날 수 잇는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.

#N = int(input())
#data = list(map(int, input().split()))

N = 5
data = [1,3,2,2,3]
data.sort()

count = 0 #현재 그룹 모험가 수
result = 0

# 1은 1명 2는 2명 3은 3명 4는 4명필요


for i in data:

  count += 1

  if i <= count:

    result += 1
    count = 0



print("Count : "+ str(result))
     

