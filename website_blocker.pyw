import time
from datetime import datetime as dt

host_temp = r'C:\workspace\python\basics\hosts'
host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com']

while True:
    cur = dt.now()
    year = cur.year
    month = cur.month
    day = cur.day
    hour = cur.hour

    time_f = dt(year, month, day, 0) # 12:00 am
    time_s = dt(year, month, day, 7) # 07:00 am

    if time_f < cur < time_s:
        print('working hours {}'.format(cur))
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f'\n{redirect}\t{website}')

    else:
        print('fun hours')
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
