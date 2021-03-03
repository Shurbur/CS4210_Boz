#-------------------------------------------------------------------------
# AUTHOR: Alexander Boz
# FILENAME: Decision Tree
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: Too Long
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:
    all_values = []
    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    case = []
    #print(dbTraining)
    #print(len(dbTraining))
    for array in dbTraining:
        case = array[0:4]
        newcase =[]
        for i in case:
            if i == "Young":
                #newcase.remove("Young")
                newcase.append(1)
            elif i == "Prepresbyopic":
                #newcase.remove("Prepresbyopic")
                newcase.append(2)
            elif i == "Presbyopic":
                #newcase.remove("Presbyopic")
                newcase.append(3)
            elif i == "Myope":
                #newcase.remove("Myope")
                newcase.append(1)
            elif i == "Hypermetrope":
                #newcase.remove("Hypermetrope")
                newcase.append(2)
            elif i == "Reduced":
                #newcase.remove("Reduced")
                newcase.append(1)
            elif i == "Normal":
                #newcase.remove("Normal")
                newcase.append(2)
            elif i == "No":
                newcase.append(1)
            elif i == "Yes":
                newcase.append(2)
        X.append(newcase)
    #print(len(X))
    #print(X)




        #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
        #--> add your Python code here
        # Y =
    outcome =[]

    for array in dbTraining:

        outcome = array[3:5]
        lenses =[]
        for i in outcome:
            if i == "No":
               lenses.append(1)
            elif i == "Yes":
                lenses.append(2)
        Y.append(lenses)
    #print(Y)
    #print(len(Y))
        #loop your training and test tasks 10 times here
    test =[]
    class_predicted = []

    for i in range (10):

           #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

           #read the test data and add this data to dbTest
           #--> add your Python code here
           # dbTest =
        dataTest = ['contact_lens_test.csv']

        for dt in dataTest:

            dbTest =[]
            X_test = []
            Y_test = []

            with open(dt, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for i, row in enumerate(reader):
                    if i > 0:  # skipping the header
                        dbTest.append(row)

            for data in dbTest:
                   #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
                   #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
                   #--> add your Python code here
                   #print(data)
               test = data[0:4]
               new_case = []


               for i in test:

                   if i == "Young":
                       # newcase.remove("Young")
                       new_case.append(1)
                   elif i == "Prepresbyopic":
                       # newcase.remove("Prepresbyopic")
                       new_case.append(2)
                   elif i == "Presbyopic":
                       # newcase.remove("Presbyopic")
                       new_case.append(3)
                   elif i == "Myope":
                       # newcase.remove("Myope")
                       new_case.append(1)
                   elif i == "Hypermetrope":
                       # newcase.remove("Hypermetrope")
                       new_case.append(2)
                   elif i == "Reduced":
                       # newcase.remove("Reduced")
                       new_case.append(1)
                   elif i == "Normal":
                       # newcase.remove("Normal")
                       new_case.append(2)
                   elif i == "No":
                       new_case.append(1)
                   elif i == "Yes":
                       new_case.append(2)
               X_test.append(new_case)
        predic_come = []
        j = 0
        for sample in X_test:

            j +=1

            predic_come = clf.predict([sample])[0]
            #class_predicted.append('sample ' + str(j)+':')

            class_predicted.append(predic_come)


    #print(len(X_test))
    #print(class_predicted)
    #print(len(class_predicted))
    #print(dbTest)
    #print(X_test)



               #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
               #--> add your Python code here
        FN = 0

        FP = 0
        TP = 0
        TN = 0
        temp =[]
        temp2 = []
        truth = []
        truth2 = []
        #print(dbTest)
        for data in dbTest:
            help = []
            result = data[4]

            if result == "No":
               #print("made it")
               truth.append(1)
            else:
               #print("nope")
               truth.append(2)
            #truth.append(help)
        for every in class_predicted:

            for data in truth:


                if data == every:
                    if data == 1:
                        TN +=1
                    else:
                        TP +=1
                else:
                    if data == 1:
                        FP+= 1
                    else:
                        FN +=1


    #print(temp)



    #print (truth)

    #print(FN)
    #print(FP)
    #print(TN)
    #print(TP)



            #find the lowest accuracy of this model during the 10 runs (training and test set)
            #--> add your Python code here

        z = (TP+TN)/(FP+FN+TN+TP)
        all_values.append(z)

    answer = min(all_values)

        #print the lowest accuracy of this model during the 10 runs (training and test set).
        #your output should be something like that:
             #final accuracy when training on contact_lens_training_1.csv: 0.2
             #final accuracy when training on contact_lens_training_2.csv: 0.3
             #final accuracy when training on contact_lens_training_3.csv: 0.4
        #--> add your Python code here


    print("final acurracy when tracking on"+ ds + ":",answer)
