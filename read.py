data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count +=1  #count = count + 1
        if count % 100000 ==0:
            print(len(data))
print('檔案讀取完了總共有', len(data), '筆資料')
print(len(data[0]))


#想知道如何只取得第一筆留言的長度
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))




