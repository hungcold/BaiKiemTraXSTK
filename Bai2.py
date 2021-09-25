A=[1,1,2,3,5,8,13,21,34,55,88]
B=[1,3,5,4,7,88,66,59,40,54]
for i in A:
    for j in B:
        if(i==j):
            print("Các phần tử trùng nhau là",i)
for i in A:
    for j in B:
        if(j==i):
            A.remove(j)
            B.remove(j)
print("Xóa các phần tử bị trùng nhau",A)
print("Xóa các phần tử bị trùng nhau",B)