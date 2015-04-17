import csv
import math
import numpy as np
import six
import main as da
from sklearn.svm import SVR


#Notes : more then 2 inch of snow or more then 1 inch of rain


data =  csv.reader( open( r'weather.csv' ) )
data.next() # this removes the header in the file i.e the first collumn
#data = np.array(data)

data = [[i for i in y] for y in data]





snow = da.getCollumn(data,13)
rain = da.getCollumn( data,16)
station = da.getCollumn(data,0)
date  = da.getCollumn(data,1)



for i in range ( len ( rain)):

    if (rain[i] == 'M' or rain[i] == 'T') :
        rain [i] = 0.0
    if (snow[i] == 'M',rain[i] == 'T') :
        snow[i] = 0.0
    rain[i] = float(rain[i])
    snow[i] = float(snow[i])

print rain


rainDate = []
snowDate = []
realDate = []
avgRain = 0
avgSnow = 0
count = 0
i = 0




while i < len(snow)- 1:
    try:
        while ( date[i] == date [i+1] ):
            avgRain = avgRain + rain[i]
            avgSnow = avgSnow + snow[i]

            count = count + 1
            i = i+1
    except IndexError:
        print " list index out of range "
        #print i
    realDate.append(date[i])
    i = i + 1
    rainDate.append(avgRain/count)
    snowDate.append(avgSnow/count)
    avgRain = 0
    avgSnow = 0
    count = 0


weatherImformation = [] # create a data structure with date, rain and snow
weatherImformation = da.addCollumn(weatherImformation,realDate)
weatherImformation = da.addCollumn(weatherImformation,rainDate)
weatherImformation = da.addCollumn(weatherImformation,snowDate)





#_____________________________________________________________________________________________
# Now the train file

train =  csv.reader( open( r'train.csv' ) )
train.next() # this removes the header in the file i.e the first collumn
#data = np.array(data)

train = [[i for i in y] for y in train]



i = 0
y = 0
x = []
while i< len(train):
    if ( train[i][0] == weatherImformation[y][0]):
        train[i].append(snowDate[y])
        train[i].append(rainDate[y])
        i = i + 1
    else :
        y = y + 1

for i in range(len(train)):
    for j in range(1,len(train[0])):

        train[i][j] = float(train[i][j])

for i in range (len(train)):

    buff = train[i][0]
    buff = buff[:4] + buff[5:7] + buff[8:]
    train[i][0] = float(buff)


for i in range(len(train)):

    if (train[i][4] >= 2.0 or train[i][5] >=1.0):
        x.append(train[i])

print len(x)

print len(train)
#train data ready
#______________________________________________________________________________________________

y = da.getCollumn(x,3)
da.delCollumn(x,3)
print len(y)
#svrRbf = SVR(kernel= 'rbf', C = 1e3)
#svrRbf.fit(x,y)


print "complete "
