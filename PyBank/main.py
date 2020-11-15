import os

import csv

budget_path = os.path.join('..\Desktop\budget_data.csv', 'r')

budget_csv = budget_path

lines = 0
with open(budget_csv, 'r') as text:
    lines = text.read()
    print(lines)
