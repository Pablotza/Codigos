import csv

# read the data from the CSV file
with open('expectativa-de-vida.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# remove the header row
header = data[0]
data = data[1:]

# find the year and country with the lowest life expectancy
min_val = float('inf')
min_country = ''
min_year = ''
for row in data:
    if float(row[3]) < min_val:
        min_val = float(row[3])
        min_country = row[0]
        min_year = row[2]
print(f"The year and country with the lowest life expectancy is: {min_year} {min_country} with a life expectancy of {min_val:.2f} years.")

# find the year and country with the highest life expectancy
max_val = float('-inf')
max_country = ''
max_year = ''
for row in data:
    if float(row[3]) > max_val:
        max_val = float(row[3])
        max_country = row[0]
        max_year = row[2]
print(f"The year and country with the highest life expectancy is: {max_year} {max_country} with a life expectancy of {max_val:.2f} years.")

# ask user to input a year of interest
year = input("Enter the year of interest: ")

# find the average life expectancy for the given year
total_life_expectancy = 0
count = 0
for row in data:
    if row[2] == year:
        total_life_expectancy += float(row[3])
        count += 1
if count == 0:
    print(f"No data available for year {year}.")
else:
    avg_life_expectancy = total_life_expectancy / count
    print(f"The average life expectancy for the year {year} is: {avg_life_expectancy:.2f} years.")

    # find the country with the minimum and maximum life expectancy for the given year
    min_val = float('inf')
    min_country = ''
    max_val = float('-inf')
    max_country = ''
    for row in data:
        if row[2] == year:
            if float(row[3]) < min_val:
                min_val = float(row[3])
                min_country = row[0]
            if float(row[3]) > max_val:
                max_val = float(row[3])
                max_country = row[0]
    print(f"For the year {year}:")
    print(f"The country with the minimum life expectancy is {min_country} with a life expectancy of {min_val:.2f} years.")
    print(f"The country with the maximum life expectancy is {max_country} with a life expectancy of {max_val:.2f} years.")
