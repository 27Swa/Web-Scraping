from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
def getting_books_data(i):
    # getting the number of pages 
    # 1 is the default
    j = 0
    try:
        pages = driver.find_element(By.CLASS_NAME,"current")
        if pages:
            pages = int(pages.text.split(' ')[-1])
    except NoSuchElementException:
        print("This category consists of 1 page only")
        pages = 1
    for s in range(1,pages+1):
        if s != 1:
            url_n = f"https://books.toscrape.com/catalogue/category/books/{l}_{i}/page-{s}.html"
            driver.get(url_n)
            time.sleep(2)

        books1 = driver.find_elements(By.CSS_SELECTOR, '.col-xs-6.col-sm-4.col-md-3.col-lg-3') 

        for book in books1:
            element = book.find_element(By.TAG_NAME,'h3').find_element(By.TAG_NAME,'a')
            x = book.text.split('\n')[1]
            
            # Go to the link to get the number of this book in the stock
            title = element.get_attribute('title')
            href = element.get_attribute('href')
            j+=1
            b_title.append(title)
            b_salary.append(x)
            driver.get(href)
            time.sleep(2)

            ava = driver.find_element(By.CSS_SELECTOR,'.instock.availability').text.split('(')[1].split(' ')[0]
            num_in_stock.append(ava)

            driver.back()
    return j
if __name__ == '__main__':    
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    site = 'https://books.toscrape.com/'

    b_title = []
    b_salary = []
    num_in_stock = []
    categ = []
    driver.get(site)
    time.sleep(2)


    matches = driver.find_elements(by= By.XPATH,value='//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul')

    i = 2
    for m in matches:
        x = m.text.lower()
        x = x.split('\n')
        for l in x:    
            url_n = f"https://books.toscrape.com/catalogue/category/books/{l}_{i}/index.html"
            driver.get(url_n)
            time.sleep(2)
            j = getting_books_data(i)
            categ.extend([l]*j)
            i = i + 1
    
    # storing in csv file
    di = {
        'Title': b_title,
        'Salary': b_salary,
        'Available In Stock': num_in_stock,
        'Category': categ
    }
    df = pd.DataFrame(di)
    df.to_csv("Books.csv",index= False)