import requests
import time
import json

def reverse_ip():
   try:
      target = input("target:")
   except:
      pass
   if "https://" in target or "http://" in target:
      print("[!] please include http") 
      time.sleep(2)
      return
   try:
      post_data = {"remoteAddress":target}
      req = requests.post("https://domains.yougetsignal.com/domains.php",data=post_data)
      source = json.loads(req.text)
      print("")
      if source["status"] != "Success":
         print("[!] Daily reverse IP check limit reached")
      else:
         for s in source["domainArray"]:
           print(s[0])
           time.sleep(0.1)
   except:
      print("[!] can't to connect api")
   try:
      input("[*] back to menu ... ")
   except:
      pass
     
