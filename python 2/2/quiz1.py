import csv


class Customer:

    def __init__(self, name, national_code, sum_purchase):
        self.name = name
        self.national_code = national_code
        self.sum_purchase = sum_purchase


class_customers = []

with open('Book1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        customerObj = Customer(row[0], row[1], row[2])
        class_customers.append(customerObj)
        print(row)
        # b=[]
        # for row in reader:
        #     sum_purchase =customerObj.sum_purchase
        #     b.append(sum_purchase)
temp = []
for item in class_customers:
    temp.append(item.sum_purchase)

print(max(temp))

# print(b)
# print(customerObj)
# print(class_customers)
print((customerObj.sum_purchase))
