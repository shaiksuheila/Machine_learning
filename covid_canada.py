# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:50:11 2020

@author: Rajesh
"""

#taska 1
import pandas as pd
data = pd.read_csv(r'C:/Users/Ibrahim Shaik/Downloads/public-covid-19-cases-canada.csv')

#task a 2
data.head()
data.shape
data.describe()
data.info()

data.isnull()

(data.isnull()).sum()

(data.isnull()).sum().sum()

data['sex'].value_counts()

data['age'].value_counts()

##two insights are has_travel_history(49832),locally_acquired (50408) has heighest null values
##and more than 90%people not reported their age  and gender

#task b 1
data1=df = data.drop('case_id', 1)
data1.shape
(data1.isnull()).sum()

data2=data1.dropna()
#data2=data1.fillna(0)
data2.shape
(data2.isnull()).sum()

data2['sex'].value_counts()
data2['age'].value_counts()

#data2['age'].replace('Not Reported','None')

data2=data2[data2['sex']!='Not Reported']
data2=data2[data2['age']!='Not Reported']
data2['age'].value_counts()

#taskb 2
data2['age']=data2['age'].replace('<20','0-19')

data2['age']=data2['age'].replace('10-19','0-19')
data2['age']=data2['age'].replace('<10','0-19')
data2['age']=data2['age'].replace('<18','0-19')
data2['age']=data2['age'].replace('<1','0-19')
data2['age'].value_counts()

#task b 3
a=data2.groupby('age').count()
print(a['sex'])

#task c
data2.to_csv('file1.csv')



#3
import pandas as pd
data2=pd.read_csv('file1.csv')
#3a 2b 1
data2["DATE"] = pd.to_datetime(data2['date_report'])
a=data2[data2['DATE'].dt.month==2]
a['sex'].value_counts()
b=a[(a['has_travel_history']=='f') &(a['age']=='60-69') | (a['age']=='50-59')| (a['age']=='60-69')| 
        (a['age']=='70-79')| (a['age']=='80-89')| (a['age']=='90-99')].count()

a=data2[data2['DATE'].dt.month==3]
a['sex'].value_counts()
c=a[(a['has_travel_history']=='f') &(a['age']=='60-69') | (a['age']=='50-59')| (a['age']=='60-69')| 
        (a['age']=='70-79')| (a['age']=='80-89')| (a['age']=='90-99')].count()

a=data2[data2['DATE'].dt.month==4]
a['sex'].value_counts()
d=a[(a['has_travel_history']=='f') &(a['age']=='60-69') | (a['age']=='50-59')| (a['age']=='60-69')| 
        (a['age']=='70-79')| (a['age']=='80-89')| (a['age']=='90-99')].count()
#3a 2b 2
e=[b[0],c[0],d[0]]
e.sort()
e[1:]



#3c 1
def day():
    data2['dayofweek']=data2['DATE'].dt.weekday_name
    #data2['report_week']=data2['DATE'].dt.weekday_name
day()


#3c 2
z=list(data2['date_report'])
x=set(z)
y=[]
w=[]
for i in x:
    y.append(z.count(i))
y.sort()
y=y[-3:]
for i in x:
     if z.count(i)==y[0] or z.count(i)==y[1] or z.count(i)==y[2]:
         print(i)
#3c 3
m=[]
f=[]
m.append(data2[(data2['DATE'].dt.month==2) & (data2['sex']=='Male')].count()[0])
f.append(data2[(data2['DATE'].dt.month==2) & (data2['sex']=='Female')].count()[0])

m.append(data2[(data2['DATE'].dt.month==3) & (data2['sex']=='Male')].count()[0])
f.append(data2[(data2['DATE'].dt.month==3) & (data2['sex']=='Female')].count()[0])

m.append(data2[(data2['DATE'].dt.month==4) & (data2['sex']=='Male')].count()[0])
f.append(data2[(data2['DATE'].dt.month==4) & (data2['sex']=='Female')].count()[0])

import matplotlib.pyplot as plt
plt.plot(['feb','mar','april'],m, label='male')
plt.plot(['feb','mar','april'],f, label='female')
plt.xlabel('month')
plt.ylabel('no of cases')
plt.legend()
plt.show()

##2b 2
k=list(data2['province'].value_counts())
l=data2['province'].value_counts().index
plt.bar(l,k)
plt.xlabel('province')
plt.ylabel('no of cases')
plt.show()

#2b 1
def province():
    a=data2[(data2['DATE'].dt.month==2)]
    print(a['province'].value_counts())
    
    a=data2[(data2['DATE'].dt.month==3)]
    b=a['province'].value_counts()
    print(b[:3])
    
    a=data2[(data2['DATE'].dt.month==4)]
    print(a['province'].value_counts())
province()

#3b 3
data2['province'].value_counts()

m=(data2[(data2['province']=='Ontario') & (data2['sex']=='Male')].count()[0])
f=(data2[(data2['province']=='Ontario') & (data2['sex']=='Female')].count()[0])

import matplotlib.pyplot as plt
plt.bar('male',m,label='male')
plt.bar('female',f, label='female')
plt.xlabel('gender')
plt.ylabel('no of cases')
plt.legend()
plt.show()















