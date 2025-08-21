from datetime import date
import time
import json
import yfinance as yf

class Company:
	def __init__(self, name, symbol, weight):
		self.name = name
		self.symbol = symbol
		self.weight = weight

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
			self.snp500.append(Company(name.strip(), symbol.strip(), weight.rstrip("%\n")))
			
	def get_permissibilities(self, file):
		self.permissibilities = {}
		
		with open(file) as fp:
			perms_list = fp.readlines()
			
		for line in perms_list:
			symbol, permissibility = line.split(",")
			self.permissibilities[symbol] = permissibility.strip()
			
	def screen(self):
		self.snp500 = list(filter(lambda company: self.permissibilities.get(company.symbol) == "Halal", self.snp500))
		
	def update(self):
		fetch_time = time.time()
		today = date.today().isoformat()
		symbols = [c.symbol for c in self.snp500]
		p_30d = yf.download(symbols, period = "30d", multi_level_index = False)['Close']
		#self.price = p_30d[-1]
		#price_30_day = p_30d[0]
		p_6mo = yf.download(symbols, period = "180d", multi_level_index = False)['Close']
		#price_6_month = p_6mo[0]
		
		for company in self.snp500:
			company.price = p_30d[company.symbol][-1]
			company.price_30d = p_30d[company.symbol][0]
			company.price_6m = p_6mo[company.symbol][0]
		
	def rank_by_size(self):
		self.snp500.sort(key=lambda company: company.weight, reverse=True)
		
	def compute_relative_price(self):
		self.update()
		#TODO: calculate 30 day and 6 month performance and decide how to store items
		for company in self.snp500:
			company.st_perf = company.price / company.price_30d - 1
			company.lt_perf = company.price / company.price_6m - 1
		
	def choose(self):
		# Choosing will be a manual step for now.
		# This function will display candidates in order of size with their price performance
		for company in self.snp500:
			if company.st_perf < 0 and company.lt_perf >= 0:
				print(f"{company.symbol}\t\t{company.weight}\t{company.price:.2f}\t{company.st_perf:.2f}\t{company.lt_perf:.2f}\t{company.name}")
		return

if __name__ == "__main__":
	print("Starting...")
	purchaser = PurchasingAgent("sp500.csv")
	purchaser.get_permissibilities("perm.txt")
	purchaser.screen()
	purchaser.rank_by_size()
	purchaser.compute_relative_price()
	purchaser.choose()
	
