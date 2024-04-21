import os
import json
import math
import requests
from colorama import Fore

# color
color = Fore.RESET

# get cred

# cred = open(r'\\'.join(__file__.split('\\')[:-1])+'\\'+"auth.json")
# cred = json.load(cred)

current_directory = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(current_directory, "auth.json")
cred = json.load(open(cred_path,'r'))

print('')
print(Fore.CYAN+f"ATTENDANCE:{cred['username']}".center(55,' ')+Fore.WHITE)
print('')

# get auth
session = requests.Session()
payload = ""
headers_login = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://rcoem.in/studentCourseFileNew.htm?shwA=^%^2700A^%^27",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}
response = session.request("GET", "https://rcoem.in/login.htm", data=payload, headers=headers_login,auth=(cred['username'],cred['password']))

# get attendence
querystring = {"termId":cred["semester"]}
url = "https://rcoem.in/getSubjectOnChangeWithSemId1.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://rcoem.in/studentCourseFileNew.htm?shwA=^%^2700A^%^27",
    "Cookie": f"JSESSIONID={session.cookies.get_dict()['JSESSIONID']}",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}
response = session.request("GET", url, data=payload, headers=headers, params=querystring)

# print it yeah
totalPresent = 0
totalAbsent = 0
try:
    rjson = response.json()
except:
    print("May be wrong credentials, try again!")
    exit()

for i in rjson:
    currentAbsent = i['absentCount']
    currentPresent = i['presentCount']

    totalPresent += currentPresent
    totalAbsent += currentAbsent

    if currentPresent == currentAbsent == 0:
        currentPercent = 0
    else:
        currentPercent = round(currentPresent*100/(currentPresent+currentAbsent),2)
    
    if currentPercent != 0 and currentPercent < 75:
        color = Fore.RED
    elif currentPercent != 0 and currentPercent > 85:
        color = Fore.GREEN
    else:
        color = Fore.WHITE

    print(color + i['subject'].ljust(35,'-')[:35]+f"{currentPresent}/{currentPresent+currentAbsent}".center(20,'-')+f"{currentPercent}%" + Fore.WHITE)

if totalPresent == totalAbsent == 0:
    totalPercent = 0
else:
    totalPercent = round(totalPresent*100/(totalPresent+totalAbsent),2)

if totalPercent != 0 and totalPercent < 75:
    color = Fore.RED
elif totalPercent != 0 and totalPercent > 90:
    color = Fore.GREEN
else:
    color = Fore.WHITE

print('\n'+rjson[0]['termName'].ljust(55,'-')+f"{totalPercent}%")
print('')

# 75% manager
if totalPercent > 75:
    canAbsent = math.floor((totalPresent - 3*totalAbsent)/3)
    print(Fore.GREEN+f"[+] {canAbsent} classes absentee will reach you 75%"+Fore.WHITE)
elif totalPercent != 0 and totalPercent < 75:
    needPresent = math.ceil(3*totalAbsent-totalPresent)
    print(Fore.RED+f"[+] {needPresent} classes presentee will reach you 75%"+Fore.WHITE)
else:
    print("[+] Absentee is a bad habit")

# let's logout
payload = ""
headers_logout = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://rcoem.in/studentCourseFileNew.htm?shwA=^%^2700A^%^27",
    "Cookie": f"JSESSIONID={session.cookies.get_dict()['JSESSIONID']}",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

response = requests.request("GET", "https://rcoem.in/logout.json", data=payload, headers=headers_logout)
if response.status_code == 200:
    print(Fore.GREEN+'Logout Response:',response,Fore.WHITE)
else:
    print(Fore.YELLOW+'Logout Response:',response,Fore.WHITE)

input("Press Enter to continue..."+Fore.RESET)

