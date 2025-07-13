#This file only are for checks.

import csv

#Read the csv
with open('src/data/expenses.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f'{row['category']} , lenght: {len(row['category'])}')

#Insert a element to csv:
# with open('src/data/expenses.csv','w') as file:
#     Writer = csv.writer(file)
#     Writer.writerow()


from datetime import datetime 
now = datetime.now()

print(now)
print(now.date())

