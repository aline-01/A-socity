import requests
import time
from colorama import Fore

search_array = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

def robots():
    try:
      target = input("target: ")
    except:
      return
    if not "https://" in target and not "http://" in target:
        target = "https://"+target
    try:
       print("")
       for i in search_array:
          target_url = target+"/"+i
          req = requests.get(target_url)
          if req.status_code == 200:
             print(Fore.GREEN+target_url)
          else:
             print(Fore.RED+target_url)
    except:
       input("[*] back to menu ...");pass
    try:
       input("[*] back to menu ...")
    except:
       pass


