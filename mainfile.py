# pandas_identifier
import pandas as pd
import os

class identifier():

	def __init__(self):
		self.identify_field = None

	def policyIDapi(self):
		#code for applying api call on policyID.
		print('performing api calls on policyID')

	def countyapi(self):
		#code for applying api call on county.
		print('performing api calls on county')
		pass

	def identify(self):

		if os.path.isfile('insurance.csv'):	# checks for file path.
			self.policyIDread = pd.read_csv('insurance.csv')
			print(self.policyIDread)

			if 'policyID' == self.policyIDread.columns[0]:
				print('Intializing API Call on Column: PolicyID')
				self.policyIDapi()
				print('')

			# if self.identify_field == None:
			# 	self.couAntyread = pd.read_csv('insurance.csv')
			# 	if 'statecode' in self.countyread:
			# 		print('county found')
			
			if 'county' == self.policyIDread.columns[2]:
				print('Initializing API call on Column: county')
				self.countyapi()

newinstance = identifier()

newinstance.identify()
