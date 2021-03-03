#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
#reading the training data
#--> add your Python code here
db = []
X=[]
Y=[]
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
print(db)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
for each in db:

    newcase = []

    for a in each:

        if a == "Sunny":
            # newcase.remove("Young")
            newcase.append(1)
        elif a == "Overcast":
            # newcase.remove("Prepresbyopic")
            newcase.append(2)
        elif a == "Rain":
            # newcase.remove("Presbyopic")
            newcase.append(3)
        elif a == "Overcast":
            # newcase.remove("Myope")
            newcase.append(4)
        elif a == "Hot":
            # newcase.remove("Hypermetrope")
            newcase.append(5)
        elif a == "Mild":
            # newcase.remove("Reduced")
            newcase.append(6)
        elif a == "Cool":
            # newcase.remove("Normal")
            newcase.append(7)
        elif a == "Normal":
            newcase.append(8)
        elif a == "High":
            newcase.append(9)
        elif a == "Weak":
            newcase.append(10)
        elif a == "Strong":
            newcase.append(11)
    X.append(newcase)
    #X.append(each[1:5])
print(X)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
#          elif i == "No":
#             newcase.append(1)
#         elif i == "Yes":
#             newcase.append(2)
for each in db:
    newcaseY = []
    for a in each:

        if a == "No":
            print("made it")
            newcaseY.append(1)
        elif a == "Yes":
            newcaseY.append(2)
    Y.append(newcaseY)
print(Y)
#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
dt = []
X_test = []
Y_test = []
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dt.append (row)

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for data in dt:
    newcase_test = []
    for a in each:

        if a == "Sunny":
            # newcase.remove("Young")
            newcase_test.append(1)
        elif a == "Overcast":
            # newcase.remove("Prepresbyopic")
            newcase_test.append(2)
        elif a == "Rain":
            # newcase.remove("Presbyopic")
            newcase_test.append(3)
        elif a == "Overcast":
            # newcase.remove("Myope")
            newcase_test.append(4)
        elif a == "Hot":
            # newcase.remove("Hypermetrope")
            newcase_test.append(5)
        elif a == "Mild":
            # newcase.remove("Reduced")
            newcase_test.append(6)
        elif a == "Cool":
            # newcase.remove("Normal")
            newcase_test.append(7)
        elif a == "Normal":
            newcase_test.append(8)
        elif a == "High":
            newcase_test.append(9)
        elif a == "Weak":
            newcase_test.append(10)
        elif a == "Strong":
            newcase_test.append(11)

    X_test.append(newcase_test)
print(X_test)
for each in X_test:
    predicted = clf.predict_proba([each])[0]
print(predicted)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

