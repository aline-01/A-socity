import requests
import time

def whois():
    try:
       target = input("target: ")
    except:
       return
    post_data = {"remoteAddress":target}
    try:
       req = requests.post("https://www.yougetsignal.com/tools/whois-lookup/php/get-whois-lookup-json-data.php",data=post_data)
       result = req.text.split("<br \/>")
       result = result[1:-1]
    except:
       print("[!] can't connect to api")
    print("")
    for i in result:
       i = i[2:1000]
       print(i)
       time.sleep(0.1)
    try:
       input("back to menu ...")
    except:
       pass
    
