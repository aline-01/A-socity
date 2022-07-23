import socket
import time
from colorama import Fore

subdomain_array = ['mail', 'mail2', 'www', 'ns2', 'ns1', 'blog', 'localhost', 'm', 'ftp', 'mobile', 'ns3', 'smtp', 'search', 'api', 'dev', 'secure', 'webmail', 'admin', 'img', 'news', 'sms', 'marketing', 'test', 'video', 'www2', 'media', 'static', 'ads', 'mail2', 'beta', 'wap', 'blogs', 'download', 'dns1', 'www3', 'origin', 'shop', 'forum', 'chat', 'www1', 'image', 'new', 'tv', 'dns', 'services', 'music', 'images', 'pay', 'ddrint', 'conc', '']

def cloudflare():
    try:
        target = input("target: ")
    except:
        return
    print("")
    for s in subdomain_array:
        host = s+"."+target
        try:
            ip = socket.gethostbyname(host)
            print(Fore.GREEN+host+"  "+ip + "  bypassed")
        except:
            pass

    try:
        input("back to menu ...")
    except:
        pass
