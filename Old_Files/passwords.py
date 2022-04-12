import json
from cryptography.fernet import Fernet
import ast
import os
import random
import string

class Main():
	def __init__(self):
		self.rawData = ""
		self.key = ""
		self.data = {}
		self.appInfo = {}
		self.passwords = {}
		self.enterPassword = ""
		self.access = False
		self.wrongPassCount = 0
		self.stringPossa = string.ascii_letters + string.punctuation + string.digits
		self.passwordGen = ""
		self.inputList = ["exit", "add", "platforms", "rm", "aardbei", "gen"]


		with open('passwords.json', 'r') as f:
			self.rawData = f.read()

		self.key = "NAiG15nypSPS6MulN-v7J6SGvOKVcm69FeVCg_fCZGY="

		self.fernet = Fernet(self.key)

	def init(self):
		self.data = self.rawData

		self.appInfo = self.data["App info"]
		self.passwords = self.data["Passwords"]
		self.enterPassword = self.appInfo["Main Password"]

	def decrypt(self, data):
		data = bytes(data, encoding="utf8")

		data = self.fernet.decrypt(data)

		data = data.decode("utf8")

		data = ast.literal_eval(data)

		return data

	def encrypt(self, data):
		data = str(data)

		data = bytes(data, encoding="utf8")

		data = self.fernet.encrypt(data)

		data = data.decode("utf8")

		return data

	def store(self, data):
		with open("passwords.json", "w") as f:
			f.write(data)

	def get_access(self):
		inputPassword = input("Enter password:\n> ")

		if inputPassword == self.enterPassword:
			self.access = True
		else:
			self.wrongPassCount += 1

			print("This is the {} time the pass is wrong. At 5 you will lose the data permanently".format(self.wrongPassCount))

	def add(self):
		plat = input("Platform: ")
		if plat in self.passwords:
			update = input("The platform is already in the system. Do you want to update it? [y/n] ").lower()

			
		else:
			update = "y"

		if update == "y":
			name = input("Name: ")
			passw = input("(Type useGen if you want to use generated password)\nPassword: ")
			if passw == "useGen":

				self.data["Passwords"][plat] = {"Username": name, "Password": self.passwordGen}
			else:
				self.data["Passwords"][plat] = {"Username": name, "Password": passw}
			self.rawData = self.encrypt(self.data)

			self.store(self.rawData)

			print("{} added/updated successfully".format(plat))

		else:
			print("\n")

	def rm(self):
		platf = input('rm > ')

		if platf in self.passwords:
			if input("Do you really want to remove '{}'? [y/n] ".format(platf)).lower() == 'y':
				self.data['Passwords'].pop(platf)
				self.rawData = self.encrypt(self.data)
				self.store(self.rawData)
				print("'{}' removed successfully\n".format(platf))
		else:
			print("'{}' is not in the dictionary".format(platf))

	def gen(self):
		self.passwordGen = "".join(random.choice(self.stringPossa) for x in range(random.randint(8, 13)))

	def main_2(self):
		for i in self.passwords:
			print(i)
		while True:
			self.appInfo = self.data["App info"]
			self.passwords = self.data["Passwords"]
			self.enterPassword = self.appInfo["Main Password"]


			input_ = input("> ")
			if input_.lower() in self.inputList:
				if input_.lower() == "exit":
					break
				if input_.lower() == "add":
					self.add()
				if input_.lower() == "platforms":
					for i in self.passwords:
						print(i)
				if input_.lower() == "rm":
					self.rm()
				if input_.lower() == 'aardbei':
					for i in range(100):
						print("corn")
				if input_.lower() == "gen":
					self.gen()
					print(self.passwordGen)
			elif input_ in self.passwords:
				print("Username: {}\nPassword: {}".format(self.passwords[input_]["Username"], self.passwords[input_]["Password"]))
			else:
				print("Wrong command, or argument is not in the database")



	def main(self):
		while True:
			if self.wrongPassCount <= 4:
				self.get_access()
			else:
				os.remove('key.key')
				print("You lost your data permanently..")
				break

			if self.access == True:
				self.main_2()
				break

		

	def on_execute(self):
		self.rawData = self.decrypt(self.rawData)

		self.init()
		self.gen()
		self.main()



if __name__ == '__main__':
	main = Main()
	main.on_execute()
	
