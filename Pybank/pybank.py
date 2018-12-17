# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
with open ('budget_data.csv') as csv_file:
    reader=csv.reader(csv_file, delimiter=',')
    counter=0
    total=0
    months=[]
    change=0
    totalchange=0
    maxprofit=0
    maxloss=0
    previous=0
    next(reader)
    for row in reader:
        month=row[0]
        thisone=int(row[1])
        total+=thisone
        change=thisone-previous
        totalchange+=change
        
        if (change>maxprofit) and (thisone>0):
            maxprofit=change
            profit_month=month
            
        if (change<maxloss) and (thisone<0):
            maxloss=change
            losses_month=month            
        previous=thisone
        counter+=1
        if month not in months:
            months.append(month)

print('Total:',total)
print('Months:',len(months))
print('Average change:',(totalchange/counter))
print ('Max Profits: ', profit_month,' ', (maxprofit))
print ('Max Loss:', losses_month, ' ', (maxloss))
