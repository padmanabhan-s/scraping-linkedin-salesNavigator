from selenium import webdriver    # to  control the chrome browser
import time
from bs4 import BeautifulSoup     # to parse the page source
import pandas as pd                # to create csv file of scraped user details
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Alpha\\AppData\\Local\\Google\\Chrome\\User Data\\linkedin")
bro = webdriver.Chrome(chrome_options=options)    # creating chrome instance
record=[]
print("ENTER THE FILENME WHERE LINKS ARE STORED")  # filename where the url of user to be scraped are stored
file_name_link=str(input())
file=open(file_name_link+".txt","r")
print("ENTER THE FILENAME TO STORE LEADS")          # filename to store the details of the users
file_name=str(input())                               
for i in file:
    bro.get(str(i))             
    bro.implicitly_wait(15)                         # wait until the page load fully
    time.sleep(3)
    ss=bro.page_source                              # getting page source from selenium
    soup=BeautifulSoup(ss,'html.parser')            # parsing the page source with a html parser of Beautiful Soup
    time.sleep(1)
    try:
        names=soup.find("span",{"class":"profile-topcard-person-entity__name Sans-24px-black-90%-bold"})
        name=names.text
    except:
        name="NO"
    try:
        desination=soup.find("dd",{"class":"mt2"})
        desgination=desination.text
        designation=desination.text
    except:
        designation="NO"
        
    contacts=soup.findAll("a",{"class":"profile-topcard__contact-info-item-link inverse-link-on-a-light-background t-14"})
    try:
        website=contacts[0].get("href")
    except:
        website="No"
    try:
        twitter=contacts[1].get("href")
    except:
       twitter="No"
    
    record.append((name,desgination,website,twitter,i))         # temporariy storing a user details in a list 
    df=pd.DataFrame(record,columns=['name','desgination','website','twitter','salesnavigator-link']) 
    df.to_csv(file_name + '.csv',index=False,encoding='utf-8')   # copy user's details from the list to the file
    

        
