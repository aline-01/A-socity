import requests
import time
import socket

def ip_information():
   try:
      target = input("target:")
      if "." in target:
         splited_target = target.split(".")
         if len(splited_target) == 2:
            try:
               target = socket.gethostbyname(target)
            except:
               pass
   except:
      return
   req = requests.get("http://ip-api.com/json/"+target)
   result = req.text.split(",")
   result = result[1:-1]
   print("")
   for r in result:
      r = r.replace("\""," ")
      print(r)
      time.sleep(0.1)
   try:
      print("")
      input(" back to menu ...")
   except:
      return


