# 文字查詢
#程式碼沒有寫成 def()，所以沒有看起來沒有結構
#字典很適合處理 名字配上次數，如哪個商品最常被購買? 被買了幾次?
#關鍵8行
#這功能還無法處理大小的問題
data = []
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())



wc = {} #word_count     #連兩個for loop 巢狀迴圈
for d in data:    #d是data清單中的每一筆留言 字串，data 是清單 裝有一百萬筆的清單 ，for loop 一筆一筆留言讀取
    words = d.split(' ') #遇到空白鍵就分割  words 是一個清單裝了很多的字
    for word in words:   # 留言中的每一個字叫word，要怎麼把每個字做計數? 要有一個for loop讀取清單的每一個字
        if word in wc: #檢查'字'有沒有出現在字典裡 如果有出現過，現在的值加1 #不在 'not in'
            wc[word] += 1 # wc[word]去字典查找這個所對應的值，會出現值 然後+1
        else:
            wc[word] = 1 # 新增新的key進WC字典,因為沒遇過就把值當作1, key就是現在遇到的這個字word

#print(wc)  #印出來超醜，寫一個for loop 把字典印出來

for word in wc: #把每個key叫出來  
    if wc[word] >1000000: # 超過出現1萬字 才印出來
        print(word, wc[word]) #word 是每一個字典中的key

print(len(wc)) #字典的長度
print(wc['Allen']) # 'Allen' 出現在字典幾次

while True:
    word = input('請問您想查什麼字: ') 
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為', wc[word])
    else:
        print('這個字沒有出現在此字典')
print('感謝您使用本次查詢')
#有可做排序的功能，但不在這次混淆

# ''  字串可以是空的，如遇到連續3個空白鍵'   '，會切3刀
# slpit() 的預設值是空白鍵，如果沒有自己寫split(' ')，就會出現上述切空白鍵的例子，會直接略過


# 註解選很多行，按ctrl + / , 可多行執行