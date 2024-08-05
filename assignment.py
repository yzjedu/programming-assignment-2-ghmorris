# Programmer: Grace-Ann Morris
# Course: CS701/GB-731, Dr. Yalew
# Date: August 6, 2024
# Programming Assignment: 2
# Program Inputs: Month (as a number in the range 1 through 12), Year
# Program Outputs: Number of days in the given month

# Algorithm: Start
def main():
# Step 1: Ask the user for the month and year
    month = int(input("Please enter the month (1-12): "))
    year = int(input("Please enter the year: "))

    def is_leap(year): 
    # Step 2: Determine if the year is a leap year
        if year % 400 == 0:  
            return  True # If the year is divisible by 400 then it is a leap year 
        elif year % 100 == 0: 
            return False # If the year is divisible by 100 but not 400 it is not a leap year 
        elif year % 4 == 0: 
            return True # If the year is divisible by 4 but not 100 it is a leap year
        else: 
            return False # If year is not divisible by 4 it is not a leap year
        
    # Step 3: Determine the number of days in the month
    if month < 1 or month > 12: # If month is not between 1-12 it is invalid
        print("Invalid month")
    else:
        if month == 2: # If the month is February 
            if is_leap(year):
                days = 29 # If a leap year, February has 29 days 
            else: 
                days = 28 # If not a leap year, February has 28 days 
        elif month in [4, 6, 9, 11]: # April, June, September, or November use 30 days 
            days = 30 
        else:
            days = 31 # All other months have 31 days 
    # Step 4: Output the number of days in the month
        print(f"The month has {days} days")

if __name__ == "__main__":
    main()