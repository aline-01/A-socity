import requests
import time
from bs4 import BeautifulSoup

def whois():
   try:
      target = input("target:")
   except:
      return
   url = "https://whois.com/whois/"+str(target)
   req = requests.get(url)
   

   try:
      input("[+] back to menu ...")
   except:
       pass
