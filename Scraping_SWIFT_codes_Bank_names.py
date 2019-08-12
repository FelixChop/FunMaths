import os
import bs4
import requests
import pandas as pd

PATH = os.path.join("C:\\","Users","frevert","Documents","py")

def table_to_df(table):
	return pd.DataFrame([[td.text for td in row.findAll('td')] for row in table.tbody.findAll('tr')])

def next_page(soup):
	return "http:" + soup.find('a', attrs={'rel':'next'}).get('href')

res = pd.DataFrame()
url = "http://bank-code.net/country/FRANCE-%28FR%29/"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
headers = { 'User-Agent' : user_agent }
counter = 0

while True:
	print(counter)
	page = requests.get(url, headers=headers)
	soup = bs4.BeautifulSoup(page.content, 'lxml')
	table = soup.find(name='table', attrs={'id':'tableID'})
	res = res.append(table_to_df(table))
	res.to_csv(os.path.join(PATH,"BIC","table.csv"), index=None, sep=';', encoding='iso-8859-1')
	url = next_page(soup)
	counter += 1
