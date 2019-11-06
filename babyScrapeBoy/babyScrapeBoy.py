from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

urlBoy = 'https://www.babble.com/pregnancy/1000-most-popular-boy-names/'


# Opens a connection, grabs the page
uClient = uReq(urlBoy)
page_Html = uClient.read()
uClient.close()

# HTML Parsing
page_soup = soup(page_Html, "html.parser")

# Grabs each name
name = page_soup.find('div',{'class':'tm-content-container tm-content-container--wide'})

filename = "babyBoyNames.csv"
f = open(filename, 'w')

headers = 'Names\n'
f.write(headers)

boy = name.main.ol.text

# Need to edit data because of unwanted 'ads' in four names
f.write(boy)


f.close()