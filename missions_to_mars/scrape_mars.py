from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
        
    browser = Browser('chrome', executable_path="./chromedriver")
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all('div', class_='content_title')

    p_text = soup.find_all('div', class_='article_teaser_body')

    browser = Browser('chrome', executable_path="./chromedriver")
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    f_img = soup.find_all('img', class_='headerimage fade-in')
    f_url = url+f_img[0]['src']


    url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url)

    df = tables[1]
    html_table = df.to_html(index=False,header=False,classes="table table-striped table-dark")

    hem_imgs = [{'title': 'Cerberus Hemisphere', 'img_url': 'https://marshemispheres.com/images/full.jpg'},
                {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'},
                {'title': 'Syrtis Major Hemisphere', 'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'},
                {'title': 'Valles Marineris Hemisphere', 'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'}]



    mars_data = [{'news_title': title[0].text,
                 'news_content': p_text[0].text,
                 'featured_image': f_url,
                 'mars_table': html_table,
                 'hemi_pics': hem_imgs}]

    browser.quit()

    return mars_data

