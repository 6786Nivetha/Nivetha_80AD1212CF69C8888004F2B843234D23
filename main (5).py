import calendar

yr = int(input ("Enter a Year = "))

if calendar.isleap(yr):
  print(yr,"is a leap Year.") 
else:
  print (yr, "is not.")

                