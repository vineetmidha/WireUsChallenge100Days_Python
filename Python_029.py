# Problem statement in description

age = int(input("Enter age (less than 100): "))

if age < 0 or age > 100:
    print("Invalid age")
    exit()

birth_year = int(input("Enter year of birth (yyyy): "))

if birth_year < 0 or birth_year > 2020 or len(str(birth_year)) != 4:
    print("Invalid year")
    exit()

target_year = 2020 + (100-age)

print("You will turn 100 in", target_year)
            
year = int(input("Enter a year to know your age in that year (yyyy): "))

if year < 2020 or len(str(year)) != 4:
    print("Invalid year")
    exit()

print("You will turn", year-birth_year, "in", year)

