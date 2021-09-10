#N = int(input())
#data = list(map(int, input().split()))

# 첫 째줄에 공간의 크기를 나타내는 n이 주어집니다.
# 둘 째줄에 여행가 a가 이동할 계획서 내용이 주어집니다.

# 첫 째줄에 여행가 a가 최종적으로 도착할 지점의 좌표를 공백을 기준으로 구분하여 출력합니다.

N = int(input())
plan = list(map(str, input().split()))

X = []
startX = 1
startY = 1

# 1,1 1,2 1,3 1,4 1,5
# 2,1 2,2 2,3 2,4 2,5

# R j+1
# L j-1
# U i+1
# D i-1

for i in range(N):
  for j in range(N):

    X.append([i+1,j+1])

#print(X)

for p in plan:

  if p == 'R':
    if startY < N:
      startY += 1
  elif p == 'L':
    if startY > 1:
      startY -= 1
  elif p == 'U':
    if startX > 1:
      startX -= 1
  elif p == 'D':
    if startX < N:
      startX += 1
  else: 
    print("This is error")

print(startX, startY)