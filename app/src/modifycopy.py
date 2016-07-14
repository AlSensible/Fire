import csv
import random
l=[]
with open('answer.csv','rb') as myFiler:
	lines=csv.reader(myFiler)
	for line in lines:
		l.append(line)
i = 0
while (i < 100):
	print l[i][1]
	if (l[i][1]):
		l[i][1] = 0
	else:
		l[i][1] = 1
	i = i + 1
with open('result.csv','wb') as myFilew:
	myWriter=csv.writer(myFilew)
	for k in l:
		myWriter.writerow(k)