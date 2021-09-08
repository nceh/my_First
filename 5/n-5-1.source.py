import csv
from statistics import mean


def calculate_averages(input_file_name, output_file_name):
    with open('m.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(int(grade))
    return these_grades


print(calculate_averages())

# def calculate_sorted_averages(input_file_name, output_file_name):
#
#
# def calculate_three_best(input_file_name, output_file_name):
#
#
# def calculate_three_worst(input_file_name, output_file_name):
#
#
# def calculate_average_of_averages(input_file_name, output_file_name):
