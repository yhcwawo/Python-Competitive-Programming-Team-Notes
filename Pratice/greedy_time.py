# 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.

# input 5 -> output 11475

#N = int(input())
#data = list(map(int, input().split()))

n = int(input())
count = 0
data = []

for i in range(n+1):

  for j in range(60):

    for k in range(60):
      data.append(str(i)+"시"+str(j)+"분"+str(k)+"초")


for i in data:

  if '3' in i:
    count = count + 1

print(count)
