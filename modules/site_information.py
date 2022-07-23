import builtwith

def site_information():
   try:
      target = input("target: ")
      if target == "":return
      if not "https" in target and not "http" in target:
        target = "https://"+target
      print("")
   except:
      return
   try:
      site_data = builtwith.parse(target)
      for i in site_data:
         for s in site_data[i]:
            print(i +" : "+ s)
   except:
      print("[!] not found data for this")
  
   try:
       input("[*] back to menu ...")
   except:
       pass
