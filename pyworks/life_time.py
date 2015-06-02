import datetime

today = datetime.date.today()
birthday = datetime.date(1975,6,18)
life = today - birthday
print(life.days)
