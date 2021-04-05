import requests
from bs4 import BeautifulSoup as bs
import time
import smtplib

URL = input("Please enter the URL of the book you want checked: ")

waiting_interval = 540 # in seconds

headers = {"User-Agent":"USER-AGENT"}
r = requests.get(URL,headers=headers)
soup = bs(r.content,"lxml")
cut1 = soup.find("td",attrs={"width":"24%"})
availability = cut1.text.strip()
author = soup.find("td",attrs={"class":"bibInfoData"})
author = author.text.strip()
title = soup.find("strong").text.strip()

def send_email():

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("testing.smtpdev","*testing123*")

    subject = str(title)+" is now available!"
    body = "Check "+str(URL)+" for details."

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail("testing.smtpdev@gmail.com",to_address,message)

    print("success! e-mail has been sent to",to_address,".")

    server.quit()

if availability == "AVAILABLE":
    print(title,"is available. Check",URL,"for details.")
else:
    print(title,"is",availability,". Would you like to be notified when it's available?")
    response = input("Please respond with 'yes' or 'no'.: ")
    if response=="yes":
        to_address = input("Please enter your e-mail address: ")
        print("You will be notified once",title,"is available.")
        while availability != "AVAILABLE":

            time.sleep(waiting_interval)
            r = requests.get(URL, headers=headers)
            soup = bs(r.content, "lxml")
            cut1 = soup.find("td", attrs={"width": "24%"})
            availability = cut1.text.strip()

        send_email()
    else:
        print("Thank you for using our service. ")





