import shodan
import time
import socket
api_key = "zImpQFaZmz9ezgmSsQ2o8p6BIWFmsEbs"
api_shodan = shodan.Shodan(api_key)

def port_scan():
    try:
       target = input("target: ")
       domain = target.split(".")
       if len(domain) == 2:
          target = socket.gethostbyname(target)
    except:
       pass
    print("")
    try:
       result = api_shodan.host(target)
       ports = result["ports"]
    except:
       print("[!] not found target")
       try: 
          input("[*] back to menu ...")
       except:
          pass
    for r in ports:
      print("[*] "+str(r)+ " open")
      time.sleep(0.2)
    print("")
    try:
       input("[*] back to menu ...")
    except:
       pass
