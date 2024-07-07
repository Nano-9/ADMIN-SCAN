# Script feito por: Nano
# Telegram: https://t.me/rdzin9

import os
import sys
import re
import requests
import datetime
import pathlib
from time import sleep
from BanerAdm import BanerAdm

def LimparTela():

	global system
	system = sys.platform

	match system:
		case "win32":
			os.system("cls")
		case "linux":
			os.system("clear")

def ValidEnter(msg=None):

	validar = re.search(r"^(http://|https://){1}(www\.)?([a-zA-Z0-9\-\_])+.+(\.com/|\.br/|\.ch/|\.edu/|\.su/|\.org/|\.sp/\.mg/\.gov/|\.eu/|\.me|\.io|\.pt/|\.tv/|\.uk/|\.ga/|\.ac/|\.mk/|\.co/|\.id/|\.net/|\.uk/|\.jp/|\.in/|\.vn/|\.tr/|\.tw/|\.info/|\.pk/|\.ng/|\.my/|\.sy/|\.bd/|\.cn/|\.gh/|\.se/|\.cyb|\.bbs/|\.geek/|\.chan/|\.vc/|\.pirate/|\.libre/|\.neo/|\.parody/)$", msg, flags=re.IGNORECASE)
	if validar != None:
		return True
	else:
		return False

def ValidWay(way=None):

	way_valid = re.search(r"^((C:\\|/)?)([a-zA-Z0-9])+(\\|/){1}[a-zA-Z0-9]+(\\|/){1}([a-zA-Z0-9])+(\\|/){1}([a-zA-Z0-9])+(\\|/){1}([a-zA-Z0-9])+\.(txt)$", way)
	if way_valid != None:
		return True
	else:
		return False

Persist = requests.Session()

