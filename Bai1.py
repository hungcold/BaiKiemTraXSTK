list = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
for i in list:
    if i < 30:
        print("Các số nhỏ hơn 30 là:",i)
n = int(input('Nhập vào một số:'))
for j in list:
    if (n < j):
        print("Các số lơn hơn", n, "là:",j)

