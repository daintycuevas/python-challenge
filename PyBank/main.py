import os
import csv

budget_path = os.path.join(r'.\Resources\budget_data.csv')
budget_csv = (budget_path)

with open(budget_csv, 'r') as text:
    lines = text.read()
    print(lines)

    
