import csv
import math
import numpy as np
import six
import main as da


#Notes : more then 2 inch of snow or more then 1 inch of rain


data =  csv.reader( open( r'weather.csv' ) )
data.next() # this removes the header in the file i.e the first collumn
#data = np.array(data)

data = [[i for i in y] for y in data]


# working with weather_________________________________________________________


#snow = da.getCollumn(data,13)
#rain = da.getCollumn( data,16)
#station = da.getCollumn(data,0)
#date  = da.getCollumn(data,1)
#
#
#
#for i in range ( len ( rain)): # replace the Missing and trace values from the
#
#    if (rain[i] == 'M' or rain[i] == 'T') :
#        rain [i] = 0.0
#    if (snow[i] == 'M',rain[i] == 'T') :
#        snow[i] = 0.0
#    rain[i] = float(rain[i])
#    snow[i] = float(snow[i])
#
#
#
#rainDate = []
#snowDate = []
#realDate = []
#avgRain = 0
#avgSnow = 0
#count = 0
#i = 0
#
#
#
#
#while i < len(snow)- 1: # calculate the average rain and snow for 20 stations
#    try:
#        while ( date[i] == date [i+1] ):
#            avgRain = avgRain + rain[i]
#            avgSnow = avgSnow + snow[i]
#
#            count = count + 1
#            i = i+1
#    except IndexError:
#        print " list index out of range "
#        #print i
#    realDate.append(date[i])
#    i = i + 1
#    rainDate.append(avgRain/count)
#    snowDate.append(avgSnow/count)
#    avgRain = 0
#    avgSnow = 0
#    count = 0
#
#
#weatherImformation = [] # create a data structure with date, rain and snow
#weatherImformation = da.addCollumn(weatherImformation,realDate)
#weatherImformation = da.addCollumn(weatherImformation,rainDate)
#weatherImformation = da.addCollumn(weatherImformation,snowDate)

# weather complete _________________________________________________________________________



#_____________________________________________________________________________________________
# Now the train file

train =  csv.reader( open( r'train.csv' ) )
testO = csv.reader(open(r'test.csv'))

train.next() # this removes the header in the file i.e the first collumn
testO.next()
#data = np.array(data)

train = [[i for i in y] for y in train]
testO  =[[i for i in y ] for y in testO]
test = [[i for i in y ] for y in testO]



i = 0
y = 0
x = []
o = []

#while i< len(train): # add rain and snow data to the train file
#    if ( train[i][0] == weatherImformation[y][0]):
#        train[i].append(snowDate[y])
#        train[i].append(rainDate[y])
#        i = i + 1
#    else :
#        y = y + 1
#



for i in range(len(train)): # change every value in train to float
    for j in range(1,len(train[0])):

        train[i][j] = float(train[i][j])

for i in range (len(train)): # change the date to a float value

    buff = train[i][0]
    buff = buff[:4] + buff[5:7] + buff[8:]
    train[i][0] = float(buff)

#taking in account the wether it was a weather event or not
#for i in range(len(train)):

#    if (train[i][4] >= 2.0 or train[i][5] >=1.0):
#        x.append(train[i])
#y = da.getCollumn(train,3)


for i in range (0,len(train),6): # make the x and the output values for testing
    x.append(train[i])
    o.append(train[i][3])
print x[0]
print train[0]
da.delCollumn(x,3)
#train data ready
#______________________________________________________________________________________________

from sklearn.svm import SVR
from sklearn import linear_model



svrRbf = SVR(kernel= 'linear', C = 1e3)
svrRbf.fit(x,o)

#clf = linear_model.LinearRegression()
#clf.fit(x,o)
j
# prepare the test file ______________________________________________________________________

for i in range (len(test)): # change date to a float value

    buff = test[i][0]
    buff = buff[:4] + buff[5:7] + buff[8:]
    test[i][0] = float(buff)

trainDate = da.getCollumn(train,0)
#for i in range (  len ( test)):
#    j = trainDate.index(test[i][0])
#    test[i].append(train[j][3])
#    test[i].append(train[j][4])
#    print i

dateMap = {}
#for i in range(len(train)):
#    dateMap[trainDate[i]] = train [i]
#for i in range(len(test)):
#    buff = dateMap[train[i][0]]
#    test[i].append(buff[3])
#    test[i].append(buff[4])
#    print i




print'test'
test = [[float(i) for i in y ] for y in test]
#test file ready______________________________________________________________________

#now predict
c = csv.writer(open("submit3.csv","wb"))
c.writerow(['id','units'])
for i in range (len(test)):

    buff = str(testO[i][1]) + "_" + str(testO[i][2]) + "_" + str(testO[i][0])

    c.writerow( [  buff , str(int(clf.predict(test[i]))) ] )










