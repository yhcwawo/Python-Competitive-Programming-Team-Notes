# 1이 될 때까지
# 어떠한 수 n이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 단 두 번째 연산은 n이 k로 나누어 떨어질 때만 선택할 수 있습니다.

# n, k를 공백을 기준으로 구분하여 입력받기

n, k = map(int, input().split())

count = 0

while True:

  if n % k == 0:

    count = count + 1
    n = n / k
    print(n)
    print("this first" + str(count))
  else:

    count = count + 1
    n = n - 1
    print(n)
    print("this second" + str(count))

  if n == 1:
    break

print("result :" + str(count))