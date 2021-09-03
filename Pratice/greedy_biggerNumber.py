# 각 자리가 숫자로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램 - 모든 연산은 왼쪽에서부터 순서대로

# 02984 - 576
# 567 210

# 0이랑 1만 아니면 곱하기가 크다.



S = input()

S_ARRAY = list(S)
temp = 0

for i in S_ARRAY:

  if temp == 0:
    temp = temp + int(i)
    print("plus")
  else:
    if int(i) == 0 or int(i) == 1:
      temp = temp + int(i)

      print(temp)
      print("plus")

    else:
      temp = temp * int(i)
      print("mul")

  



  print(temp)