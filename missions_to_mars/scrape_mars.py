from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


browser = Browser('chrome', executable_path="./chromedriver")
url = 'https://redplanetscience.com/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all('div', class_='content_title')
print(title[0].text)

p_text = soup.find_all('div', class_='article_teaser_body')
print(p_text[0].text)

browser = Browser('chrome', executable_path="./chromedriver")
url = 'https://spaceimages-mars.com/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

f_img = soup.find_all('img', class_='headerimage fade-in')
for x in range(len(f_img)):
    print(f_img[x]['src'])

full_url = url+f_img[0]['src']


url = 'https://galaxyfacts-mars.com/'

tables = pd.read_html(url)
tables

df = tables[1]
html_table = df.to_html()

hem_imgs = [{'title': 'Cerberus Hemisphere', 'img_url': 'https://marshemispheres.com/images/full.jpg'},
            {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'},
            {'title': 'Syrtis Major Hemisphere', 'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'},
            {'title': 'VAlees Marineris Hemisphere', 'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'}]