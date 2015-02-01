class Place():
	def __init__(self, name, description, latitude, longitude, update):
		self.name = name
		self.description = description
		self.latitude = latitude
		self.longitude = longitude
		self.update = update
		self.format_coordinates()

	def __str__(self):
		return str('Namn: ' + self.name + '\nBeskrivning: ' + self.description + '\nKoordinater: ' + self.latitude + ', ' + self.longitude + '\nSenast uppdaterad: ' + self.update)

	def format_coordinates(self):
		self.latitude = self.latitude[:2] + '°' + self.latitude[2:4] + '\'' + self.latitude[4:] + '\"'
		self.longitude = self.longitude[:2] + '°' + self.longitude[2:4] + '\'' + self.longitude[4:] + '\"'