# 8x8 좌표 평변상에 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.

# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.


y = [1,2,3,4,5,6,7,8]
x = [1,2,3,4,5,6,7,8]
#'a','b','c','d','e','f','g','h'
count = 0
data_x = 1

data = 'c2'
# data = str(input())
data = list(data)

data_x = ord(data[0]) - int(ord('a'))+1


# x[+2] y[+1]
# x[+2] y[-1]
# x[-2] y[-1]
# x[-2] y[+1]

# y[+2] x[+1]
# y[+2] x[-1]
# y[-2] x[+1]
# y[-2] x[-1]

if int(data[1])+2 in y and data_x+1 in x:
  count += 1


if int(data[1])+2 in y and data_x-1 in x:
  count += 1


if int(data[1])-2 in y and data_x+1 in x:
  count += 1


if int(data[1])-2 in y and data_x-1 in x:
  count += 1

if int(data[1])+1 in y and data_x+2 in x:
  count += 1


if int(data[1])+1 in y and data_x-2 in x:
  count += 1


if int(data[1])-1 in y and data_x+2 in x:
  count += 1


if int(data[1])-1 in y and data_x-2 in x:
  count += 1



print('Count : ' + str(count))  