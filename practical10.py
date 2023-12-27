#WAP in which user will enter the days and it will print months and days

number_of_days=int(input("Enter the numbe rof days:"))

years = number_of_days // 365

months = (number_of_days - years *365) // 30

days = (number_of_days - years * 365 - months*30)

print("Years",years)
print("Months",months)
print("Days",days)
