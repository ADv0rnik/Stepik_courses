"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит,
когда с момента исходной даты date пройдет число дней, равное days.
"""

from datetime import date, timedelta

year, month, day  = map(int, input().split())
days = int(input())
start_date = date(year, month, day)
end_date = start_date + timedelta(days=days)
print(end_date.year, end_date.month, end_date.day)