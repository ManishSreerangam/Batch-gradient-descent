# -*- coding: utf-8 -*-

import sys
import csv
import uuid
"""
Loading input values from command prompt
"""
#"""
#loading our csv file 
args=sys.argv
#loading our csv file 

file=open(args[2],newline='')
reader=csv.reader(file)
data=[row for row in reader]
#initializing learning rate 
learning_rate= float(args[4])
#initializing threshold rate 
threshold_rate= float(args[6])

#initializing list for x values
x_values = [ ] 
#initializing list for y values
y_actual = [ ] 
#finding number of rows in our dataset
rows = len(data) 
#finding number of columns in our dataset
columns = len(data[0])
#counter : to notify when we reach last column in every row
counter = 0
#seperating dependent and independent variables 
for i in range(0 , rows) :
    independent_variable = [1]    #initializing x1 == 1
    dependent_variable,counter=[],0
    for j in data[i] :
        counter += 1
        if counter == columns :
            dependent_variable.append(float(j))
            break
        independent_variable.append(float(j))
    y_actual.append(dependent_variable)    
    x_values.append(independent_variable)

#initializing a list for weights
#weight_list = []
#initializing  for weights
grad_list={ }
# intializing evry column with a 0.000
for i in range(columns):
    grad_list[i]=float(0)
    
    
weight_list={}
# intializing evry column with a 0.000
for i in range(columns):
    weight_list[i]=float(0)






#print(weight_list)
l=columns-1

y_original={}
for j in range(rows):
    y_original[j]=float(data[j][l])
#print(y_original)

iteration=0
stopping_criteria=[]
 
while True:
    
    final_output=[] #initializing list for priniting
    hypothesis =[]  #initializing list for hypothesis 
        
    for i in range(len(x_values)):
            
        row = 0
            
        for j in range(len(x_values[0])):
            row += weight_list[j]*x_values[i][j] 
            
        hypothesis.append(row)
            
    error = [y_original[i]-hypothesis[i] for i in range(rows) ]
        
    sum_of_squared_error =[error * error for error in error]
        
        
        # for output printing  
        
        
    final_output.append(iteration)
    print(iteration , end = ',')
    for i in range(len(data[0])):
        print(round(weight_list[i],4), end =',')
        final_output.append(round(weight_list[i],4))
    final_output.append(round(sum(sum_of_squared_error),4))
    print(round(sum(sum_of_squared_error),4))
        
 
    stopping_criteria.append(sum(sum_of_squared_error))
    for j in range(len(data[0])):
        a =[]
        for i in range(len(data)):
            a.append(x_values[i][j]*error[i])
        grad_list[j]=sum(a)
    for i in range(len(data[0])):
        weight_list[i]=weight_list[i]+(learning_rate*grad_list[i])  
#for coming out of loop or stopping criteria           
    if(iteration>0 and stopping_criteria[iteration-1]-stopping_criteria[iteration] < threshold_rate):
        break
    iteration+=1 
  



