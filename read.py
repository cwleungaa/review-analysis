count = 0
data = [] 
total = 0
with open ('reviews.txt', 'r') as f :
	for line in f :
		count += 1
		data.append(line)

print (len(data))

for d in data :
	total += len(d)

average = total / len(data)

print ('留言的平均長度是 ', average, '句')


data_L = []
data_S = []

for e in data:
	if len(e) <= 100:
		data_S.append(e)
	elif len(e) > 100:
		data_L.append(e)

print('長度少於100字的留言有 ', len(data_S),'筆')

print('長度大於100字的留言有 ', len(data_L),'筆')