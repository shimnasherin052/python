leapyear=int(input("enter the year"))
for year in range (2024,leapyear+1):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(year,"is a leap year")
    else:
        print(year,"no!it is not leap year")
