class Girl:	# Class variable. Any object we create will have this variable by default. Shared among all objects.	gender = 'female'	def __init__(self, name):		# Instance variable. Unique to each object.		self.name = name# All objects will have the gender Female but unique names.s = Girl('Stacy')m = Girl('Mercie')print(s.name)print(s.gender)print(m.name)print(m.gender)