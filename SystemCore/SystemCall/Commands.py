class Generate():
	def __init__(self, element, command, eargs: dict):
		self.element = element
		self.command = command
		self.eargs = eargs

	def __str__(self) -> str:
		# debug
		context = self.__dict__
		bigstr = "\n"

		for key, value in context.items():
			bigstr += f"{key} --> {value}\n"

		return bigstr
