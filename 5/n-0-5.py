import csv
from statistics import mean

with open('nceh1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        name = row[0]
        these_grades = list()
        for grade in row[1:]:
            these_grades.append(int(grade))
            # print(name , grade, these_grades)

        print("avarage of %s is %f" % (name, mean(these_grades)))
