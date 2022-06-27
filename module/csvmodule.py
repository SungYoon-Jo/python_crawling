import csv

filename = 'google.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)
