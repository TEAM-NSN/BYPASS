#YOUR FATHER TEAM-NSN
#decompile By TEAM-NSN


# TAKE CEAR ABAL DEC BY TEAM-NSN
import os, re, requests, json, bs4
import sys,time,random
from bs4 import BeautifulSoup as parser
ses=requests.Session()
os.system('clear')
def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
print(""" 	
                   FUCK YOUR SYSTEM BY TEAM-NSN 
   \033[1;91m██╗  ██╗ \033[1;92m █████╗  \033[1;94m███████╗ \033[1;95m █████╗  \033[1;96m███╗   ██╗
   \033[1;91m██║  ██║ \033[1;92m██╔══██╗ \033[1;94m██╔════╝ \033[1;95m██╔══██╗ \033[1;96m████╗  ██║
   \033[1;91m███████║ \033[1;92m███████║ \033[1;94m███████╗ \033[1;95m███████║ \033[1;96m██╔██╗ ██║
   \033[1;91m██╔══██║ \033[1;92m██╔══██║ \033[1;94m╚════██║ \033[1;95m██╔══██║ \033[1;96m██║╚██╗██║
   \033[1;91m██║  ██║ \033[1;92m██║  ██║ \033[1;94m███████║ \033[1;95m██║  ██║ \033[1;96m██║ ╚████║
   \033[1;91m╚═╝  ╚═╝ \033[1;92m╚═╝  ╚═╝ \033[1;94m╚══════╝ \033[1;95m╚═╝  ╚═╝ \033[1;96m╚═╝  ╚═══╝
      BRO DECODE ER MAL PUBLIC KORE DILAM   
  \033[1;92m×××××××××××××××××\033[1;93m××××××××××××××\033[1;92m××××××××××××××××××
  \033[1;32m|     \033[1;33m[✓] CREATED BY\33[0;m   :  \033[1;33mASRAFUL ISLAM HASAN   \033[1;92m|
  \033[1;32m|     \033[1;32m[✓] FACEBOK      : \033[1;34m Hasa N                \033[1;92m|
  \033[1;32m|     \033[1;35m[✓] GITHUB       :  \033[1;35mXNXX               \033[1;92m|
  \033[1;32m|     \033[1;36m[✓] TOOL STATUS  :  \033[1;36mFb Post Auto Share    \033[1;92m|
  \033[1;32m|     \033[1;35m[✓] TEAM         :  \033[1;35mNSN                   \033[1;92m|
  \033[1;32m|     \033[1;36m[✓] TOOL VIRSION :  \033[1;36m XODAI NAH                   \033[1;92m|
  \033[1;92m×××××××××××××××××\033[1;93m×××××××××××××××\033[1;92m×××××××××××××××××


        \033[1;91m PLEASE ENTER COOKIE TO RUN

""")
def login():
	cookie = input("         \033[1;92mEnter Cookie : ")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		menu()
	except:
		os.system("rm token.txt cookie.txt")
		exit(" Login Failed, Cookies or Link Invalid")
def menu():
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
	except:
		login()
	runtxt(f"""\x1b[1;92mLET'S START 

""")
	idt = input("Enter Post Link :")
	limit = int(input("Enter Share Limit :"))
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
		for x in range(limit):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				runtxt(f" \x1b[1;92m{n}. HASAN VAU × DONE [ {data['id']} ]")
			else:
				exit(" Failed To Share, Invalid Token")
	except:
		exit(" Failed To Share, Invalid Token")
		
menu()

