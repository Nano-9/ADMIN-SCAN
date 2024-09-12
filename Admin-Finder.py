# Coded by Nano

import os
import sys
import random
import requests
import json
import base64
import hashlib
import datetime
import fake_useragent
import clear_screen
import baner
from bs4 import BeautifulSoup
from time import sleep

class IdentifierHashAndDecrypt:

	def __init__(self,hashes,files=False):

		self.Hash = hashes
		self.NumHeaders = random.randint(0,2)
		self.UserAgent = [fake_useragent.UserAgent()["google chrome"],fake_useragent.UserAgent().firefox,fake_useragent.UserAgent()["safari"]]
		self.Headers = {"User-Agent":self.UserAgent[self.NumHeaders]}
		self.Sessions = requests.Session()
		self.HashType = False
		self.HashDecrypted = False
		self.Sites = True
		self.Files = files
		self.start1 = datetime.dateime.now()


	def ReturnTypeHashes(self):
		
		self.Sessions = requests.Session()
		try:
			self.Connects = self.Sessions.get(f"https://hashes.com/en/api/identifier?hash={self.Hash}",verify=True,headers=self.Headers)
		except requests.exceptions.ConnectionError:
			print("Site temporariamente com problemas, tente novamente mais tarde!")
		except requests.exceptions.SSLError:
			print("Temporariamente indisponível")
			raise SystemExit
		except requests.exceptions.ReadTimeout:
			raise SystemExit
		else:
			try:
				resultadoEmJson = json.loads(self.Connects.text)
				if str(resultadoEmJson["success"]) == "False":
					print("Impossível detectar o tipo de hash, informe uma hash válida!")
				else:
					self.HashType = resultadoEmJson["algorithms"][0]
					return self.HashType
			except:
				pass


