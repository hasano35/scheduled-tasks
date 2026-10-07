import datetime as dt
import pandas as pd
import smtplib
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")  # istersen bunu da secret yapabilirsin

today = dt.datetime.today()
month = today.month
day = today.day
today_tuple = (month, day)

data = pd.read_csv('birthdays.csv')
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as f:
        letter_template = f.read()
        letter_template = letter_template.replace("NAME", birthday_person["name"])

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            to_addrs=TO_EMAIL,
            from_addr=MY_EMAIL,
            msg=f'Subject: Birthday Message!\n\n{letter_template}'
        )






