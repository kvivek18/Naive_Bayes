# K.V.R.K.VIVEK
# Roll No :- 17CS10024
# Machine Learning assignment 2

import numpy as np

import pandas as pd
df=pd.read_csv('data2_19.csv')
testdf=pd.read_csv('test2_19.csv')
features1=df.columns.tolist()
f=[]
ex=[]
test=[]
ex1=df.values.tolist()              # ex1 contains the train data
ex2=testdf.values.tolist()				# ex2 contains the test data
features=[]									
i=0
while i<len(features1):
	f_list=features1[i]					# features1 are the different attributes
	i=i+1
	x=1
i=0
#print (f_list)								# f_list contains the list of features
while i<len(features1):
    features.extend(features1[0].split(','))
    i=i+1	
#print (len(features1)) 
#print (features)
												# features are differenct atrributes comma seperated

for i in ex1:
    ex.append(i[0].split(','))   
for i in ex2:
    test.append(i[0].split(','))

df1=df[str(f_list)].str.split(',')	
#print(df1)

i=0

def increm(val):
	return val+1

i=0
val=0

while i<len(features):
    o=df1.str.get(i).unique().tolist()
    p=[]
    for j in o:
        p.append(j)
    f.append(p)
    i=increm(i)

#print (o)
#print (f)
#print (p)

class Node(object):
    def __init__(self):
        self.value=[]
        self.number=[]
        self.total=[]

class Main(object):
    def __init__(self):
        self.child=[]


i=0


probability=[]
i=-1
while (i+1)<len(f[0]):
    prob = Main()
    i=increm(i)
    j=-1
    while (j+1)<len(features):
        j=increm(j)
        if j==0:
        		continue
        else:
            temp=Node()
            k=0
            while (k)<len(f[j]):
            #for k in range(0,len(f[j])):	
                temp.value.extend(f[j][k])
                b=0
                a=0
                l=0
                while l<len(ex):
                    if ex[l][j]!=f[j][k]:
                    		l=increm(l)
                    		continue
                    else:
                        b=increm(b)
                        if ex[l][0]!=f[0][i]:
                        	 l=increm(l)
                        	 continue
                        else:
                            a=increm(a)
                    l=increm(l)
                temp.number.extend([a])
                temp.total.extend([b])
                k=increm(k)
            prob.child.append(temp)
    probability.append(prob)



def p(list):
	 #print (len(list))	
    a=[]
    begin=0
    end1=len(f[0])
    end2=len(list)
   # print (len(list))
    i=begin
    while (i<end1):
        k=float(1)
        j=begin
        while (j<end2):
            l=f[j].index(list[j])
            num=(probability[i].child[j-1].number[l-1]+1)
            den=(probability[i].child[j-1].total[l-1]+len(features)-1)
            k=k*num/den
            j=increm(j)
        a.extend([(k)])
        i=increm(i)
    return a

y=0
#print (len(test))
for i in test:
    a=p(i)
#    print (a)
    j=a.index(max(a))
    #print (f[0][j]+ " " +i[0])
    if f[0][j]==i[0]:
        x=x+1
        y=y+1
    else:
        y=y+1

def printfunc(fin_ans):
	print (fin_ans)

fin_ans=100-(x/y)*100
printfunc(fin_ans)
