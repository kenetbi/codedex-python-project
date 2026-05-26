import datetime, bday_messages as bdmess

today = datetime.date.today()
next_birthday = datetime.date(2026, 9, 22)


days_away = next_birthday - today

if today == next_birthday:
    print(bdmess.random_message)
else:
    print(f"My next birthday is {days_away.days} days away.")

