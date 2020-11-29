import json
import smtplib
import datetime
import requests
from time import localtime, strftime, sleep
from bs4 import BeautifulSoup
from playsound import playsound
from colorama import init, Fore, Back, Style
init()

# loading json file
product = open("Product-Info.json", "r")
p_info = product.read()
p_data = json.loads(p_info)
user = open("User-Info.json", "r")
u_info = user.read()
u_data = json.loads(u_info)

# data for sms and email
list = u_data["USER-INFO"]
for i in range(len(list)):
    email = list[i].get("EMAIL")
    ass = list[i].get("PASS")
    pemail = list[i].get("PEMAIL")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo
server.login(email, ass)


# web checker
def checker():
    num = 0
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    while True:
        # misc data
        cur_time = strftime(Fore.WHITE + "%I:%M:%S:", localtime())
        
        # getting product info
        list = p_data["GPU" + str(num)]
        for i in range(len(list)):
            store = list[i].get("STORE")
            gpu = list[i].get("GPU")
            link = list[i].get("LINK")
            ind = list[i].get("IND")
            type = list[i].get("TYPE")
            sot = list[i].get("SOT")
            at = list[i].get("AT")
        
        # bs4 data
        page = requests.get(link, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if type == "class_":
            avail = soup.find(class_ = ind).text
        elif type == "style":
            avail = soup.find(style = ind).text

        # checking product status
        if avail == sot:
            print(cur_time, "::", Fore.BLUE + store, Fore.WHITE +  
                "(" , num, ")", Fore.CYAN + gpu, Fore.WHITE + "::", Fore.RED + "Sold-Out")
            print(Fore.WHITE + "------------------------------------------------------------------")
            print(Style.RESET_ALL)
        elif avail == at:
            print(cur_time, "::", Fore.BLUE + store, Fore.WHITE +  
                "(" , num, ")", Fore.CYAN + gpu, Fore.WHITE + "::", Fore.GREEN + "Available")
            print(Fore.WHITE + "------------------------------------------------------------------")
            print(Style.RESET_ALL)
            msg(gpu, link)
            send_email(gpu, link)
            print(Fore.GREEN + "Sent!") 
            playsound("Alert.mp3")
        elif avail != sot or at:
            print(Fore.RED + "ERROR: Unkown STATUS")
            error_msg()
        
        # incremental counter for json array
        num += 1
        if num == len(p_data):
            num = 0

        sleep(5)
    return gpu, link

# sms messaging
def msg(gpu, link):
    subject = ""
    body = (gpu, " is now available at:")
    msg = f"subject: {subject}\n\n{body}"

    subject_2 = ""
    body_2 = link
    msg_2 = f"subject: {subject_2}\n\n{body_2}"

    server.sendmail(email, pemail, msg)
    server.sendmail(email, pemail, msg_2)

# sms message for error
def error_msg():
    subject = ""
    body = "ERROR: Unkown STR"
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(email, pemail, msg)

# email messaging
def send_email(gpu, link):
    # msg data
    subject = (gpu, " is Now Available!")
    body = (gpu, " is now available at: ", link)
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
    email,
    email,
    msg)

# may not implement
def autobuy():
    pass
   
checker()