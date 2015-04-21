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
key = csv.reader(open(r'key.csv')) #load the station data and the store place
key.next()
key = [[int(i) for i in y ]for y in key]
keyS = {}
for i in range(len(key)):
    keyS[key[i][0]] = key[i][1]



snow = da.getCollumn(data,13)
rain = da.getCollumn( data,16)
station = da.getCollumn(data,0)
date  = da.getCollumn(data,1)



for i in range ( len ( rain)): # replace the Missing and trace values from the

    if (rain[i] == 'M' or rain[i] == 'T') :
        rain [i] = 0.0
    if (snow[i] == 'M',rain[i] == 'T') :
        snow[i] = 0.0
    rain[i] = float(rain[i])
    snow[i] = float(snow[i])



avgRain = 0
avgSnow = 0
count = 0
i = 0




#while i < len(snow)- 1: # calculate the average rain and snow for 20 stations
#    try:
#        while ( date[i] == date [i+1] ):
#            avgRain = avgRain + rain[i]
#            avgSnow = avgSnow + snow[i]
#
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


weatherImformation = [] # create a data structure with date, rain and snow

#weatherImformation = da.addCollumn(weatherImformation,station)
#weatherImformation = da.addCollumn(weatherImformation,rainDate)
#weatherImformation = da.addCollumn(weatherImformation,rain)
#weatherImformation = da.addCollumn(weatherImformation,snow)

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

#rubbish Code#while i< len(train): # add rain and snow data to the train file
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
print "reached here"
k = 0
# create a dictionary for weather data so as to map the station with store
stationStore ={}
for i in range( len(data)):
    stationStore[str(data[i][1])+str(data[i][0])] = [rain[i],snow[i]]
for i in range( len(train)):
    buff = stationStore[str(train[i][0])+str(keyS[train[i][1]])]
    train[i].append(buff[0])
    train[i].append(buff[1])

#for i in range(len(data)): # adding the weather data according to the station and store relation using keys
#    while(train[y][0] == data[i][1]):
#
#        if(int(keyS[train[y][1]]) == int (data[k][0])) :
#                train[y].append(rain[k])
#                train[y].append(snow[k])
#                y = y + 1
#                print y
#        k = k +1
#    k = 0

print train[0]
for i in range (len(train)): # change the date to a float value

    buff = train[i][0]
    buff = buff[:4] + buff[5:7] + buff[8:]
    train[i][0] = float(buff)


#rubbish code #taking in account the wether it was a weather event or not
#for i in range(len(train)):

#    if (train[i][4] >= 2.0 or train[i][5] >=1.0):
#        x.append(train[i])
#y = da.getCollumn(train,3)

c = 0
for i in range (0,len(train)): # make the x and the output values for testing
    if ( i != len(train) -1 ) :
        if (train[i][0] != train[i+1][0]):
                c = c + 1
    if ( c == 3 ):
        x.append(train[i])
        o.append(train[i][3])
        c = 0
print x[0]
print train[0]
da.delCollumn(x,3)
#train data ready
#______________________________________________________________________________________________

from sklearn.svm import SVR
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor

#svrRbf = SVR(kernel= 'linear', C = 1e3)
#svrRbf.fit(x,o)
clf = DecisionTreeRegressor(max_depth = 2)

#clf = linear_model.LinearRegression()

clf.fit(x,o)
print "complete"
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
for i in range(len(train)):
    dateMap[trainDate[i]] = train [i]
for i in range(len(test)):
    buff = dateMap[test[i][0]]
    test[i].append(buff[3])
    test[i].append(buff[4])




test = [[float(i) for i in y ] for y in test]
print test[0]
#test file ready______________________________________________________________________

#now predict
c = csv.writer(open("submit4.csv","wb"))
c.writerow(['id','units'])
for i in range (len(test)):

    buff = str(testO[i][1]) + "_" + str(testO[i][2]) + "_" + str(testO[i][0])

    c.writerow( [  buff , str(int(max(0,clf.predict(test[i])))) ] )











