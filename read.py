count = 0
data = [] 
total = 0
with open ('reviews.txt', 'r') as f :
	for line in f :
		count += 1
		data.append(line)
		if count % 100000 == 0:
			print(len(data))

print ('檔案讀完了,共有', len(data), '筆資料')

for d in data :
	total += len(d)

average = total / len(data)

print ('留言的平均長度是 ', average)

data_L = []
data_S = []

for e in data:
	if len(e) <= 100:
		data_S.append(e)
	elif len(e) > 100:
		data_L.append(e)

print('長度少於100字的留言有 ', len(data_S),'筆')

print('長度大於100字的留言有 ', len(data_L),'筆')

good = []
for d in data:
	if 'good' in d:
		good.append(d)

print('一共有',len(good),'筆留言提到good')		

#word count
wd = {}      #word dict
for d in data:
	words = d.split()
	for word in words:
		if word in wd:
			wd[word] += 1
		else:
			wd[word]=1

for word in wd:
	if wd[word] > 10000:
		print(word, wd[word])
print(len(wd))

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wd:
		print(word,'出現了', wd[word] , '次')
	else:
		print('本字典沒有這個字')

print('感謝使用本字典!')
