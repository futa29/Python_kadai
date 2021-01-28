count=0

for i in range(1,10):
    for j in range(1,10):
        #余り0の値が偶数
        if i*j%2 == 0:
            count+=1
            print(i*j)

#str()で文字列にするのを忘れずに       
print('表示個数'+str(count))    