from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
import random

title = input("Please enter the title you want to scrape entries from: ")
title = title.upper()
title = title.lower()
title_placeholder = title
title = title.replace(" ", "%20")
headers = {"User-Agent": "USER_AGENT"}
URL2 = "https://eksisozluk.com/" + str(title)
r_title = requests.get(URL2, headers=headers)
soup_title = bs(r_title.content, "lxml")
cutt1 = soup_title.find("div", attrs={"id": "topic"})
link_title_tail = cutt1.a.get("href")
link_title_head = "https://eksisozluk.com"
link_title = link_title_head + link_title_tail + "?p=1"
cutt2 = soup_title.find("div", attrs={"class": "clearfix sub-title-container"})
try:
    cutt3 = cutt2.find("div", attrs={"class": "pager"})
    cutt3 = str(cutt3)
    cutt3 = cutt3[:-8]
    cutt3 = cutt3[56:]
    page_count = int(cutt3)
    approximate_dur = page_count * 2.5
except:
    approximate_dur = 2.5

if approximate_dur < 60:
    print()
    print("This will take approximately", round(approximate_dur), "seconds. Would you like to proceed?")
elif 60 <= approximate_dur < 3600:
    approximate_dur = approximate_dur / 60
    print()
    print("This will take approximately", round(approximate_dur), "minutes. Would you like to proceed?")
else:
    approximate_dur = approximate_dur / 3600
    print()
    print("This will take approximately", round(approximate_dur), "hours. Would you like to proceed?")
print()
prompt_1 = input()
if prompt_1 == "yes":

    URL = str(link_title)[:-1]
    URL_prima = URL

    if approximate_dur == 2.5:
        page_limit = 0
    else:
        page_limit = page_count
    entries = []
    timestamps = []
    counter = 0

    for i in range(1, page_limit + 1):

        time.sleep(random.uniform(2, 3))

        URL += str(i)

        r = requests.get(URL, headers=headers)
        soup = bs(r.content, "lxml")

        cut1 = soup.find("ul", attrs={"id": "entry-item-list"})
        cut2 = cut1.find_all("div", attrs={"class": "content"})
        for entry in cut2:
            counter += 1
            entry = entry.text.strip()
            entries.append(entry)
            print("number of entries saved: ", counter)
        cut3 = cut1.find_all("a", attrs={"class": "entry-date permalink"})
        for date_time in cut3:
            date_time = date_time.text.strip()
            timestamps.append(date_time)

        URL = URL_prima

    df_entries = pd.DataFrame(entries)
    df_timestamps = pd.DataFrame(timestamps)
    df = pd.concat([df_entries, df_timestamps], axis="columns")
    file_name = title_placeholder + ".csv"
    df.to_csv(file_name, encoding="utf-8-sig")
    print()
    print("Your data is ready. Would you like to download it?")
    prompt_2 = input()

    if prompt_2 == "yes":
        from google.colab import files

        files.download(file_name)
    else:
        print()
        print("Thank you for using our service.")

else:
    print()
    print("Thank you for using our service.")