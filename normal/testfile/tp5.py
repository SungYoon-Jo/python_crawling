import csv

with open("google.csv") as file_name:
    file_read = csv.reader(file_name)
    array = list(file_read)
    print(array)
    

