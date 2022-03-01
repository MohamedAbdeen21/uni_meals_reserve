import requests
import re

#Enter your login information
email = ""
password = ""

#the urls that the requests are sent to
url = "https://ejust-campus.ejust.edu.eg/login"
url2 = "https://ejust-campus.ejust.edu.eg/add/applicant/nutrition/reservation/save"

#Start the session
session = requests.Session()
ses = session.get(url)

#find the token 
token = re.findall('value="(.+?)"',ses.text)
btoken = bytes(token[0], 'utf-8')

#Send the login info then the meals order
r = session.post(url,data={"email":email,"password":password,"_token":btoken})
q = session.post(url2,data={"_token":btoken,"breakfast_meal": "1", "lunch_meal": "1", "dinner_meal": '1',"_token":btoken})

if r.status_code == 200 and q.status_code == 200:
    print("DONE")
else:
    print("Error:",r,q)