# DESCRIPTOGRAFANDO A HASH  MD5
	def DecryptMD5Hashes(self):

		self.start1 = datetime.dateime.now()
		print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m Senha a ser encontrada: {} : {}".format(self.Hash,self.HashType))
		print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m Total de sites para fazer a busca: 3")
		print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m Status: Carregando...\n")

		for x in range(30):
			print(".",end="",flush=True)
			sleep(0.001)

		print("\n")

		self.DecryptMD5Passwords = self.Sessions.get(f"http://www.nitrxgen.net/md5db/{self.Hash}.json",verify=True,headers=self.Headers)
		self.ResultadoDecryptPwd = json.loads(self.DecryptMD5Passwords.text)

		if str(self.ResultadoDecryptPwd["result"]["found"]) == "True":
			self.HashDecrypted = self.ResultadoDecryptPwd["result"]["pass"]

			if self.HashDecrypted:
				print("\033[1;32m[\033[m+\033[1;32m]\033[m \033[1;36mTentativa\033[m\033[1m 1\033[m")
				print("\033[1;32m[\033[m*\033[1;32m] Hash\033[m\033[1m: {}\033[m  \033[1;36m|\033[m  \033[1m{}\033[m".format(self.Hash,self.HashDecrypted))
				self.Sites = False
				self.finish = datetime.dateime.now() - self.start1
				print("Tempo até encontrar: {}".format(self.finish))
		else:

			print("\033[1;32m[\033[m+\033[1;32m]\033[m \033[1;36mTentativa\033[m\033[1m 1\033[m")
			print("\033[1;31m[\33[m*\033[1;31m] Hash:\033[m \033[1m{}\033[m  \033[1;36m|\033[m  \033[1;31mFAIL\033[m\n".format(self.Hash))
			try:
				self.DecryptMD5Passwords = self.Sessions.get(f"https://md5.gromweb.com/?md5={self.Hash}",verify=True,headers=self.Headers)
				self.resultados = self.DecryptMD5Passwords.text
				self.procurar = BeautifulSoup(self.resultados,"html.parser")
				self.achou = self.procurar.find_all("a",{"class":"String"},href=True)
				if self.achou:
					if len(self.achou) > 1:
						self.HashDecrypted = str(self.achou[0]["href"].replace("/?string=","")).strip()
						if self.HashDecrypted:
							print("\033[1;32m[\033[m+\033[1;32m]\033[m \033[1;36mTentativa\033[m\033[1m 2\033[m")
							print("\033[1;32m[\033[m*\033[1;32m] Hash\033[m\033[1m: {}\033[m  \033[1;36m|\033[m  \033[1m{}\033[m".format(self.Hash,self.HashDecrypted))
							self.Sites = False
							self.finish = datetime.dateime.now() - self.start1
							print("Tempo até encontrar: {}".format(self.finish))
					else:
						print("\033[1;32m[\033[m+\033[1;32m]\033[m \033[1;36mTentativa\033[m\033[1m 2\033[m")
						print("\033[1;31m[\33[m*\033[1;31m] Hash:\033[m \033[1m{}\033[m  \033[1;36m|\033[m  \033[1;31mFAIL\033[m\n".format(self.Hash))

			except Exception as e:
				print(e)

			if self.Sites:
				Found = False
				
				try:
					self.conectar = self.Sessions.get("https://decrypt.tools/api/decrypt?hash_string={}&hash_type={}".format(self.Hash,self.HashType.lower()))
					self.ResultadoJson = json.loads(self.conectar.text)
					if str(self.ResultadoJson["messages"]) == "false":
						print("\033[1;32m[\033[m+\033[1;32m]\033[m \033[1;36mTentativa\033[m\033[1m 3\033[m")
						print("\033[1;31m[\33[m*\033[1;31m] Hash:\033[m \033[1m{}\033[m  \033[1;36m|\033[m  \033[1;31mFAIL\033[m\n".format(self.Hash))
					else:
						print("\033[1;32m[\033[m+\033[1;32m]\033[m \033[1;36mTentativa\033[m\033[1m 3\033[m")
						print("\033[1;32m[\033[m*\033[1;32m] Hash\033[m\033[1m: {}\033[m  \033[1;36m|\033[m  \033[1m{}\033[m".format(self.Hash,self.ResultadoJson["messages"]["text"]))
						self.Sites = False
						self.finish = datetime.dateime.now() - self.start1
						print("Tempo até encontrar: {}".format(self.finish))
				except:
					pass
				else:
					sleep(2)
					baner.Banner()
					with open("word1.txt","rt") as passwords:
						try:
							for senhas in passwords:
								transf_pass = "{}".format(senhas.strip().replace("\n","")).encode()
								encode_pass = hashlib.md5(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									raise SystemExit
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
						except UnicodeDecodeError:
							pass
					passwords.close()
					if not Found:
						print("\nAbrindo Wordlist 2....\n")
						sleep(2)
						with open("word2.txt","rt") as passw:
							try:
								for senhas in passw:
									transf_pass = "{}".format(senhas.strip().replace("\n","")).encode()
									encode_pass = hashlib.md5(transf_pass).hexdigest()

									if encode_pass == self.Hash:
										self.finish = datetime.dateime.now() - self.start1
										print("Tempo até encontrar: {}".format(self.finish))
										print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
										exit()
									else:
										print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
							except UnicodeDecodeError:
								pass
						raise SystemExit
					passw.close()
# DESCRIPTOGRAFANDO A HASH  SHA1
	def DecryptSHA1Hashes(self):

		print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m Senha a ser encontrada: {} : {}".format(self.Hash,self.HashType))


		for x in range(30):
			print(".",end="",flush=True)
			sleep(0.01)

		print("\n")
		try:
			self.DecryptMD5Passwords = self.Sessions.get(f"https://sha1.gromweb.com/?hash={self.Hash}",verify=True,headers=self.Headers)
			self.resultados = self.DecryptMD5Passwords.text
			self.procurar = BeautifulSoup(self.resultados,"html.parser")
			self.achou = self.procurar.find_all("a",{"class":"String"},href=True)

			if self.achou:
				if len(self.achou) == 1:
					self.HashDecrypted = False
					print("\033[1;31m[\33[m*\033[1;31m]\033[m\033[1;36m Tentativa\033[m\033[1;36m 1\033[m")
					print("\033[1;31m[\33[m*\033[1;31m] Hash:\033[m \033[1m{}\033[m  \033[1;36m|\033[m  \033[1;31mFAIL\033[m\n".format(self.Hash))

					try:
						self.conectar = self.Sessions.get("https://decrypt.tools/api/decrypt?hash_string={}&hash_type={}".format(self.Hash,self.HashType))
						self.ResultadoJson = json.loads(self.conectar.text)
						if str(self.ResultadoJson["messages"]) == "Hash type not found":
							print("\033[1;31m[\33[m*\033[1;31m]\033[m\033[1;36m Tentativa\033[m\033[1;36m 2\033[m")
							print("\033[1;31m[\33[m*\033[1;31m] Hash:\033[m \033[1m{}\033[m  \033[1;36m|\033[m  \033[1;31mFAIL\033[m\n".format(self.Hash))
						else:
							print("\033[1;31m[\33[m*\033[1;31m]\033[m\033[1;36m Tentativa\033[m\033[1;36m 3\033[m")
							print("\033[1;32m[\033[m*\033[1;32m] Hash\033[m\033[1m: {}\033[m  \033[1;36m|\033[m  \033[1m{}\033[m".format(self.Hash,self.ResultadoJson["messages"]["text"]))
							self.finish = datetime.dateime.now() - self.start1
							print("Tempo até encontrar: {}".format(self.finish))
							raise SystemExit
					except:
						pass
				else:
					self.HashDecrypted = str(self.achou[0]["href"].replace("/?string=","")).strip()
					if self.HashDecrypted:
						print("\033[1;31m[\33[m*\033[1;31m]\033[m\033[1;36m Tentativa\033[m\033[1;36m 1\033[m")
						print("\033[1;32m[\033[m*\033[1;32m] Hash\033[m\033[1m: {}\033[m  \033[1;36m|\033[m  \033[1m{}\033[m".format(self.Hash,self.HashDecrypted))
						self.finish = datetime.dateime.now() - self.start1
						print("Tempo até encontrar: {}".format(self.finish))
						self.Sites = False
			else:
				print("\nMuitas tentativas, espere 60s")
				print("Tentando pelas wordlists....")
				sleep(2)
		except:
			print("\nNão foi possível solicitar os serviços! Tente novamente mais tarde!")
			print("Abrindo wordlists...")
			sleep(2)

		if self.Sites:
			baner.Banner()
			with open("word1.txt","rt") as passwords:
				try:
					for senhas in passwords:
						transf_pass = "{}".format(senhas.strip().replace("\n","")).encode()
						encode_pass = hashlib.sha1(transf_pass).hexdigest()

						if encode_pass == self.Hash:
							print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
							self.finish = datetime.dateime.now() - self.start1
							print("Tempo até encontrar: {}".format(self.finish))
							exit()
						else:
							print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
				except UnicodeDecodeError:
					pass
			print("Abrindo Wordlist 2...")
			sleep(2)
			with open("word2.txt","rt") as passwords:
				try:
					for senhas in passwords:
						transf_pass = "{}".format(senhas.strip().replace("\n","")).encode()
						encode_pass = hashlib.sha1(transf_pass).hexdigest()

						if encode_pass == self.Hash:
							print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
							self.finish = datetime.dateime.now() - self.start1
							print("Tempo até encontrar: {}".format(self.finish))
							exit()
						else:
							print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
				except UnicodeDecodeError:
					pass
			raise SystemExit

	def DecryptOtherHashes(self):
		print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m Senha a ser encontrada: {} : {}".format(self.Hash,self.HashType))

		for x in range(30):
			print(".",end="",flush=True)
			sleep(0.001) 

		print("\n")

		try:
			self.conectar = self.Sessions.get("https://decrypt.tools/api/decrypt?hash_string={}&hash_type={}".format(self.Hash,self.HashType.lower()))
			self.ResultadoJson = json.loads(self.conectar.text)
			if str(self.ResultadoJson["messages"]) == "false":
				print("\033[1;31m[\33[m*\033[1;31m]\033[m\033[1;36m Tentativa\033[m\033[1;36m 1\033[m")
				print("\033[1;31m[\033[m*\033[1;32m] Hash\033[m\033[1m: {}\033[m  \033[1;36m|\033[m  \033[1m{}\033[m".format(self.Hash))
			else:
				print("\033[1;31m[\33[m*\033[1;31m]\033[m\033[1;36m Tentativa\033[m\033[1;36m 1\033[m")
				print("\033[1;32m[\033[m*\033[1;32m] Hash\033[m\033[1m: {}\033[m  \033[1;36m|\033[m  \033[1m{}\033[m".format(self.Hash,self.ResultadoJson["messages"]["text"]))
				self.finish = datetime.dateime.now() - self.start1
				print("Tempo até encontrar: {}".format(self.finish))
				raise SystemExit
		except:
			pass

		if self.Sites:
			Found = False
			baner.Banner()
			with open("word1.txt","rt") as passwords:
				try:
					for senhas in passwords:
						transf_pass = "{}".format(senhas.strip().replace("\n","")).encode()

						if self.HashType.lower() == "sha256":
							encode_pass = hashlib.sha256(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
						elif self.HashType.lower() == "md4":
							encode_pass = hashlib.md4(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))

						elif self.HashType.lower() == "md2":
							encode_pass = hashlib.md2(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
						elif self.HashType.lower() == "sha224":
							encode_pass = hashlib.sha224(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
						elif self.HashType.lower() == "sha384":
							encode_pass = hashlib.sha384(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
						elif self.HashType.lower() == "sha3-256":
							encode_pass = hashlib.sha256(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
						elif self.HashType.lower() == "sha3-224":
							encode_pass = hashlib.sha224(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
						elif self.HashType.lower() == "sha512":
							encode_pass = hashlib.sha512(transf_pass).hexdigest()

							if encode_pass == self.Hash:
								print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
								self.finish = datetime.dateime.now() - self.start1
								print("Tempo até encontrar: {}".format(self.finish))
								exit()
							else:
								print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
				except UnicodeDecodeError:
					pass
			Found = False
			if not Found:
				with open("word2.txt","r") as pwssd:
					try:
						for senhas in pwssd:
							transf_pass = "{}".format(senhas.strip().replace("\n","")).encode()

							if self.HashType.lower() == "sha256":
								encode_pass = hashlib.sha256(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
							elif self.HashType.lower() == "md4":
								encode_pass = hashlib.md4(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))

							elif self.HashType.lower() == "md2":
								encode_pass = hashlib.md2(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
							elif self.HashType.lower() == "sha224":
								encode_pass = hashlib.sha224(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
							elif self.HashType.lower() == "sha384":
								encode_pass = hashlib.sha384(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
							elif self.HashType.lower() == "sha3-256":
								encode_pass = hashlib.sha256(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
							elif self.HashType.lower() == "sha3-224":
								encode_pass = hashlib.sha224(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
							elif self.HashType.lower() == "sha512":
								encode_pass = hashlib.sha512(transf_pass).hexdigest()

								if encode_pass == self.Hash:
									print("\033[1;32m[\033[m\033[1;34m+\033[m\033[1;32m]\033[m \033[1m{}  \033[1;33m|\033[m \033[m \033[1;36m{}\033[m".format(encode_pass,senhas))
									self.finish = datetime.dateime.now() - self.start1
									print("Tempo até encontrar: {}".format(self.finish))
									exit()
								else:
									print("\033[1;31m[\033[m\033[1m-\033[m\033[1;31m]\033[m \033[3m{}\033[m  \033[1;33m|\033[m  \033[3m{}\033[m".format(self.Hash,str(encode_pass)))
					except UnicodeDecodeError:
						pass

			print("Senha não encontrada!\n")
			raise SystemExit

	def DecryptBase64Hashes(self):

		try:
			resposta = base64.b64decode(self.Hash).decode()
		except base64.binascii.Error:
			print("Nenhuma hash encontrada!")
		else:
			print(resposta)
			self.finish = datetime.dateime.now() - self.start1
			print("Tempo até encontrar: {}".format(self.finish))

if __name__ == "__main__":

	matcheswords = ["word1.txt","word2.txt"]
	install = True

	try:
		caminho_script = os.getcwd()
		for wordlists in os.listdir(str(caminho_script)):
			if wordlists.startswith("word"):
				a = wordlists
				if wordlists.replace("\n","").strip() in matcheswords:
					print(wordlists)
					install = False
			else:
				pass
	except:
		pass
	if install:
		baner.Banner()
		print("\033[1m[\033[m\033[1;31m OOOPSS! \033[m\033[1m]\033[m\n")
		print("\033[1;32m[\033[m\033[1;32m!\033[1m]\033[m\033[1m Siga as instruções para configurar o script!\033[m \033[1;32m[\033[m\033[1;32m!\033[1m]\033[m")
		print("\n\033[1;33m[\033[m\033[1m+\033[1;33m]\033[m \033[1;34mPasso\033[m\033[1m 1:\033[m \033[1mInstale 2 das wordlists que deixei no \033[m\033[1;36mREADME\033[m\033[1m na página inicial do script\033[m")
		print("\033[1;33m[\033[m\033[1m+\033[1;33m]\033[m \033[1;34mPasso\033[m\033[1m 2:\033[m \033[1mExtraia a wordlist se ela estiver zipada!\033[m")
		print("\033[1;33m[\033[m\033[1m+\033[1;33m]\033[m \033[1;34mPasso\033[m\033[1m 3:\033[m \033[1mApós a extração, renomeie as Wordlists para word1.txt e word2.txt\033[m")
		print("\033[1;33m[\033[m\033[1m+\033[1;33m]\033[m \033[1;34mPasso\033[m\033[1m 4:\033[m \033[1mColoque as duas dentro aqui da pasta do script\033[m")
		print("\033[1;33m[\033[m\033[1m+\033[1;33m]\033[m \033[1;34mPasso\033[m\033[1m 5:\033[m \033[1mPronto! Agora você já pode utilizar o script!\033[m\n")
		print("\033[1;33m[\033[m\033[1m+\033[1;33m]\033[m \033[1;34mWordlists\033[m\033[1m:\033[m \033[1mhttps://github.com/nano-9/Decrypt\033[m")
		print("\n\033[1;33m[\033[m\033[1m+\033[1;33m]\033[m \033[1;34mCriador\033[m\033[1m: Nano\033[m\n")
		raise SystemExit
	lista_separet = ["md5","sha1","base64 encoded string"]
	clear_screen.Clear()
	baner.Banner()
	EntradaUser = sys.argv
	if len(EntradaUser) == 2:
		inicial = IdentifierHashAndDecrypt(hashes=sys.argv[1].strip())
		hashest = inicial.ReturnTypeHashes()
		if hashest != None:
			if hashest.lower() == "md5":
				inicial.DecryptMD5Hashes()
			elif hashest.lower() == "sha1":
				inicial.DecryptSHA1Hashes()
			elif hashest.lower() == "base64 encoded string":
				inicial.DecryptBase64Hashes()
			elif hashest.lower() not in lista_separet:
				inicial.DecryptOtherHashes()
	else:
		print("Use: python hash.py SUA HASH AQUI")
