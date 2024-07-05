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

	validar = re.search(r"^(http://|https://){1}(www\.)?([a-zA-Z0-9\-\_])+.+(\.com/|\.br/|\.ch/|\.edu/|\.su/|\.org/|\.sp/\.mg/\.gov/|\.eu/|\.me|\.io|\.pt/|\.tv/|\.uk/|\.ga/|\.ac/|\.mk/|\.co/|\.id/|\.net/|\.uk/|\.jp/|\.in/|\.vn/|\.tr/|\.tw/|\.info/|\.pk/|\.ng/|\.my/|\.sy/|\.bd/|\.cn/|\.gh/|\.se/)$", msg, flags=re.IGNORECASE)
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

BanerAdm()

site = str(input("\033[1;32m[+] Informe o site alvo:\033[m "))
wordlists = str(input("\033[1;32m[+] Você deseja utilizar a wordlist padrão? (Y/N)\033[m ")).strip().lower()
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
		site_teste = Persist.get(site)
	except requests.ConnectionError:
		print("\033[1;31m[!]\033[m \033[1mO Site não está disponível!\033[m\n")
		sys.exit()
	except KeyboardInterrupt:
		print("\033[1;31m[!]\033[m \033[1mSaindo...!\033[m\n")
		sleep(0.5)
		sys.exit()
	else:
		if site_teste.status_code == 200:

			if wordlists == "y":

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
							print("\033[1;31m[!] url indisponível!\033[m")
							sys.exit()
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

				if not match:
					BanerAdm()
					print("\033[1;33m[{}]\033[m\033[1;32m [*]\033[m \033[1mAbrindo Wordlist de sublinks...\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
					sleep(1)
					caminho_wordlist_2 = os.getcwd()
					resultado = False
					proxies = {"27.54.71.234":"8080"}
					size_subs1 = open("Subdominios.txt","r").readlines()
					print("\033[1;32m[*]\033[m\033[1;m Wordlist carregada com: {} tentativas!\033[m\n".format(len(size_subs1)))
					sleep(1)
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
										except requests.exceptions.ConnectionError:
											print("\033[1;32m[{}]\033[m\033[1;31m [403]\033[m\033[1m Site:\033[m \033[1;36m{}\033[m | \033[1mStatus:\033[m \033[1;31mError!\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),resultado))
										except requests.exceptions.InvalidURL:
											continue
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
			
			elif wordlists == "n":
				caminho_wordlist = str(input("\033[1;33m[+] Informe o caminho + nome da wordlist: \033[m")).strip()
				exists = ValidWay(way=caminho_wordlist)
				if exists:
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
										match = True
										print("\n\033[1;33m-----------------------------\033[m")
										print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
										print("\033[1;36m[INFO]\033[m \033[1;32mAdmin Page: :\033[m \033[1m{}\033[m".format(testar2))
										print("-----------------------------\033[m\n")
										with open("Found.txt","a") as save:
											save.write("-----------------\n")
											save.write("SITE: {}\n".format(site))
											save.write("Página de Adm: {}\n".format(testar2))
											save.write("Tempo que levei para encontrar: {}\n".format(results))
											save.write("-----------------\n")
											save.close()
									elif conectar2.status_code == 401:
										finishs = datetime.datetime.now() - starts
										results = str(finishs)
										match = True
										print("\n\033[1;33m-----------------------------\033[m")
										print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
										print("\033[1;36m[INFO]\033[m \033[1;32mAdmin Page-Js: :\033[m \033[1m{}\033[m".format(testar2))
										print("-----------------------------\033[m\n")
										with open("Found.txt","a") as save:
											save.write("-----------------\n")
											save.write("SITE: {}\n".format(site))
											save.write("Página de Adm: {}\n".format(testar2))
											save.write("Tempo que levei para encontrar-Js: {}\n".format(results))
											save.write("-----------------\n")
											save.close()
									else:
										print("\033[1;33m[{}]\033[m \033[1;31m[{}]\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar2.status_code,testar2))
							page2.close()
							if not match:
								BanerAdm()
								print("\033[1;33m[{}]\033[m\033[1;32m [*]\033[m \033[1mAbrindo Wordlist de sublinks...\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
								sleep(1)
								caminho_wordlist_2 = os.getcwd()
								resultado = False
								proxies = {"27.54.71.234":"8080"}
								size_subs2 = open("Subdominios.txt","r").readlines()
								print("\033[1;32m[*]\033[m\033[1;m Wordlist carregada com: {} tentativas!\033[m\n".format(len(size_subs2)))
								sleep(1)
								for file in os.listdir(str(caminho_wordlist_2)):
									if file == "Subdominios.txt":
										with open(file,"r") as wordlist_2:
											for subdominio in wordlist_2:
												if "www." in site:
													site_2 = site.replace("www.","")
													subd = subdominio.replace("\n","")
													mudar = site_2.split("//")
													resultado3 = mudar[0]+"//"+subd+"."+mudar[1]
													try:
														conectar3 = Persist.get(resultado3,headers=headers)
													except requests.exceptions.ConnectionError:
														print("\033[1;32m[{}]\033[m\033[1;31m [403]\033[m\033[1m Site:\033[m \033[1;36m{}\033[m | \033[1mStatus:\033[m \033[1;31mError!\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),resultado3))
													except requests.exceptions.InvalidURL:
														continue
													else:
														if conectar3.status_code == 200:
															if "www." not in resultado3:
																if "m." not in resultado3:
																	print("\n\033[1;33m-----------------------------\033[m")
																	print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																	print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page:\033[m \033[1m{}\033[m".format(resultado3))
																	print("-----------------------------\033[m\n")
																	with open("Found.txt","a") as save2:
																		save2.write("-----------------\n")
																		save2.write("SITE: {}\n".format(site))
																		save2.write("Página de Adm: {}\n".format(resultado3))
																		save2.write("-----------------\n")
																		save2.close()
														elif conectar3.status_code == 401:
															if "www." not in resultado3:
																if "m." not in resultado3:
																	print("\n\033[1;33m-----------------------------\033[m")
																	print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																	print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page-Js:\033[m \033[1m{}\033[m".format(resultado3))
																	print("-----------------------------\033[m\n")
																	with open("Found.txt","a") as save2:
																		save2.write("-----------------\n")
																		save2.write("SITE: {}\n".format(site))
																		save2.write("Página de Adm-Js: {}\n".format(resultado3))
																		save2.write("-----------------\n")
																		save2.close()
												else:
													subd = subdominio.replace("\n","")
													mudar = site.split("//")
													resultado4 = mudar[0]+"//"+subd+"."+mudar[1]
													try:
														conectar4 = Persist.get(resultado4,proxies=proxies)
													except requests.exceptions.ConnectionError:
														print("\033[1;32m[{}]\033[m\033[1;31m [403]\033[m\033[1m Site:\033[m \033[1;36m{}\033[m | \033[1mStatus:\033[m \033[1;31mError!\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),resultado4))
													else:
														if conectar4.status_code == 200:
															if "www." not in resultado4:
																if "m." not in resultado4:
																	print("\n\033[1;33m-----------------------------\033[m")
																	print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																	print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page:\033[m \033[1m{}\033[m".format(resultado4))
																	print("-----------------------------\033[m\n")
																	with open("Found.txt","a") as save3:
																		save3.write("-----------------\n")
																		save3.write("SITE: {}\n".format(site))
																		save3.write("Página de Adm: {}\n".format(resultado4))
																		save3.write("-----------------\n")
																		save3.close()
														elif conectar4.status_code == 401:
															if "www." not in resultado4:
																if "m." not in resultado4:
																	print("\n\033[1;33m-----------------------------\033[m")
																	print("\033[1;36m[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
																	print("\033[1;36m[INFO]\033[m \033[1;32mPossível Admin page:\033[m \033[1m{}\033[m".format(resultado4))
																	print("-----------------------------\033[m\n")
																	with open("Found.txt","a") as save3:
																		save3.write("-----------------\n")
																		save3.write("SITE: {}\n".format(site))
																		save3.write("Página de Adm: {}\n".format(resultado4))
																		save3.write("-----------------\n")
																		save3.close()

					except FileNotFoundError:
						print("\033[1;31m[!] Arquivo {} não encontrado!\033[m".format(caminho_wordlist))
						sys.exit()
				else:
					system2 = sys.platform
					if system2 == "win32":
						print("\033[1;31m[!]\033[m \033[1mVerifique se o caminho começa com C:\\\n\033[1;31m[!]\033[m e contém o nome do arquivo com final .txt e tente novamente!\033[m\n")
					elif system == "linux":
						print("\033[1;31m[!]\033[m \033[1mVerifique se o caminho começa com /\n\033[1;31m[!]\033[m e contém o nome do arquivo com final .txt e tente novamente!\033[m\n")
#end
