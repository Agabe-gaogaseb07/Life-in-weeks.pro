#Firstly my program ask the age as an input.
age = input("What is your current age?: ")

#Here 90 years is stored in a dictionary with how many days it has in total.
{"90 years; 32,850 days"}

#The days in a year and the current year are defined as you see with numbers 365 and 2022
daysinayear = 365
current_year = 2022

#The goal year is 2090
year = 2090

#Then we need to calculate how old the client is in days.(Client_age_in_days)
client_age_in_days = int(age) * int(365)

#And then how many days that is, it will be stored as a string (days).
days = client_age_in_days

#Then we find out how many weeks there are in 90 years.
weeks = 32850 // 7

#Then we subtract the total number of weeks from the 90 years in (weeks2)
weeks2 = 32850 - weeks 

#Here in weeks3, we multiply the clients age and number of weeks there are in 90 years to get how many weeks are left.
weeks3 = int(age) * int(weeks2)

#To get months, i divided 90 years in days into 30 to get total months in 90 years.
months = int(32850) / int(30)

#Then i subtract that total from 90 years in days.
months2 = 32850 - months

#Then multiply that total with the client's age to get the total months left to live.
months3 = int(age) * months2

#And lastly i use f-strings to run the code with it's variables.
print(f"You have {days} days, {weeks} weeks and {months} months left.")
