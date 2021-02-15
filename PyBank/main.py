import os

import csv

budget_path = os.path.join("../Python-challenge/Resources/budget_data.csv")

budget_csv = budget_path

# lines = 0
# with open(budget_csv) as text:
#     lines = text.read()
#     print(lines)


with open(budget_csv) as csvfile:

    budget_data = csv.reader(csvfile, delimiter=",")
    header = next(budget_data)


#Months       
    month = []
    revenue = []

    for row in budget_data:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))

    total_revenue = (sum(revenue))
    print(total_revenue)
    
    # months =  []
    # for item in budget_data:
    #     item.append(item[0])
        
    # print(budget_data)
    # # month_list = []
    # # for result in months:
    # #     month_list.append(result)

    # year = []
    # month = []
    # month_count = {}
    # for entry in budget_data:   
    #     month_list = str(month_count)
    #     month_list.replace('-', ',').split(',') 
    #     month.append(month_list[0])
    #     year.append(month_list[1])

        # if month not in month_count:
        #     month_count = 0
        #     month_count += 1


    # total_months = [{'month': entry, 'count': month_count[entry]} for entry in month_count]
   
