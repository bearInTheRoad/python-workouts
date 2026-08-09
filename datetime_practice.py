# Exercise 1
# Problem Statement: Write a Python program to print the current date and time.

# Purpose: This exercise introduces you to Python’s datetime module and shows how to retrieve the current system date and time – a fundamental skill used in logging, scheduling, and timestamping data.
#
# Given Input: No input required. The program reads the current system date and time.
#
# Expected Output: Current date and time: 2025-01-15 14:23:45.123456 (output will vary based on when the program runs)

import datetime

print("Exercise 1")
print(datetime.datetime.now())


# Exercise 2: Format DateTime
# Problem Statement: Write a Python program to format the current date and time into a human-readable string using a custom format.
#
# Purpose: This exercise teaches you how to use strftime() to control the display of date and time values – an essential skill for generating reports, file names, log entries, and user-facing timestamps.
#
# Given Input: No input required. Use the current date and time.
#
# Expected Output: Formatted: 15-Jan-2025 02:23:45 PM (output will vary based on when the program runs)

print("----------------------")
print("Exercise 2")
print(datetime.datetime.strftime(datetime.datetime.now(), "%d-%b-%Y %H:%M:%S"))
print(datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))


# Exercise 3: Find Day of Week
# Problem Statement: Write a Python program to find the day of the week for a given date.
#
# Purpose: This exercise shows how to extract the weekday from a date – useful in scheduling applications, calendar tools, and any logic that depends on whether a day falls on a weekday or weekend.
#
# Given Input: date = datetime(2025, 1, 15)
#
# Expected Output: Day of the week: Wednesday

print("----------------------")
print("Exercise 3")
date = datetime.datetime(2025, 1, 15)
print(date.weekday())  # weekday is 0 - 6, hence 2 is wednesday
print(date.strftime("%A"))


# Exercise 4: Convert Datetime into String
# Problem Statement: Write a Python program to convert a datetime object into a string representation.
#
# Purpose: This exercise shows how to serialize a datetime object into a plain string, which is needed when storing dates in text files, databases, JSON payloads, or sending them over APIs.
# Given Input: dt = datetime(2025, 6, 15, 10, 30, 45)
#
# Expected Output: DateTime as string: 2025-06-15 10:30:45
print("-----------------------")
print("Exercise 4")
dt = datetime.datetime(2025, 6, 15, 10, 30, 45)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))


# Exercise 5: Extract Components
# Problem Statement: Write a program to extract the Year, Month, Day, Hour, Minute, and Second as separate integers from a single datetime object.
#
# Purpose: This exercise teaches you how to access individual date and time components from a datetime object – useful when you need to perform calculations, comparisons, or conditional logic on specific parts of a timestamp.
#
# Given Input: dt = datetime(2025, 8, 20, 14, 35, 50)
#
# Expected Output:
# Year: 2025
# Month: 8
# Day: 20
# Hour: 14
# Minute: 35
# Second: 50

print("-----------------------")
print("Exercise 5")
dt = datetime.datetime(2025, 8, 20, 14, 35, 40)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)


# Exercise 6: Print Time with AM/PM
#
# Problem Statement: Format the current time to display in a 12-hour format with AM/PM (e.g., “02:30 PM”).
#
# Purpose: This exercise shows how to present time in the 12-hour clock format that is standard in many user-facing applications, notifications, and interfaces intended for general audiences.
#
# Given Input: No input required. Use the current system time.
#
# Expected Output: Current time: 02:30 PM (output will vary based on when the program runs)
#
print("-----------------------")
print("Exercise 6")

source = datetime.datetime.now()
print(source.strftime("%I:%M %p"))


# Exercise 7: Print Current Time in Milliseconds
# Problem Statement: Write a Python program to print the current time including milliseconds.
#
# Purpose: This exercise shows how to access sub-second precision from a datetime object – important in performance profiling, event logging, benchmarking, and any application where millisecond-level accuracy matters.
#
# Given Input: No input required. Use the current system time.
#
# Expected Output: Current time with milliseconds: 14:23:45.123 (output will vary based on when the program runs)

