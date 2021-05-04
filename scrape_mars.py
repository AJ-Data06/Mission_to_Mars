from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import pymongo
import time
import pandas as pd
def scrape():

    

    mars_dic ={}

    #part01
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)

    


    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find_all('div', class_='content_title')[0].find('a').text.strip()
    para = soup.find_all('div', class_='rollover_description_inner')[0].text.strip()
    

    
    mars_dic["title"] = title
    mars_dic["para"] = para


    

    #part02

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url)

    html = browser.html
    soup1 = BeautifulSoup(html, 'html.parser')

    featured_image_url = soup1.find('img', class_="headerimage fade-in")["src"]
    full_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + featured_image_url

    mars_dic["featured_image_url"] = full_url
    

    browser.quit()

    

    #part03

    url1 = 'https://space-facts.com/mars/'
    mars_table = pd.read_html(url1)

    df = mars_table[0]
    df.columns = ['Description','Mars']
    df.set_index('Description', inplace=True)
    table = df.to_html(classes='table-striped table-dark')
    mars_dic["df"] = table

    

    #part04

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url2)

    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    mars_hemis=[]
    for i in range (4):
        time.sleep(1)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemis.append(dictionary)
        browser.back() 

    mars_dic["mars_hemis"] = mars_hemis

    browser.quit()

    return mars_dic
    






