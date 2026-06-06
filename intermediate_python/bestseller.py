import csv

# data_to_write = [
#   ['Name', 'Age', 'Grade'],
#   ['Alice', 25, 'A'],
#   ['Bob', 22, 'B'],
#   ['Charlie', 28, 'A+']
# ]

# with open("output.csv", "w", newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data_to_write)

file_to_read = "Bestseller - Sheet1.csv"
max_sales = 0
best_selling = []

with open(file_to_read, "r", encoding="utf8") as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)

    for row in data[1:]:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling.append(row)
            print(row)

with open("example.csv", "w", newline = "") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Book", "Author", "Sales in Million"])
    for row in best_selling:
        csv_writer.writerow([row[0],row[1], row[4]])