from bs4 import BeautifulSoup
import requests
from datetime import datetime
from time import sleep
import webbrowser
from playsound import playsound
from colored import fg, attr
from mouse import click, move

#User agent
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68"
}

#Colors
Ryzen = fg('#fc4903') ### Color variables
DateColor =  fg('#1a3d38')
r = attr('reset') ### Color reset variable
Green = fg('#10de58')
Red = fg('#b00c0c')
Skytech =  fg('#02f051')
Mindfactory = fg('#0236f0')

#Audio pathing
x5900 = 'C:/Users/viliu/Desktop/Python/bassdrop.mp3'
x5600 = 'C:/Users/viliu/Desktop/Python/bruh.mp3'


#Price
def FindP_M5600():
    global PM5600
    FindPrice_Mindfactory_5600 = body1.find('div',class_='pprice')
    PMn5600 = []
    for letter in FindPrice_Mindfactory_5600.text:
        if letter.isnumeric():
            PMn5600.append(letter)

    PM5600 = f'{PMn5600[0]:1}{PMn5600[1]:1}{PMn5600[2]:1}'

def FindP_M5900():
    global PM5900
    FindPrice_Mindfactory_5900 = body2.find('div',class_='pprice')
    PMn5900 = []
    for letter in FindPrice_Mindfactory_5900.text:
        if letter.isnumeric():
            PMn5600.append(letter)

    PM5900 = f'{PMn5900[0]:1}{PMn5900[1]:1}{PMn5900[2]:1}'

def FindP_S5900():
    global PS5900
    FindPrice_Skytech_5900 = body3.find('span',class_='num')
    PSm5900= FindPrice_Skytech_5900.find('span')
    PSn5900= []
    for letter in PSm5900.text:
        if letter.isnumeric():
            PSn5900.append(letter)

    PS5900 = f'{PSn5900[0]:1}{PSn5900[1]:1}{PSn5900[2]:1}'

#ALERTED FOR STOCK?
M5900 = False
M5600 = False
S5900 = False