print("-----------------------")
print("Exercise 7")
print(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])


# Exercise 8
# Problem Statement: Calculate which day of the year it is (from 1 to 366) for any given date.
#
# Purpose: This exercise demonstrates how to derive the ordinal day of the year from a date – a useful calculation in scientific data analysis, day-of-year reporting, agricultural or financial calendars, and countdown timers.
#
# Given Input: date = datetime(2025, 3, 15)
#
# Expected Output: Day of the year: 74

print("-----------------------")
print("Exercise 8")
date = datetime.datetime(2025, 3, 15)
print(date - datetime.datetime(2025, 1, 1) + datetime.timedelta(days=1))
print(int(date.strftime("%j")))

# Exercise 9: Combine Date and Time Objects
# Problem Statement: Create a date object and a time object separately, then combine them into a single datetime object using datetime.combine().
#
# Purpose: This exercise shows how to work with the date and time types independently before merging them – a pattern commonly used when date and time values arrive from different sources, such as separate form fields or database columns.
#
# Given Input: d = date(2025, 5, 20) and t = time(9, 45, 0)
#
# Expected Output: Combined datetime: 2025-05-20 09:45:00

print("-----------------------")
print("Exercise 9")
d = datetime.date(2025, 5, 20)
t = datetime.time(9, 45, 0)
print(datetime.datetime.combine(d, t))

# Exercise 10
# Purpose: This exercise teaches you how to parse date strings using strptime() – a critical skill when reading dates from CSV files, APIs, user input, or databases where dates arrive as plain text and must be converted for calculations or comparisons.
#
# Given Input: date_string = "20 January, 2025"
#
# Expected Output: DateTime object: 2025-01-20 00:00:00

print("-----------------------")
print("Exercise 10")
date_string = "20 January, 2025"
print(datetime.datetime.strptime(date_string, "%d %B, %Y"))


# Exercise 11: Subtract a Week From a Given Date
# Problem Statement: Write a Python program to subtract one week from a given date and print the resulting date.
#
# Purpose: This exercise introduces timedelta, Python’s built-in class for representing a duration or difference between two dates. Subtracting fixed intervals from dates is a common need in scheduling, deadline tracking, and generating historical date ranges.
#
# Given Input: date = datetime(2025, 3, 15)
#
# Expected Output: Date after subtracting one week: 2025-03-08 00:00:00

print("-----------------------")
print("Exercise 11")
date = datetime.datetime(2025, 3, 15)
print(date - datetime.timedelta(weeks=1))


# Exercise 13: Calculate Days Between Two Dates
# Problem Statement: Write a Python program to calculate the number of days between two given dates.
#
# Purpose: This exercise shows how to measure the elapsed time between two points in time – a calculation needed in age computations, project duration tracking, invoice due-date checks, and any feature that works with date ranges.
#
# Given Input: date1 = datetime(2025, 1, 1) and date2 = datetime(2025, 3, 15)
#
# Expected Output: Days between dates: 73

print("-----------------------")
print("Exercise 13")
date1 = datetime.datetime(2025, 1, 1)
date2 = datetime.datetime(2025, 3, 15)
gap = date2 - date1

print(gap.days)


# Exercise 14: Convert Unix Timestamp to Datetime
# Problem Statement: Given a Unix timestamp (e.g., 1672531200), convert it into a human-readable Python datetime object.
#
# Purpose: This exercise shows how to interpret Unix timestamps, which are integers representing the number of seconds elapsed since January 1, 1970 (UTC). They appear throughout APIs, server logs, databases, and file systems, making this conversion an essential real-world skill.
#
# Given Input: timestamp = 1672531200
#
# Expected Output: Datetime from timestamp: 2023-01-01 00:00:00

