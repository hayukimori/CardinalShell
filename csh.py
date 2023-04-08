#!/usr/bin/env python

# BI libs
import os, sys
import readline
from contextlib import suppress

# Color related
from colorama import Fore, Style

# SystemCore
from SystemCore.Elements import *
from SystemCore.Shapes import *
from SystemCore.SystemCall.Commands import *


CLEAR = Style.RESET_ALL
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED


user = "hayukimori"
hostname = "turtle"

class LocalCommands():
	def __init__(self):
		self.commands = {
			'sum': self.sum,
			'divide': self.divide,
			'clear': self.clear_cmd,
			'exit': self.quit_cmd,
			'ls': self.ls,
		}

	def ls(self, *args):
		if len(args) == 0:
			try:
				a = os.listdir()
				for x in a:
					print(x)
			except:
				print(f"Couldn't list `{x}`")
		else:
			for x in args:
				try:
					a = os.listdir(x)
					for d in a:
						print(d)
				except:
					print(f"Couldn't list `{x}`")


	def sum(self, *numbers):
		rest = 0

		for number in numbers:
			rest += float(number)

		print(rest)
		return rest

	def divide(self, *numbers):
		rest = float(numbers[0])

		for number in numbers[1:]:
			rest = float(rest) / float(number)

		print(rest)
		return rest

	def clear_cmd(self, *args):
		os.system("clear")

	def quit_cmd(self, *args):
		exit()

class SystemCallSession():
	def __init__(self):
		self.user = user
		self.PS1: str = f"{self.user}@SYSTEMCALL » "

		self.elements_formats = [
			"BasicShape",
			"VortexShape"
		]

		self.acm = [
			"Discharge",
			"Adhere"
		]

		self.bigclasses = [
			{
				'name': "Generate",
				'cl': Generate
			},
		]

		self.genCommandLine()

	def genCommandLine(self) -> None:
		ar = {}
		cm = ""

		main_command: str = input(self.PS1)
		spmc = main_command.split(" ")
		spmc = [x for x in spmc if x != " "]

		# :: < Element Related Commands > ::
		if len(spmc) == 2:
			mc0 = spmc[0]
			mcarg = spmc[1]

			_ = [x for x in self.bigclasses if mc0 == x['name']]

			if len(_) == 0:
				return

			else:
				while True:

					aof: str = input("(aof) » ")

					if ":" in aof:
						key = aof.split(":")[0].replace(" ", '')
						value = aof.split(":")[1].replace(' ', '')

						ar.update({key: value})

					else:
						if len([x for x in self.acm if x == aof.replace(' ', '')]) == 0:
							key = aof.replace(' ', '')
							value = True

							ar.update({key: value})

						else:
							cm = aof
							break


			fcmd = _[0]['cl'](element=eval(mcarg), command=str(cm), eargs=ar)
			print(fcmd)




# CardinalShell Start
class CardinalShell():
	def __init__(self):

		# Defines user and host

		self.user = None
		self.hostname = None
		self.PS1: str = f"{self.user}@{self.hostname} > "

		self.CDB = LocalCommands()

		# Reloads user and host and start command line
		self.get_vars()
		self.commandline()

	def get_vars(self):
		self.user = user
		self.hostname = hostname

	def update_ps1(self):
		self.PS1: str = f"{GREEN}{self.user}{CLEAR}@{self.hostname} {BLUE}>{CLEAR} "


	def commandline(self):

		self.update_ps1()

		while True:
			try:
				command = input(f"{self.PS1}")
				separated_commands = command.split(";")

				for c in separated_commands:
					realcommand = c.split(" ")
					to_be_removed = {''}

					newcommand = [item for item in realcommand if item not in to_be_removed]
					self.ap_command(newcommand)

			except KeyboardInterrupt:
				print("Log Out.")
				sys.exit(0)




	def ap_command(self, command: list):
		base = ""
		args = ()

		with suppress(IndexError): base = command[0]
		with suppress(IndexError): args = tuple(command[1:])


		if base != "":
			self.corun(base, args)


	def corun(self, base, args):
		# Check if is in local commands
		tries = []
		if base != "SystemCall":
			for com in self.CDB.commands.keys():
				if com == base:
					self.CDB.commands[com](*args)
					tries.append(True)
					break

				else:
					tries.append(False)



			if len(tries) > 0 and any(tries) == False:
				print("SystemCore: Enchanced Element Does'nt exisat.")

		else:
			NGVCOM = SystemCallSession()





if __name__ == "__main__":
	cardinal = CardinalShell()
