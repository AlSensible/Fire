import csv
import random
l=[]
with open('answer.csv','rb') as myFiler:
	lines=csv.reader(myFiler)
	for line in lines:
		l.append(line)
l.remove(l[0])
i = 0
while (i < 1000):
	j = random.randint(0,220244)
	if l[j][1] == 0:
		l[j][1] = 1
	else:
		l[j][1] = 0
	i = i + 1

print l
with open('result.csv','wb') as myFilew:
	myWriter=csv.writer(myFilew)
	for k in l:
		myWriter.writerow(k)