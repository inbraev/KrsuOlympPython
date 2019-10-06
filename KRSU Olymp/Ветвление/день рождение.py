import calendar
import datetime

d, m = map(int, input().split())

my_date = datetime.date(2016, m, d)
print(calendar.day_name[my_date.weekday()])  # 'Wednesday'
