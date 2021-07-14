import selenium
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.firefox.options import Options
import json
import sqlite3
import math
import backend
import sqlite3


options = Options()
# options.headless = True
driver = webdriver.Firefox(options=options,executable_path=GeckoDriverManager().install())


aList =[]

def Start():
    # selenium options


    driver.get("https://www.udemy.com/courses/free/")
    time.sleep(10)

    results = driver.find_element_by_class_name('filter-panel--item-count--2JGx3').text
    course_count = results.split()[0]

    number_of_pages = math.ceil((int(course_count)/16))
    print(number_of_pages)
    # driver.quit()
    Scrape(number_of_pages)

    
def Scrape(number_of_pages):
    for n in range(number_of_pages):
        driver.get("https://www.udemy.com/courses/free/?p={}".format(n))
        time.sleep(10)
        course_cards = driver.find_elements_by_class_name('browse-course-card--link--3KIkQ')
        
     


        for card in course_cards:
            aList.append({
                "link":card.get_attribute('href'),
                "title":card.find_element_by_class_name('course-card--course-title--2f7tE').text,
                "headline":card.find_element_by_class_name('course-card--course-headline--yIrRk').text,
                "instructor":card.find_element_by_class_name('course-card--instructor-list--lIA4f').text,
                "rating":card.find_element_by_class_name('star-rating--rating-number--3lVe8').text,
                "revies":card.find_element_by_class_name('course-card--reviews-text--12UpL').text,
                "image":card.find_element_by_class_name('browse-course-card--image--35hYN').get_attribute("src")
                })

        print("completed page ",n)

    with open('data.json', 'w', encoding='utf-8') as f:
       json.dump(aList, f, ensure_ascii=False, indent=4)

    
         



Start()

driver.quit() 







