import os

import csv

election_path = os.path.join(r'./daint/OneDrive/Desktop/election_data.csv')

with open(election_path, 'r') as text:
    lines = text.read()
    print(lines)