print("-----------------------")
print("Exercise 14")
timestamp = 1672531200
print(
    datetime.datetime.fromtimestamp(timestamp, datetime.UTC).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
)


# Exercise 15: Get ISO Week Number
# Problem Statement: Find the ISO week number for a specific date (e.g., January 1st, 2026).
#
# Purpose: This exercise introduces the ISO 8601 week numbering system, where weeks run Monday to Sunday and the first week of the year is defined as the week containing the first Thursday. ISO week numbers are widely used in business reporting, payroll systems, and European calendar conventions.
#
# Given Input: date = datetime(2026, 1, 1)
#
# Expected Output: ISO week number: 1

print("-----------------------")
print("Exercise 15")
date = datetime.datetime(2026, 1, 1)
print(date.isocalendar()[1])
print(date.strftime("%V"))


# Exercise 16: Subtract 5 Hours and 30 Minutes
# Problem Statement: Take the current time and subtract exactly 5 hours and 30 minutes from it using timedelta.
#
# Purpose: This exercise helps you practice using timedelta for time arithmetic, a skill essential in scheduling, time zone conversions, and log analysis where offsets from a reference time are commonly needed.
#
# Given Input: Current datetime (e.g., datetime.now())
#
# Expected Output: 5 hours and 30 minutes before now: 2025-07-15 08:45:00.123456 (actual value will vary)

print("-----------------------")
print("Exercise 16")
source = datetime.datetime.now()
print(source + datetime.timedelta(hours=5, minutes=30))


# Exercise 17: Check for Leap Year
# Problem Statement: Write a function that takes a year as input and returns True if it is a leap year and False otherwise, using the calendar module.
#
# Purpose: This exercise introduces the calendar module and Boolean-returning functions, while reinforcing the concept of leap year logic used in date calculations, calendar applications, and scheduling systems.
#
# Given Input: year = 2024
#
# Expected Output: 2024 is a leap year: True
print("-----------------------")
print("Exercise 17")
import calendar

year = 2024
print(calendar.isleap(year))


# Exercise 18: Calculate Age in Days
# Problem Statement: Input a birthdate and calculate exactly how many days old a person is today.
#
# Purpose: This exercise practices date subtraction and working with timedelta objects, skills used in age verification systems, health apps, and any application that needs to measure elapsed time between two dates.
#
# Given Input: birthdate = date(1995, 6, 15)
#
# Expected Output: Age in days: 10992 (actual value will vary based on today’s date)

print("-----------------------")
print("Exercise 18")
birthdate = datetime.datetime(1995, 6, 15)
gap = datetime.datetime.now() - birthdate
print(gap.days)


# Exercise 19: Difference in Seconds
# Problem Statement: Calculate the total number of seconds between two specific datetime objects.
#
# Purpose: This exercise teaches you to extract the total elapsed time in seconds from a timedelta, a technique used in performance benchmarking, event duration tracking, and countdown timers.
#
# Given Input: dt1 = datetime(2025, 1, 1, 9, 0, 0) and dt2 = datetime(2025, 1, 1, 11, 45, 30)
#
# Expected Output: Difference in seconds: 9930.0

print("-----------------------")
print("Exercise 19")
dt1 = datetime.datetime(2025, 1, 1, 9, 0, 0)
dt2 = datetime.datetime(2025, 1, 1, 11, 45, 30)

print((dt2 - dt1).seconds)
print((dt2 - dt1).total_seconds())

# Exercise 20: Print a Monthly Calendar
# Problem Statement: Accept a year and a month from the user and print a formatted text calendar for that month.
#
# Purpose: This exercise introduces the calendar module’s text rendering capabilities, useful for building CLI tools, report generators, and any interface that needs to display human-readable date grids.
#
# Given Input: year = 2025, month = 7
print("-----------------------")
print("Exercise 20")

calendar.prmonth(theyear=2025, themonth=7)


