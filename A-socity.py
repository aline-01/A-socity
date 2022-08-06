#-------------------------------------------
#coded by alien-01     (:                  #
#telegram aline0110                        #
#the quitier you become the more able hear #
#-------------------------------------------
import time
import logo
import os
import platform
from modules import ip_information
from modules import site_information
from modules import reverse_ip
from modules import whois
from modules import robots
from modules import admin_finder
from modules import port_scan
from modules import cloudflare

#for detect os
osname = platform.uname()[0]
if osname == "Windows":
   comm = "cls"
elif osname == "Linux" or osname == "Mac":
   comm = "clear"
else:
   pass

while True:
   os.system(comm)
   logo.logo()
   print("[1] Ip Information");time.sleep(0.1)
   print("[2] Site Information");time.sleep(0.1)
   print("[3] whois ");time.sleep(0.1)
   print("[4] reverse ip domain");time.sleep(0.1)
   print("[5] port scan");time.sleep(0.1)
   print("[6] cloudflare bypass")
   print("[7] robot scanner");time.sleep(0.1)
   print("[8] admin page finder");time.sleep(0.1)
   print("[9] exit")
   try:
      module = input(">>")
      module = int(module)
      if module == 1:
        os.system(comm)
        logo.logo()
        ip_information.ip_information()
      if module == 2:
        os.system(comm)
        logo.logo()
        site_information.site_information()
      if module == 3:
        os.system(comm)
        logo.logo()
        whois.whois()
      if module == 4:
        os.system(comm)
        logo.logo()
        reverse_ip.reverse_ip()
      if module == 5:
        os.system(comm)
        logo.logo()
        port_scan.port_scan()
      if module == 6:
        os.system(comm)
        logo.logo()
        cloudflare.cloudflare()
      if module == 7:
        os.system(comm)
        logo.logo()
        robots.robots()
      if module == 8:
        os.system(comm)
        logo.logo()
        admin_finder.admin_finder()
      if module == 9:
        exit()

   except:
      pass
