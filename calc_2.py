# 리스트오 반복문으로 프로그램 간단하게 만들기

input_price = input('insert: ')
product_price = input('product: ')
change = int(input_price) - int(product_price)

# 지폐 및 동전 단위를 요소로 설정한 리스트
coin=[5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))