# Exercise 21: Calculate the Date 4 Months From Today
# Problem Statement: Calculate and display the date that falls exactly 4 months from the current date.
#
# Purpose: This exercise teaches month-based date arithmetic, a common requirement in billing cycles, subscription renewals, and project deadline calculations where timedelta alone is insufficient because months vary in length.
#
# Given Input: Current date (e.g., date.today())

print("-----------------------")
print("Exercise 21")
from dateutil.relativedelta import relativedelta

source = datetime.date.today()
print(source + relativedelta(months=4))


# Exercise 22: Find the First Day of the Month
# Problem Statement: For any given date, write a script to find the date of the first day of that specific month.
#
# Purpose: This exercise practices date manipulation with replace(), commonly used in financial reporting, monthly aggregations, and generating date ranges that start at the beginning of a billing or calendar period.
#
# Given Input: given_date = date(2025, 8, 17)
#
# Expected Output: First day of the month: 2025-08-01

print("-----------------------")
print("Exercise 22")
source = datetime.date(2025, 8, 17)
print(source + relativedelta(day=1))
print(source.replace(day=1))


# Exercise 23: Find the Last Day of the Month
# Problem Statement: Determine the last day of the current month (e.g., 28, 29, 30, or 31).
#
# Purpose: This exercise shows how to query month-end dates using the calendar module, a requirement in payroll systems, invoice due-date calculations, and any logic that must handle months of varying lengths including leap year Februaries.
#
# Given Input: Current date (e.g., date.today())
#
# Expected Output: Last day of current month: 2025-07-31 (actual value will vary)

print("-----------------------")
print("Exercise 23")
source = datetime.datetime.today()
if source.month == 2:
    if calendar.isleap(source.year):
        day = 29
    else:
        day = 28
elif source.month in (1, 3, 5, 7, 8, 10, 12):
    day = 31
else:
    day = 30

print(source.replace(day=day))


start_date, end_date = calendar.monthrange(source.year, source.month)
print(source.replace(day=end_date))


# Exercise 24: Find the Date of the Next Monday
# Problem Statement: Write a script that calculates the date of the upcoming Monday, regardless of what today’s date is.
#
# Purpose: This exercise practices weekday arithmetic using timedelta and weekday(), skills used in scheduling tools, weekly report generators, and calendar applications that need to align dates to specific days of the week.
#
# Given Input: Current date (e.g., date.today())
#
# Expected Output: Next Monday: 2025-07-21 (actual value will vary)

print("-----------------------")
print("Exercise 24")
source = datetime.date.today()
print(source + datetime.timedelta(days=(7 - source.weekday()) % 7))


# Exercise 25: Round Time to the Nearest Hour
# Problem Statement: Write a program that takes a datetime object and rounds it to the closest full hour.
#
# Purpose: This exercise practices minute-based time arithmetic and conditional rounding logic, techniques applied in time series analysis, billing rounded to the nearest hour, and event logging systems that bucket timestamps.
#
# Given Input: dt = datetime(2025, 7, 15, 14, 35, 0)
#
# Expected Output: Rounded to nearest hour: 2025-07-15 15:00:00


print("-----------------------")
print("Exercise 25")
source = datetime.datetime(2025, 7, 15, 14, 29, 0)
if source.minute < 30:
    print(source.replace(minute=0))
else:
    print(source.replace(hour=source.hour + 1, minute=0))


# Exercise 26: List All Sundays in a Year
# Problem Statement: Generate a list of all dates that fall on a Sunday for the year 2026.
#
# Purpose: This exercise practices iterating over a date range and filtering by weekday, a technique used in scheduling systems, retail planning, and any application that needs to enumerate specific days across a calendar year.
#
# Given Input: year = 2026
#
# Expected Output: A list of all 52 Sunday dates in 2026, starting with 2026-01-04 and ending with 2026-12-27.

