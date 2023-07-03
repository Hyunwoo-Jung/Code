# divmod 함수 활용
# divmod(a,b)
# 결과 : (a // b, a % b)

input_price = input('insert: ')
product_price = input('product: ')
change = int(input_price) - int(product_price)

coin=[5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r, change = divmod(change, i)
    print(str(i) + ': ' + str(r))