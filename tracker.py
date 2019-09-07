import requests                             # to make a call on web browser
from bs4 import BeautifulSoup             #gets the data and parses it
import smtplib                             #mail protocol
import time


#function to check the price of a given link
def check_price():
    URL = 'https://www.amazon.com/Acer-i5-8265U-Keyboard-Fingerprint-A515-54-51DJ/dp/B07RF2123Z/ref=sxin_2_ac_d_pm?ac_md=6-2-QWJvdmUgJDQwMA%3D%3D-ac_d_pm&keywords=laptop&pd_rd_i=B07RF2123Z&pd_rd_r=721db590-2b1a-4bc6-8093-1c3a919993e3&pd_rd_w=xHEJr&pd_rd_wg=S5l5l&pf_rd_p=eeff02d5-070a-45ea-a79e-d591974b877e&pf_rd_r=G0HE3T2PS5P1KDP46AKY&psc=1&qid=1567261183&s=gateway'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    page = requests. get(URL, headers=headers)


    soup1 = BeautifulSoup(page.content, 'html.parser')                   #parse everything for us

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    # print(soup.prettify())

    title = soup2.find(id="productTitle").get_text()

    price = soup2.find(id="priceblock_ourprice").get_text()

    #print(title.strip())                                    #.strip removes the space while printing


    converted_price = int(price[1:4])

    if (converted_price >500):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()                                       #commad sent by mail server to another server saying that its trying to access
    server.starttls()
    server.ehlo()

    server.login('{Your email}', '{Your secured app password}')

    subject = 'Hey! The Price Fell Down!'

    body = 'Check the amazon link: https://www.amazon.com/Acer-i5-8265U-Keyboard-Fingerprint-A515-54-51DJ/dp/B07RF2123Z/ref=sxin_2_ac_d_pm?ac_md=6-2-QWJvdmUgJDQwMA%3D%3D-ac_d_pm&keywords=laptop&pd_rd_i=B07RF2123Z&pd_rd_r=721db590-2b1a-4bc6-8093-1c3a919993e3&pd_rd_w=xHEJr&pd_rd_wg=S5l5l&pf_rd_p=eeff02d5-070a-45ea-a79e-d591974b877e&pf_rd_r=G0HE3T2PS5P1KDP46AKY&psc=1&qid=1567261183&s=gateway'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '{Sender Email}',
        '{Receiver Email}',
        msg
    )

    print('Hey the email has been sent')

    server.quit()


while (True):
    check_price()
    time.sleep(120)                                     #number of seconds the app will sleep and check again
