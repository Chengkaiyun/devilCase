from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re


def to_integer(dt):
    return dt.year * 10000000000 + dt.month * 100000000 + dt.day * 1000000 + dt.hour * 10000 + dt.minute * 100 + dt.second


runTime = datetime(2020, 5, 31, 23, 59, 59) - datetime(2020, 4,13, 5, 37, 17)
total = runTime.total_seconds()

for i in range(1, int(total)):
    num = to_integer( datetime(2020, 4,13, 5, 37, 17)+ timedelta(seconds=i))
    imgurlK = 'https://i.devilxxxx.com/uploads/products/' + str(num) + '.jpg'
    re = requests.get(imgurlK)
    soup = bs(re.text, "html.parser")

    try:
        check = soup.find("h1")
        output = check.text + " : " + str(num)
        print(output)

    except:
        pic = requests.get(imgurlK)
        img = pic.content
        print(imgurlK)
        name = imgurlK.split("/")[-1]

        with open("img/" + name, 'wb') as pic_out:
            pic_out.write(img)
        continue