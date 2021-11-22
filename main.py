import requests
import bs4

url = input(r'Please enter the url to the scrapped')
#res = requests.get('https://www.wired.com/story/alphabay-desnake-dark-web-interview/')
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup.title)