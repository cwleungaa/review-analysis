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