while True:
	BanerAdm()

	try:
		site = str(input("\033[1;32m[+]\033[m \033[1mInforme o site alvo:\033[m "))
	except KeyboardInterrupt:
		raise SystemExit
	else:

		match = False
		Found = False

		options = [

					"Y",
					"N",
					None

		]

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

		verify = ValidEnter(msg=site)
		if not verify:
			print("\033[1;31m[!]\033[m \033[1mVerifique se a url digitada está correta! E não esqueça de adicionar -> / no final da url!\033[m\n")
		else:
			try:
				site_teste = Persist.get(site,headers=headers)
			except requests.ConnectionError:
				print("\033[1;31m[!]\033[m \033[1mO Site não está disponível!\033[m\n")
				sys.exit()
			except KeyboardInterrupt:
				print("\033[1;31m[!]\033[m \033[1mSaindo...!\033[m\n")
				sleep(0.5)
				sys.exit()
			else:
				if site_teste.status_code == 200:
					BanerAdm()
					print("""

\033[1;32m[\033[m \033[1;33m1\033[m \033[1;32m]\033[m \033[1m- Usar Wordlist normal\033[m
\033[1;32m[\033[m \033[1;33m2\033[m \033[1;32m]\033[m \033[1m- Usar Wordlist para Sublinks\033[m
						""")
					try:
						choices = str(input("\033[132mset\033[m> ")).strip()
					except KeyboardInterrupt:
						raise SystemExit
					else:
						if choices == "1":
							BanerAdm()
							size = open("admin.txt","r")
							wordlist_size = len(size.readlines())
							print("\n\033[1;36m[*]\033[m \033[1;32mWordlist carregada com\033[m \033[1;33m{}\033[m \033[1;32mtentativas!\033[m".format(wordlist_size))
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
										pass
									except requests.exceptions.InvalidUrl:
										pass
									else:
										if conectar.status_code == 200:
											finish = datetime.datetime.now() - start
											result = str(finish)
											match = True
											print("\n\033[1;33m-----------------------------\033[m")
											print("\033[1;36M[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
											print("\033[1;36M[INFO]\033[m \033[1;32mAdmin Page:\033[m \033[1m{}\033[m".format(testar))
											print("-----------------------------\033[m\n")
											with open("Found.txt","a") as save1:
												save1.write("-----------------\n")
												save1.write("SITE: {}\n".format(site))
												save1.write("Página de Adm: {}\n".format(testar))
												save1.write("Tempo que levei para encontrar: {}\n".format(result))
												save1.write("-----------------\n")
												save1.close()
										elif conectar.status_code == 401:
											finish = datetime.datetime.now() - start
											result = str(finish)
											match = True
											print("\n\033[1;33m-----------------------------\033[m")
											print("\033[1;36M[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
											print("\033[1;36M[INFO]\033[m \033[1;32mAdmin Page-Js:\033[m \033[1m{}\033[m".format(testar))
											print("-----------------------------\033[m\n")
											with open("Found.txt","a") as save1:
												save1.write("-----------------\n")
												save1.write("SITE: {}\n".format(site))
												save1.write("Página de Adm-Js: {}\n".format(testar))
												save1.write("Tempo que levei para encontrar: {}\n".format(result))
												save1.write("-----------------\n")
												save1.close()
										else:
											print("\033[1;33m[{}]\033[m \033[1;31m[{}]\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar.status_code,testar))
							page.close()
						elif choices == "2":
							try:
								sleep(0.6)
								BanerAdm()
								print("\033[1;33m[{}]\033[m\033[1;32m [*]\033[m \033[1mAbrindo Wordlist de sublinks...\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
								sleep(2)
								caminho_wordlist_2 = os.getcwd()
								resultado = False
								proxies = {"27.54.71.234":"8080"}
								size_subs1 = open("Subdominios.txt","r").readlines()
								print("\033[1;32m[*]\033[m\033[1;32m Wordlist carregada com: \033[m\033[1;33m{}\033[m\033[1;32m tentativas!\033[m".format(len(size_subs1)))
								print("\033[1;32m[*]\033[m\033[1m CTRL+C PARA PARAR O SCRIPT!\033[m\n")
								sleep(2)
							except KeyboardInterrupt:
								raise SystemExit

							for file in os.listdir(str(caminho_wordlist_2)):
								if file == "Subdominios.txt":
									with open(file,"r") as wordlist_2:
										for subdominio in wordlist_2:
											if "www." in site:
												site_2 = site.replace("www.","")
												subd = subdominio.replace("\n","")
												mudar = site_2.split("//")
												resultado = mudar[0]+"//"+subd+"."+mudar[1]
												try:
													conectar3 = Persist.get(resultado,headers=headers)
												except KeyboardInterrupt:
													raise SystemExit
												except requests.exceptions.ConnectionError:
													print("\033[1;32m[{}]\033[m\033[1;31m [403]\033[m\033[1m Site:\033[m \033[1;36m{}\033[m | \033[1mStatus:\033[m \033[1;31mError!\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),resultado))
												except requests.exceptions.InvalidURL:
													pass
												else:
													if conectar3.status_code == 200:
														if "www." not in resultado:
															if "m." not in resultado:
																print("\n\033[1;33m-----------------------------\033[m")
																print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page:\033[m \033[1m{}\033[m".format(resultado))
																print("-----------------------------\033[m\n")
																with open("Found.txt","a") as save2:
																	save2.write("-----------------\n")
																	save2.write("SITE: {}\n".format(site))
																	save2.write("Página de Adm: {}\n".format(resultado))
																	save2.write("-----------------\n")
																	save2.close()
													elif conectar3.status_code == 401:
														if "www." not in resultado:
															if "m." not in resultado:
																print("\n\033[1;33m-----------------------------\033[m")
																print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page-Js:\033[m \033[1m{}\033[m".format(resultado))
																print("-----------------------------\033[m\n")
																with open("Found.txt","a") as save2:
																	save2.write("-----------------\n")
																	save2.write("SITE: {}\n".format(site))
																	save2.write("Página de Adm-Js: {}\n".format(resultado))
																	save2.write("-----------------\n")
																	save2.close()
											else:
												subd = subdominio.replace("\n","")
												mudar = site.split("//")
												resultado2 = mudar[0]+"//"+subd+"."+mudar[1]
												try:
													conectar4 = Persist.get(resultado2,proxies=proxies)
												except requests.exceptions.ConnectionError:
													print("\033[1;32m[{}]\033[m\033[1;31m [403]\033[m\033[1m Site:\033[m \033[1;36m{}\033[m | \033[1mStatus:\033[m \033[1;31mError!\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),resultado2))
												else:
													if conectar4.status_code == 200:
														if "www." not in resultado2:
															if "m." not in resultado2:
																print("\n\033[1;33m-----------------------------\033[m")
																print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page:\033[m \033[1m{}\033[m".format(resultado2))
																print("-----------------------------\033[m\n")
																with open("Found.txt","a") as save3:
																	save3.write("-----------------\n")
																	save3.write("SITE: {}\n".format(site))
																	save3.write("Página de Adm: {}\n".format(resultado2))
																	save3.write("-----------------\n")
																	save3.close()
													elif conectar4.status_code == 401:
														if "www." not in resultado2:
															if "m." not in resultado2:
																print("\n\033[1;33m-----------------------------\033[m")
																print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page:\033[m \033[1m{}\033[m".format(resultado2))
																print("-----------------------------\033[m\n")
																with open("Found.txt","a") as save3:
																	save3.write("-----------------\n")
																	save3.write("SITE: {}\n".format(site))
																	save3.write("Página de Adm: {}\n".format(resultado2))
																	save3.write("-----------------\n")
																	save3.close()
									wordlist_2.close()						
							print("\n\033[1mRetornando ao menu...\033[m")
							sleep(2)
