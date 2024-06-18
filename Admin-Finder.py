# Script feito por: Nano
# Telegram: https://t.me/rdzin9

import os
import sys
import requests
import datetime
from time import sleep

Persist = requests.Session()
os.system("clear")

print("""\033[1;31m
                                       
		  ,---.     ,--.          ,--.         
		 /  O  \  ,-|  |,--,--,--.`--',--,--,  
		|  .-.  |' .-. ||        |,--.|      \ 
		|  | |  |\ `-' ||  |  |  ||  ||  ||  | 
		`--' `--' `---' `--`--`--'`--'`--''--' 
		,------.                        ,--.   
		|  .--. ' ,--,--.,--,--,  ,---. |  |   
		|  '--' |' ,-.  ||      \| .-. :|  |   
		|  | --' \ '-'  ||  ||  |\   --.|  |   
		`--'      `--`--'`--''--' `----'`--'   
                                       \033[m
		   \033[1;33m[*] Coded by: Nano
	           [*] Telegram: https://t.me/rdzin9\033[m

""")

site = str(input("\033[1;32m[+] Informe o site alvo:\033[m "))
wordlists = str(input("\033[1;32m[+] Você deseja utilizar a wordlist padrão? (Y/N)\033[m ")).strip().lower()
match = False
if wordlists == "y":
	print("""\n\033[1;31m####### [!] VARREDURA INICIADA [!] #######\n\033[m
""")
	with open("admin.txt","r") as page:
		for pages in page:
			admin_page = pages.replace("\n","")
			testar = site+admin_page.strip().lower()
			try:
				conectar = Persist.get(testar)
			except KeyboardInterrupt:
				print("[×] Saindo...")
				sleep(0.5)
				sys.exit()
			except requests.ConnectionError:
				print("\033[1;31m[!] url indisponível!\033[m")
				sys.exit()
			else:
				if conectar.status_code == 200:
					print("\033[1;33m[{}]\033[m \033[1;32m[{}] [MATCH] LINK: {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar.status_code,testar))
					match = True
					with open("Páginas-de-admin.txt","a") as save1:
						save1.write("-----------------\n")
						save1.write("SITE: {}\n".format(site))
						save1.write("Página de Adm: {}\n".format(testar))
						save1.write("-----------------\n")
					break
				else:
					print("\033[1;33m[{}]\033[m \033[1;31m[{}] [NOT MATCH] LINK: {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar.status_code,testar))
		page.close()

		if not match:
			print("\n\033[1;33m[{}]\033[m\033[1;31m[NOT FOUND]\033[m \033[1;32mNenhuma página de adminstrador encontrada!\n\033[m")

elif wordlists == "n":
	caminho_wordlist = str(input("\033[1;33m[+] Informe o caminho da wordlist: \033[m")).strip()
	print("""\n\033[1;31m####### [!] VARREDURA INICIADA [!] #######\n\033[m
""")
	try:
		with open(caminho_wordlist,"r") as page2:
			for pages2 in page2:
				admin_page2 = pages2.replace("\n","")
				testar2 = site+admin_page2.strip().lower()
				try:
					conectar2 = Persist.get(testar2)
				except KeyboardInterrupt:
					print("[×] Saindo...")
					sys.exit()
				except requests.ConnectionError:
					print("\033[1;31m[!] url indisponível!\033[m")
					sys.exit()
				else:
					if conectar2.status_code == 200:
						print("\033[1;33m[{}]\033[m \033[1;32m[{}] [MATCH] LINK: {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar2.status_code,testar2))
						match = True
						with open("Páginas-de-admin.txt","a") as save:
							save.write("-----------------\n")
							save.write("SITE: {}\n".format(site))
							save.write("Página de Adm: {}\n".format(testar2))
							save.write("-----------------\n")
						break
					else:
						print("\033[1;33m[{}]\033[m \033[1;31m[{}] [NOT MATCH] LINK: {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar2.status_code,testar2))
			page2.close()
			if not match:
				print("\n\033[1;33m[{}]\033[m\033[1;31m[NOT FOUND]\033[m \033[1;32mNenhuma página de adminstrador encontrada!\n\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))

	except FileNotFoundError:
		print("\033[1;31m[!] Arquivo {} não encontrado!\033[m".format(caminho_wordlist))
		sys.exit()
                                 
