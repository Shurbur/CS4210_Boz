#-------------------------------------------------------------------------
# AUTHOR: Alexander Boz
# FILENAME: find_s.py
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: 3 days
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
#column = row.split(", ")

for row in db:
		#print (i)
	
	if row[4] == "Yes":
		
		
		hypothesis = row
		print (hypothesis)
		break
	
##################
#for i in row:
"""for column in row:	
	print (column[0])
	print (i[1])
	if (i[2] == "yes"):
		print("yes")
#if (row == "yes"):
	#print ("this works")"""

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here
#for i in hypothesis: 
#	attribute = i
#	print(attribute)
for row in db:
	
	#print("1")
	#for j in row:
		#print("2")

	if row[4] == "Yes":
	
		#if row[x] != hypothesis[x]:
				#hypothesis[1]= "?" 
		if row[0] != hypothesis[0]:
			 hypothesis[0] ="?"
		if row[1] != hypothesis[1]:
				hypothesis[1]= "?" 
		if row[2] != hypothesis[2]:
				hypothesis[2] = "?" 
		if row[3] != hypothesis[3]:
				hypothesis[3] = "?"
		if row[4] != hypothesis[4]:
				hypothesis[4] = "?"

				#if i != j:
					
					#print("4")
					#hypothesis.replace(i,"?")
					#["?"if j!=i else i for i in hypothesis]
	 
			


	#if i in hypothesis != i:
		#print (i in hypothesis)
		#print (i)
		#print("yes")

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)