#Main
while True:

    now = datetime.now()
    current_time = now.strftime("%#H:%M")

    Mindfactory5600 = requests.get("https://www.mindfactory.de/product_info.php/AMD-Ryzen-5-5600X-6x-3-70GHz-So-AM4-BOX_1380726.html").text
    Mindfactory5900 = requests.get("https://www.mindfactory.de/product_info.php/AMD-Ryzen-9-5900X-12x-3-70GHz-So-AM4-WOF_1380728.html").text
    Skytech5900 = requests.get("http://www.skytech.lt/100100000061wof-amd-ryzen-5900x-box-am4-12c24t-105w-3748ghz-70mb-dezuteje-amd-ne-p-529361.html", headers=headers).text

    HTML1 = BeautifulSoup(Mindfactory5600, 'lxml')
    HTML2 = BeautifulSoup(Mindfactory5900, 'lxml')
    HTML3 = BeautifulSoup(Skytech5900, 'lxml')

    body1 = HTML1.find('body')
    body2 = HTML2.find('body')
    body3 = HTML3.find('body')

    Stock_Mindfactory_5600 = body1.find('h4')
    Stock_Mindfactory_5900 = body2.find('h4')
    Stock_Skytech_5900 = body3.find('span',class_='val')

    #5600x check at Mindfactory
    if M5600 == False:
        try :

            if Stock_Mindfactory_5600.text == "Die angeforderte URL existiert nicht" :
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5600X" + DateColor + " == " + Red + "Not in stock" + " at " + Mindfactory + "[MINDFACTORY]" + r)
                M5600 = False
            else :
                FindP_M5600()
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5600X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5600 + '€' + "]" + DateColor + " at " + Mindfactory + "[MINDFACTORY]" + r)
                webbrowser.open('https://www.mindfactory.de/product_info.php/AMD-Ryzen-5-5600X-6x-3-70GHz-So-AM4-BOX_1380726.html',new=2)
                playsound(x5600)
                M5600 = True
        except :
            FindP_M5600()
            print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5600X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5600 + '€' + "]" + DateColor + " at " + Mindfactory + "[MINDFACTORY]" + r)
            webbrowser.open('https://www.mindfactory.de/product_info.php/AMD-Ryzen-5-5600X-6x-3-70GHz-So-AM4-BOX_1380726.html',new=2)
            playsound(x5600)
            M5600 = True

    else:
        try :

            if Stock_Mindfactory_5600.text == "Die angeforderte URL existiert nicht" :
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5600X" + DateColor + " == " + Red + "Not in stock" + " at " + Mindfactory + "[MINDFACTORY]" + r)
                M5600 = False
            else :
                FindP_M5600()
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5600X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5600 + '€' + "]" + DateColor + " at " + Mindfactory + "[MINDFACTORY]" + r)
                M5600 = True
        except :
            FindP_M5600()
            print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5600X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5600 + '€' + "]" + DateColor + " at " + Mindfactory + "[MINDFACTORY]" + r)
            M5600 = True


    #5900x Check at Mindfactory

    if M5900 == False:
        try :

            if Stock_Mindfactory_5900.text == "Die angeforderte URL existiert nicht" :
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Red + "Not in stock" + " at " + Mindfactory + "[MINDFACTORY]" + r)
                M5900 = False
            else :
                FindP_M5900()
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5900 + '€' + "]" + " at " + Mindfactory + "[MINDFACTORY]" + r)
                webbrowser.open('https://www.mindfactory.de/product_info.php/AMD-Ryzen-5-5600X-6x-3-70GHz-So-AM4-BOX_1380726.html',new=2)
                playsound(x5900)
                M5900 = True
        except :
            FindP_M5900()
            print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5900 + '€' + "]" + " at " + Mindfactory + "[MINDFACTORY]" + r)
            webbrowser.open('https://www.mindfactory.de/product_info.php/AMD-Ryzen-5-5600X-6x-3-70GHz-So-AM4-BOX_1380726.html',new=2)
            playsound(x5900)
            M5900 = True

    else:
        try :

            if Stock_Mindfactory_5900.text == "Die angeforderte URL existiert nicht" :
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Red + "Not in stock" + " at " + Mindfactory + "[MINDFACTORY]" +r)
                M5900 = False
            else :
                FindP_M5900()
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5900 + '€' + "]" + " at " + Mindfactory + "[MINDFACTORY]"  + r)
                M5900 = True
        except :
            FindP_M5900()
            print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PM5900 + '€' +"]" + " at " + Mindfactory + "[MINDFACTORY]" + r)
            M5900 = True

    #5900x check at Skytech

    if S5900 == False:
        try :

            if Stock_Skytech_5900.text == '0':
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Red + "Not in stock" + " at " + Skytech + "[Skytech]" + r)
                S5900 = False
            else :
                FindP_S5900()
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PS5900 + '€' + "]" + "at" + Skytech + "[Skytech]" + r)
                webbrowser.open('http://www.skytech.lt/100100000061wof-amd-ryzen-5900x-box-am4-12c24t-105w-3748ghz-70mb-dezuteje-amd-ne-p-529361.html',new=2)
                playsound(x5900)
                S5900 = True
        except :
            FindP_S5900()
            print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PS5900 + '€' + "]" + " at " + Skytech + "[Skytech]" + r)
            webbrowser.open('http://www.skytech.lt/100100000061wof-amd-ryzen-5900x-box-am4-12c24t-105w-3748ghz-70mb-dezuteje-amd-ne-p-529361.html',new=2)
            playsound(x5900)
            S5900 = True

    else :
        try :

            if Stock_Skytech_5900.text == '0':
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Red + "Not in stock" + " at " + Skytech + "[Skytech]" + r)
                S5900 = False
            else :
                FindP_S5900()
                print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PS5900 + '€' + "]" + " at " + Skytech + "[Skytech]" + r)
                S5900 = True
        except :
            FindP_S5900()
            print(DateColor + "[" + current_time + "]" + Ryzen + " Ryzen-5-5900X" + DateColor + " == " + Green + "IN STOCK " + Ryzen + "[" + PS5900 + '€' + "]" + " at " + Skytech + "[Skytech]" + r)
            S5900 = True
    sleep(60)