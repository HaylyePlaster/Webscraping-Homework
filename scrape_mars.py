from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import pandas as pd
import numpy as np
import time 
from selenium import webdriver

def scrape():
    # NASA Mars News 

    # URL of page to be scraped
    #!which chromedriver

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    news_html = browser.html
    soup = bs(news_html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text.strip()
    news_title

    # # Retrieve page with the requests module


    news_caption = soup.find('div', class_='article_teaser_body').text.strip()
    news_caption

    # JPL Mars Space Images - Featured Image

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser2 = Browser('chrome', **executable_path, headless=False)

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser2.visit(url)

    # image = browser2.find_by_id('full_image')
    # image.click()

    # featured_image = soup.find("img", class_="fancybox-image")
    # featured_image_url = "https://www.jpl.nasa.gov" + image
    # print(featured_image_url)

    # Find the more info button and click that
    browser2.is_element_present_by_text('more info', wait_time=1)
    browser2.click_link_by_id('full_image')

    # Parse the resulting html with soup
    html = browser2.html
    img_soup = bs(html, 'html.parser')

    # find the relative image url
    img_url_rel = img_soup.find_all('img',class_ ='fancybox-image')
    print(img_url_rel)

    # Use the base url to create an absolute url
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    img_url

    #Mars Weather

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url2)
    weather_html = browser.html
    soup = bs(weather_html, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()
    mars_weather

    #Mars Facts

    url3 = 'https://space-facts.com/mars/'

    tables = pd.read_html(url3)
    tables

    #Mars Hemispheres

    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = bs(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=bs(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})

    mars_hemisphere