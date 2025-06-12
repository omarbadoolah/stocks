import unittest
import snp
import scraper

class TestPurchasingAgent(unittest.TestCase):
	def test_purchasing_agent(self):
		purchaser = snp.PurchasingAgent("sp500.csv")
		purchaser.get_permissibilities("perm.txt")
		purchaser.screen()
		purchaser.rank_by_size()
		purchaser.compute_relative_price()
		self.assertGreaterEqual(len(purchaser.snp500), 500)
		self.assertGreaterEqual(len(purchaser.snp500), len(purchaser.candidates))
	