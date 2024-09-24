#Write a program to convert specified days into years, weeks and days.
day=int(input("enter total days : "))
year=day//365
day=day%365
month=day//30
day=day%30
week=day//7
day=day%7
print(f"year ={year}")
print(f"month ={month}")
print(f"week ={week}")
print(f"day ={day}")
