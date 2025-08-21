from bs4 import BeautifulSoup

def html2csv(url):
	with open(url, "r") as html_doc: 
		soup = BeautifulSoup(html_doc, 'html.parser')
		
	tables = soup.find_all('table')

	for table in tables:
		rows = table.find_all('tr')
		if len(rows) >= 500:
			with open("sp500.csv", "w") as csv:
				for row in rows:
					cols = row.find_all('td')
					if len(cols) >= 3:
						company = ":".join((cols[1].get_text(), cols[2].get_text(), cols[3].get_text()))
						csv.write(company + "\n")
						
if __name__ == "__main__":
	print("Converting html to csv...")
	html2csv("sp500.html")