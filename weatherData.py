import csv
import math
import numpy as np
import six
import main as da
import  sys

#Notes : more then 2 inch of snow or more then 1 inch of rain


data =  csv.reader( open( r'weather.csv' ) )
data.next() # this removes the header in the file i.e the first collumn
#data = np.array(data)

data = [[i for i in y] for y in data]


# working with weather______________________________________________________
key = csv.reader(open(r'key.csv')) #load the station data and the store place
key.next()
key = [[int(i) for i in y ]for y in key]
keyS = {}
for i in range(len(key)):
    keyS[key[i][0]] = key[i][1]



snow = da.getCollumn(data,13)
rain = da.getCollumn( data,14)
station = da.getCollumn(data,0)
date  = da.getCollumn(data,1)

for i in range ( len ( rain)): # replace the Missing and trace values from the

    if (rain[i] == 'M' ):
        rain [i] = 0.0

    if(rain[i] == '  T') :
        rain[i] = 0.01

    if (snow[i] == 'M'):
        snow[i] = 0.0

    if(snow[i] == '  T') :
        snow[i] = 0.1

    rain[i] = float(rain[i])
    snow[i] = float(snow[i])



avgRain = 0
avgSnow = 0
count = 0
i = 0

# weather complete _________________________________________________________

#___________________________________________________________________________
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



for i in range(len(train)): # change every value in train to float
    for j in range(1,len(train[0])):

        train[i][j] = float(train[i][j])
print "reached here"
k = 0
# create a dictionary for weather data so as to map the station with store
# adding weather data according to the station and store relation using keys
#stationStore ={}
#for i in range( len(data)):
#    stationStore[str(data[i][1])+str(data[i][0])] = [rain[i],snow[i]]
#for i in range( len(train)):
#    buff = stationStore[str(train[i][0])+str(keyS[train[i][1]])]
#    train[i].append(buff[0])
#    train[i].append(buff[1])

for i in range (len(train)): # change the date to a float value

    buff = train[i][0]
    buff = buff[:4] + buff[5:7] + buff[8:]
    train[i][0] = float(buff)
# prepare the test file ____________________________________________________

for i in range (len(test)): # change date to a float value

    buff = test[i][0]
    buff = buff[:4] + buff[5:7] + buff[8:]
    test[i][0] = float(buff)

trainDate = da.getCollumn(train,0)
dateMap = {}
for i in range(len(train)): # add the extra weather data according to the date
    dateMap[str(trainDate[i])+str(train[i][1])] = train [i]
buff = []
#for i in range(len(test)):
#    buff = dateMap[str(test[i][0])+str(test[i][1]]
#    test[i].append(buff[3])
#    test[i].append(buff[4])
#    test[i].append(buff[5])
#print buff

test = [[float(i) for i in y ] for y in test]
#test file ready__________________________________________________________




c = 3
#indexMemory =['r']
#for i in range (len(test)): # make the x and the output values for testing
#    if (test[i][0] != indexMemory[len(indexMemory)-1]):
#            index = trainDate.index(test[i][0])
#            j = index
#            while (trainDate[j] == trainDate[j+1]):
#                x.append(train[j])
#                o.append(train[j][3])
#                j= j+ 1
#
#    indexMemory.append(test[i][0])

for i in range (1806305, len(train),3):#for all data
        x.append(train[i])
        o.append(train[i][3])

p = csv.writer(open('preparedData.csv',"wb"))# write data for validating the model
for i in train:
    p.writerow(i)
q = csv.writer(open('testData.csv',"wb"))# write data for validating the model
for i in x:
    q.writerow(i)

print len(x)
da.delCollumn(x,3)

print len(x)
print len(test)
#sys.exit('')
#train data ready
#___________________________________________________________________________

#from sklearn.svm import SVR
#from sklearn import linear_model
#from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
#clf= SVR(kernel= 'rbf', C = 1e3)

#clf = DecisionTreeRegressor(max_depth = 34)
clf = RandomForestRegressor(random_state = 0, n_estimators=60,max_depth=38)
#clf = linear_model.LinearRegression()

clf.fit(x,o)
print "complete"

#now predict
c = csv.writer(open("submit5.csv","wb"))
c.writerow(['id','units'])
for i in range (len(test)):# add the prediction to the submit file

    buff = str(testO[i][1]) + "_" + str(testO[i][2]) + "_" + str(testO[i][0])

    c.writerow( [  buff ,( str(int(max(0,clf.predict(test[i]))))) ] )

#add the predicting data to a testValidate file so as to test the model locally









