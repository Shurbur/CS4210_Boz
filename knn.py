#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries

from sklearn.neighbors import KNeighborsClassifier
import csv

db = []


#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
FN = 0

FP = 0
TP = 0
TN = 0
for each in db:
    if each[2] == '-':
        each[2] = 1
    else:
        each[2] = 2


#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):
    X = []
    Y = []
    testSample = []

    #print(instance)






    #for each in db:
      #  instance.pop()
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
    #--> add your Python code here

    for each in db:
        this = []
        for a in each[:2]:

            this.append(int(a))
            #this.remove(a)

        X.append(this)
    for each in instance[:2]:

        instance.append(int(each))
    instance = instance[2:]
    #print(instance)
    instance+=[instance.pop(0)]



    #print(instance)
    #print(X)
    a = X.index(instance[:2])
    #print(a)
    testSample_X = X.pop(a)

    #print(testSample_X)




    #testSample.append(db.pop(0))

    #X.append(testSample.pop(0))
    #for each in instance:
    #db.pop()

    #X.append(instance[:2])
    #happy = (X.pop())
    #testSample.append(happy)
    #print(testSample)
    #print(testSample)
    #print(X)
















    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]
    #--> add your Python code here
    # Y =

    for each in db:
        #if each[2] == '-':
            #Y.append(1)
        #else:
           # Y.append(2)
        Y.append(each[2])

    b = Y.index(instance[2])

    testSample_Y = Y.pop(b)
    #print(testSample_Y)
    #print(Y)
    #Y.append(instance[2:])
    # add positive or negative - same iteration
    #for row in db:
     #   case = row[2:]

        #print(case)
    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here

    testSample.append(instance[:2])
    #print(X)
    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict(testSample)[0]


    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    #FN + FP /FP + FN + TP + TN


    #print(testSample_Y)
    #print(class_predicted)
    if class_predicted == testSample_Y:
        if testSample_Y == 1:
            TN += 1
        else:
            TP += 1
    else:
        if testSample_Y == 1:
            FP += 1
        else:
            FN += 1
    print(instance)
    print(class_predicted, testSample,testSample_Y)
#print the error rate
#--> add your Python code here
print(FN)
print(FP)
print(TN)
print(TP)
z = (FN + FP) /(FP + FN + TP + TN)
print(z)





