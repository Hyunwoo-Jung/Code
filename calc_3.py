#잘못된 입력에 대응하기

# 오류 발생 시 강제 종료하기 위한 모듈
import sys

# isdecimal -> 문자열 클래스의 매서드, 해당 문자열이 10진수 숫자로만 구성 : True
input_price = input('insert: ')
if not input_price.isdecimal(): 
    print('정수를 입력하세요')
    sys.exit() # 에러가 발생하면 강제종료

product_price = input('product: ')
if not input_price.isdecimal():
    print('정수를 입력하세요')
    sys.exit() # 에러가 발생하면 강제종료

change = int(input_price) - int(product_price)

if change < 0:
    print('금액이 부족합니다')
    sys.exit()

coin=[5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))