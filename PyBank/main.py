import os

import csv

budget_path = os.path.join("..", "Resources", "budget_data.csv")

budget_csv = budget_path

# lines = 0
# with open(budget_csv) as text:
#     lines = text.read()
#     print(lines)


with open(budget_csv) as csvfile:

    budget_data = csv.reader(csvfile, delimiter=",")
    header = next(budget_data)

    months = {}
    for entry in budget_data:   
        if entry[0] not in months:
            months[entry[0]] = 0
            months[entry[0]] = months[entry[0]] + 1

    total_months = [{'month': entry, 'count': months[entry]} for entry in months]
    print(total_months)
