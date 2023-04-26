import csv

with open('expectativa-de-vida.csv') as file:
    reader = csv.reader(file)
    next(reader) # skip header row

    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    max_life_country = None
    max_life_year = None
    life_expectancy_by_year = {}

    # Iterate through rows to find minimum, maximum, and build dict of life expectancies by year
    for row in reader:
        year, country, life_expectancy = row

        # Convert life_expectancy to a float
        life_expectancy = float(life_expectancy)

        # Check if we've found a new minimum or maximum
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_life_country = country
            max_life_year = year

        # Add life expectancy to dictionary for year
        if year not in life_expectancy_by_year:
            life_expectancy_by_year[year] = []
        life_expectancy_by_year[year].append((country, life_expectancy))

# Find year and country with highest life expectancy
print(f"The country with the highest life expectancy ({max_life_expectancy}) is {max_life_country}, in the year {max_life_year}.")

# Prompt user for year and find average, min, and max life expectancy for that year
year = input("Enter a year to find the average life expectancy for that year: ")
if year in life_expectancy_by_year:
    country_life_expectancies = life_expectancy_by_year[year]
    avg_life_expectancy = sum(x[1] for x in country_life_expectancies) / len(country_life_expectancies)
    print(f"The average life expectancy for {year} is {avg_life_expectancy:.2f}.")

    min_country = min(country_life_expectancies, key=lambda x: x[1])[0]
    max_country = max(country_life_expectancies, key=lambda x: x[1])[0]
    print(f"The country with the lowest life expectancy in {year} is {min_country}.")
    print(f"The country with the highest life expectancy in {year} is {max_country}.")
else:
    print(f"No data for {year}.")