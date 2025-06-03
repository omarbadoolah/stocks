import unittest
import snp

class TestPurchasingAgent(unittest.TestCase):
	def test_purchasing_agent(self):
		purchaser = snp.PurchasingAgent()
		purchaser.update_snp500_list("sp500.txt")
		purchaser.get_permissibilities("perm.txt")
		purchaser.screen()
		purchaser.rank_by_size()
		purchaser.compute_relative_price()
		self.assertEqual(len(purchaser.snp500), 5)
		self.assertEqual(len(purchaser.candidates), 3)
	