import csv
import math
import numpy as np
import six
import main as da

train= csv.reader(open(r'preparedData.csv'))
train= [[i for i in y ] for y in train]
train= [[float(i) for i in y ] for y in train]
#actualValue = da.getCollumn(train,3)
actualValue = []
for i in train[1806305:]:
    actualValue.append(i[3])
da.delCollumn(train,3)

x = csv.reader(open(r'testData.csv'))
x = [[i for i in y ] for y in x]
x = [[float(i) for i in y ] for y in x]
o = da.getCollumn(x,3)
da.delCollumn(x,3)
print "data uploaded"

#from sklearn.tree import DecisionTreeRegressor
#clf = DecisionTreeRegressor(max_depth =34)
#16:18=45,14=48

#from sklearn.svm import SVR
#clf= SVR(kernel= 'rbf', C = 1e3)
#from sklearn import linear_model
#clf = linear_model.LinearRegression()

from sklearn.ensemble import RandomForestRegressor
clf = RandomForestRegressor(random_state = 0, n_estimators=300,max_depth=34)

#from sklearn.ensemble import GradientBoostingClassifier
#clf = GradientBoostingClassifier(n_estimators = 100, max_depth = 1, random_state = 0)


clf.fit(x,o)

print ' trained'
y = []
for i in train[1806305:]:
    y.append(max(0,clf.predict(i)))
print 'predict'
error = 0

for i in range (len(y)):

    error = error + (math.log(y[i] + 1)  - math.log(actualValue[i] +1))  ** 2

error = error/ float(len(y))
error = math.sqrt(error)
print  error

# have to test it