print("-----------------------")
print("Exercise 26")
start = datetime.datetime(2026, 1, 1)
sundays = []
while start < datetime.datetime(2027, 1, 1):
    if start.weekday() == 6:
        sundays.append(start)
    start += datetime.timedelta(days=1)
# print(sundays)
print(len(sundays))


# Exercise 27: Calculate Business Days Between Two Dates
# Problem Statement: Calculate the number of days between two dates, excluding Saturdays and Sundays.
#
# Purpose: This exercise teaches weekday filtering over a date range, an essential skill in HR systems, project management tools, SLA tracking, and financial applications where only working days count toward deadlines.
#
# Given Input: start = date(2025, 7, 1) and end = date(2025, 7, 31)
# Expected Output: Business days between 2025-07-01 and 2025-07-31: 23
#
print("-----------------------")
print("Exercise 27")
start = datetime.date(2025, 7, 1)
end = datetime.date(2025, 7, 31)

bdays = 0
while start <= end:
    if not start.weekday() in (5, 6):
        bdays += 1
    start += datetime.timedelta(days=1)
print(bdays)

import numpy as np

start = datetime.date(2025, 7, 1)
end = datetime.date(2025, 7, 31)
# busday count is half open, so add one day
print(np.busday_count(start, end + datetime.timedelta(days=1)))


# Exercise 28: Convert Local Time to UTC
# Problem Statement: Take a local datetime object and convert it to Coordinated Universal Time (UTC).
#
# Purpose: This exercise introduces timezone-aware datetime objects and UTC conversion, a foundational skill for building globally distributed applications, APIs, databases, and any system that stores or transmits timestamps across time zones.
#
# Given Input: A naive local datetime representing IST (UTC+5:30), e.g., datetime(2025, 7, 15, 10, 30, 0)
#
# Expected Output: Local (IST): 2025-07-15 10:30:00+05:30 and UTC: 2025-07-15 05:00:00+00:00

print("-----------------------")
print("Exercise 28")
from zoneinfo import ZoneInfo

# Naive datetime representing a local time in IST (UTC+5:30)
naive_dt = datetime.datetime(2025, 7, 15, 10, 30, 0)

# Make it timezone-aware by attaching the local timezone
local_dt = naive_dt.replace(tzinfo=ZoneInfo("Asia/Kolkata"))

# Convert to UTC
utc_dt = local_dt.astimezone(ZoneInfo("UTC"))

print("Local (IST):", local_dt)
print("UTC:        ", utc_dt)


# Exercise 29: Get Current Time in a Specific City
# Problem Statement: Use the zoneinfo (or pytz) library to print the current time in “Asia/Tokyo” and “America/New_York”.
#
# Purpose: This exercise demonstrates how to retrieve and display the current time across multiple time zones simultaneously, a core requirement in world clocks, international meeting schedulers, trading dashboards, and global customer support tools.
#
# Given Input: No input required. Uses datetime.now() with a timezone argument.
#
# Expected Output: Current times in both cities, formatted clearly (actual values will vary by when the program is run).

print("-----------------------")
print("Exercise 29")
source = datetime.datetime.now()
print(source.astimezone(ZoneInfo("Asia/Tokyo")))
print(source.astimezone(ZoneInfo("America/New_York")))


# Exercise 30: Calculate Date After N Working Days
# Problem Statement: Given a start date, find the date that occurs after 10 working days, skipping weekends.
#
# Purpose: This exercise combines weekday checking with iterative date advancement, a pattern used in contract management, delivery estimation, legal deadline calculators, and any workflow where turnaround times are measured in business days rather than calendar days.
#
# Given Input: start_date = date(2025, 7, 1) and n = 10
# Expected Output: Date after 10 working days from 2025-07-01: 2025-07-15
print("-----------------------")
print("Exercise 30")

start_date = datetime.date(2025, 7, 1)
days_added = 0
while days_added < 10:
    start_date += datetime.timedelta(days=1)
    if not start_date.weekday() in (5, 6):
        days_added += 1
print(start_date)
