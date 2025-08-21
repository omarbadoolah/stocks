import unittest
import scraper

class TestScraper(unittest.TestCase):
	def test_scraper(self):
		url = "sp500.html"
		sp500 = scraper.html2csv(url)