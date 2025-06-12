class SNP500:
	def __init__(self, name, symbol, weight):
		self.name = name
		self.symbol = symbol
		self.weight = weight

class Performance:
	def __init__(self, symbol, weight):
		self.symbol = symbol
		self.weight = weight
		
	def update(self):
		self.price = 25
		price_30_day = 32
		price_6_month = 21
	
class Holding:
	def __init__(self, symbol, shares):
		self.symbol = symbol
		self.shares = shares
	
	def value():
		price = 17
		return price * self.shares
		
class PurchasingAgent:
		
	def __init__(self, file):
		self.snp500 = []
		
		with open(file) as fp:
			snp_list = fp.readlines()
			
		for line in snp_list:
			name, symbol, weight = line.split(":")
			self.snp500.append(SNP500(name.strip(), symbol.strip(), weight.rstrip("%\n")))
			
	def get_permissibilities(self, file):
		self.permissibilities = {}
		
		with open(file) as fp:
			perms_list = fp.readlines()
			
		for line in perms_list:
			symbol, permissibility = line.split(",")
			self.permissibilities[symbol] = permissibility.strip()
			
	def screen(self):
		allowed = list(filter(lambda company: self.permissibilities.get(company.symbol) == "Halal", self.snp500))
		self.candidates = [Performance(company.symbol, company.weight) for company in allowed]
		
	def rank_by_size(self):
		for company in self.candidates:
			company.update()
		self.candidates.sort(key=lambda company: company.weight, reverse=True)
		
	def compute_relative_price(self):
		for company in self.candidates:
			company.update()
		#TODO: calculate 30 day and 6 month performance and decide how to store items
		
	def choose(self):
		# Choosing will be a manual step for now.
		# This function will display candidates in order of size with their price performance
		for company in self.snp500:
			print(vars(company))
		print(self.permissibilities)
		print()
		for company in self.candidates:
			print(vars(company))
		return

if __name__ == "__main__":
	print("Starting...")
	purchaser = PurchasingAgent("sp500.csv")
	purchaser.get_permissibilities("perm.txt")
	purchaser.screen()
	purchaser.rank_by_size()
	purchaser.compute_relative_price()
	purchaser.choose()
	
