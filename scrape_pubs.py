import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from splinter import Browser
import pymongo


def pubs_all():

    # Initiate headless driver for deployment
    executable_path1 = {'executable_path': 'geckodriver.exe'}
    browser = Browser('firefox', executable_path1, headless = False)

    # Run all scraping functions and store in dictionary.
    data = {
        "pubs": results
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def pubs_scrape(browser):
    cities = ['Manhattan','Boston', 'Denver', 'Philidelphia', 'San_Francisco', 'New_Orleans']
    executable_path1 = {'executable_path': 'geckodriver.exe'}
    browser = Browser('firefox', executable_path1, headless = False)
    results = {}

    for search_term in cities:
        
        pub_url = f'https://www.yelp.com/search?find_desc=Gastropubs&find_loc={search_term}&sortby=review_count'
        browser.visit(pub_url)

        html = browser.html
        
        url = requests.get(pub_url).text
        soup = bs(url, 'html.parser')

        ul_tag = soup.find('ul', class_='lemon--ul__373c0__1_cxs undefined list__373c0__2G8oH')
        h4_tag = soup.find_all('h4')
        #results = h4_tag
        nyc_ul_tag = soup.find('ul', class_='lemon--ul__373c0__1_cxs undefined list__373c0__2G8oH')
        nyc_h4_tag = soup.find_all('h4')
        nyc_h4_tag
        temp = []
        for i in range(1,6):
            print(nyc_h4_tag[i].text)
            temp.append(nyc_h4_tag[i].text.replace('\xa0','' ))
            # results[search_term] = temp

    return results
