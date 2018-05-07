from PyQt5.QtCore import QSettings


class Config:
	config = QSettings("Betcon")
	default_values = {'stake/percentage': 1.0, 'stake/stake': 0,'stake/type': 1, \
					'interface/coin': '€', 'interface/bookieCountry': 'N'}

	@classmethod
	def value(self, key, type):
		if key in self.default_values:
			return self.config.value(key, self.default_values[key], type)
		else:
			return self.config.value(key, type)

	@classmethod
	def setValue(self, key, value):
		self.config.setValue(key, value)

	@classmethod
	def sync(self):
		self.config.sync()
