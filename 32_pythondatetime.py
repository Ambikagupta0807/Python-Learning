import datetime
x = datetime.datetime.now()
print(x)

#2026-03-10 13:05:53.372056
# this code will display the current date and time. The datetime module has many other functions to return information about date and time, and to perform various operations on date and time. You can find more information about the datetime module in the Python documentation.

# this will return the year and weekday of the current date:
y = datetime.datetime.now()
print(y.year)
print(y.month)
print(y.strftime("%A"))

#creating a date : you can create a date by using the datetime() class (constructor) of the datetime module. The datetime() class requires three parameters to create a date : year, month, day.
z = datetime.datetime(2022, 10, 5)
print(z)

x = datetime.datetime(2022, 10, 5)
print(x.strftime("%B"))

# reference of all the legal format codes : https://www.w3schools.com/python/python_datetime.asp

#%a 	Weekday, short version	Wed	
#%A	    Weekday, full version	Wednesday	
#%w	     Weekday as a number 0-6, 0 is Sunday	3	
#%d	    Day of month 01-31	31	
#%b 	Month name, short version	Dec	
#%B 	Month name, full version	December	
#%m	    Month as a number 01-12	12	
#%y	    Year, short version, without century	18	
#%Y	    Year, full version	2018		
#%j 	Day number of year 001-366	365	
#%H 	Hour 00-23	17    
#%I 	Hour 00-12	05
#%p 	AM/PM	PM
#%M 	Minute 00-59	41
#%S 	Second 00-59	00
#%f 	Microsecond 000000-999999	372056
#%U 	Week number of year, Sunday as the first day of week, 00-53	52	
#%W	    Week number of year, Monday as the first day of week, 00-53	52	
#%c	    Local version of date and time	Mon Dec 31 17:41:00 2018	
#%C	    Century	20	
#%x	    Local version of date	12/31/18	
#%X	    Local version of time	17:41:00	
#%%	    A % character	%	
#%G	    ISO 8601 year	2018	
#%u	    ISO 8601 weekday (1-7)	1	
#%V	    ISO 8601 weeknumber (01-53)	01