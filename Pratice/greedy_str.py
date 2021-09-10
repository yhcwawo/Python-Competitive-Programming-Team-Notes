
# 알파벳 대문자와 숫자 로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.


# K1KA5CB7 -> ABCKK13

data = 'K1KA5CB7'
data = list(data)
data.sort()

count = 0
result = ""

data_set =  data

for i in data:

    if i.isdigit():
      count = count + int(i)


for i in data:
  if i.isdigit():
    pass
  else:
    result = result + str(i)

result = result + str(count)

print(result)
