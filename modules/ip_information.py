import requests
import time
import socket

def ip_information():
   try:
      target = input("target: ")
      if target == "":return
      if "." in target:
         domain_true = target.split(".")
         if len(domain_true) == 2:
            target = socket.gethostbyname(target)
   except:
       return
   try:
       print("")
       req = requests.get("https://ipapi.co/"+target+"/json/")
       result = req.text.split("\n")
       result = result[1:-1]
       for r in result:
         print(r)
         time.sleep(0.1)
   except:
       print("[!] can't connect to api")
   
   try:
      input("[*] back to menu ...")
   except:
      pass


