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
		   \033[31m[*]\033[m\033[1m Scaner login admin pages in websites\033[m
		   \033[31m[*]\033[m\033[1m Coded by: Nano\033[m
	           \033[31m[*]\033[m\033[1m Telegram: https://t.me/rdzin9\033[m

			      \033[1mVersion 1.1\033[m

""")

site = str(input("\033[1;32m[+] Informe o site alvo:\033[m "))
wordlists = str(input("\033[1;32m[+] Você deseja utilizar a wordlist padrão? (Y/N)\033[m ")).strip().lower()
match = False



headers = {

'user-agent': 'Googlebot'
                      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.103 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 6.1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 6.1; rv:45.0)'
                      'Gecko/20100101 Firefox/45.0'
}




if wordlists == "y":

	size = open("admin.txt","r")
	wordlist_size = len(size.read())
	print("\n\033[1;36m[*]\033[m \033[1;32mCarregado\033[m \033[1;33m{}\033[m \033[1;32murl na wordlist!\033[m".format(wordlist_size))
	size.close()
	sleep(1)
	print("\033[1;36m[*] \033[m\033[1;32mIniciado as\033[m \033[1;33m{}\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
	start = datetime.datetime.now()
	with open("admin.txt","r") as page:
		for pages in page:
			admin_page = pages.replace("\n","")
			testar = site+admin_page.strip().lower()
			try:
				conectar = Persist.get(testar,headers=headers)
			except KeyboardInterrupt:
				print("[×] Saindo...")
				sleep(0.5)
				sys.exit()
			except requests.ConnectionError:
				print("\033[1;31m[!] url indisponível!\033[m")
				sys.exit()
			else:
				if conectar.status_code == 200:
					finish = datetime.datetime.now() - start
					result = str(finish)
					print("\033[1;33m[{}]\033[m \033[1;32m[{}]\033[m\033[1m {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar.status_code,testar))
					print("\n\033[1mTempo que levou para achar a página: \033[m \033[36m[{}]\033[m\n".format(result[0:7]))
					match = True
					with open("Páginas-de-admin.txt","a") as save1:
						save1.write("-----------------\n")
						save1.write("SITE: {}\n".format(site))
						save1.write("Página de Adm: {}\n".format(testar))
						save1.write("-----------------\n")
					break
				else:
					print("\033[1;33m[{}]\033[m \033[1;31m[{}]\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar.status_code,testar))
		page.close()

		if not match:
			print("\n\033[1;33m[{}] \033[m\033[1;31m[NOT FOUND]\033[m \033[1;32mNenhuma página de adminstrador encontrada!\n\033[m".format(datetime.datetime.now().strftime("%H:%M:S")))

elif wordlists == "n":
	caminho_wordlist = str(input("\033[1;33m[+] Informe o caminho da wordlist: \033[m")).strip()
	size2 = open(caminho_wordlist,"r")
	wordlist_size2 = len(size2.read())
	print("\n\033[1;36m[*]\033[m \033[1;32mCarregado\033[m \033[1;33m{}\033[m \033[1;32murl na wordlist!\033[m".format(wordlist_size2))
	size2.close()
	print("\033[1;36m[*] \033[m\033[1;32mIniciado as\033[m \033[1;33m{}\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
	starts = datetime.datetime.now()
	try:
		with open(caminho_wordlist,"r") as page2:
			for pages2 in page2:
				admin_page2 = pages2.replace("\n","")
				testar2 = site+admin_page2.strip().lower()
				try:
					conectar2 = Persist.get(testar2,headers=headers)
				except KeyboardInterrupt:
					print("[×] Saindo...")
					sys.exit()
				except requests.ConnectionError:
					print("\033[1;31m[!] url indisponível!\033[m")
					sys.exit()
				else:
					if conectar2.status_code == 200:
						finishs = datetime.datetime.now() - starts
						results = str(finishs)
						print("\033[1;33m[{}]\033[m \033[1;32m[{}]\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar2.status_code,testar2))
						print("\n\033[1mTempo que levou para achar a página: \033[m \033[36m[{}]\033[m\n".format(results[0:7]))
						match = True
						with open("Páginas-de-admin.txt","a") as save:
							save.write("-----------------\n")
							save.write("SITE: {}\n".format(site))
							save.write("Página de Adm: {}\n".format(testar2))
							save.write("-----------------\n")
						break
					else:
						print("\033[1;33m[{}]\033[m \033[1;31m[{}]\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar2.status_code,testar2))
			page2.close()
			if not match:
				print("\n\033[1;33m[{}]\033[m\033[1;31m[NOT FOUND]\033[m \033[1;32mNenhuma página de adminstrador encontrada!\n\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))

	except FileNotFoundError:
		print("\033[1;31m[!] Arquivo {} não encontrado!\033[m".format(caminho_wordlist))
		sys.exit()
