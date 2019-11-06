from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

urlGirl = 'https://www.babble.com/pregnancy/1000-most-popular-girl-names/'


# Opens a connection, grabs the page
uClient = uReq(urlGirl)
page_Html = uClient.read()
uClient.close()

# HTML Parsing
page_soup = soup(page_Html, "html.parser")

# Grabs each name
name = page_soup.find('div',{'class':'tm-content-container tm-content-container--wide'})

filename = "babyGirlNames.csv"
f = open(filename, 'w')

headers = 'Names\n'
f.write(headers)

girl = name.main.ol.text

# Need to edit data because of unwanted 'ads' in four names
f.write(girl.replace('Related PostBiblical Girl Names That Truly Are Timeless', ' ')) 


f.close()