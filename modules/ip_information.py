import requests
import time
import socket
import ipapi

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
       info = ipapi.location(target)
       for r in info:
         print(str(r) + " : " + str(info[r]))
         time.sleep(0.1)
   except:
       print("[!] can't connect to api")
   
   try:
      input("[*] back to menu ...")
   except:
      pass


