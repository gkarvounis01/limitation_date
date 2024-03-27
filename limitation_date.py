from datetime import date
import os

# Add years function
def add_years(start_date, add_years):
    try:
        return start_date.replace(year=start_date.year + add_years)
    except ValueError:
        return start_date.replace(year=start_date.year + add_years, day=28)
    
# Limitation range function
def country_select(country):
    if country == "1":
        return 15
    if country == "2" or "3":
        return 5

country = input("Select the country you want to add the Limitation Date.\n\n"
                "1. (ES) Spain - 15 years from Invoice Issue Date\n"
                "2. (ES) Spain Rental - 5 years from Invoice Issue Date\n"
                "3. (CH) Switzerland - 5 years from Invoice Issue Date\n"
                )

years = country_select(country)

# Clearing the Screen
os.system("cls")

# Receive starting date
txt = input("Paste the date (format m/d/y): ")
# split the date 
x = txt.split("/")

# Create the starting date
starting_date = date(int(x[2]), int(x[0]), int(x[1]))
#print(starting_date)

# Add years needed
final_date = add_years(starting_date, years)
#print(final_date)

# Print Limitaton date
limitation_date = final_date.strftime("%m/%d/%Y")
print("Limitation date:", limitation_date)