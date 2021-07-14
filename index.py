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
options.headless = True
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
    for n in range(2):
        driver.get("https://www.udemy.com/courses/free/?p={}".format(n))

        # driver.set_window_size(1880, 1049)
        time.sleep(10)
        # total_available = driver.find_element_by_class_name('filter-panel--item-count--2JGx3')
        course_cards = driver.find_elements_by_class_name('browse-course-card--link--3KIkQ')
        
        # course-card--course-meta-info--1hHb3


        for card in course_cards:
            search_command(
                card.get_attribute('href'),
                card.find_element_by_class_name('course-card--course-title--2f7tE').text,
                card.find_element_by_class_name('course-card--course-headline--yIrRk').text,
                card.find_element_by_class_name('course-card--instructor-list--lIA4f').text,
                card.find_element_by_class_name('star-rating--rating-number--3lVe8').text,
                card.find_element_by_class_name('course-card--reviews-text--12UpL').text
            )

            # print({
            #     "link":card.get_attribute('href'),
            #     "title":card.find_element_by_class_name('course-card--course-title--2f7tE').text,
            #     "headline":card.find_element_by_class_name('course-card--course-headline--yIrRk').text,
            #     "instructor":card.find_element_by_class_name('course-card--instructor-list--lIA4f').text,
            #     "rating":card.find_element_by_class_name('star-rating--rating-number--3lVe8').text,
            #     "revies":card.find_element_by_class_name('course-card--reviews-text--12UpL').text
            #     })

            aList.append({
                "link":card.get_attribute('href'),
                "title":card.find_element_by_class_name('course-card--course-title--2f7tE').text,
                "headline":card.find_element_by_class_name('course-card--course-headline--yIrRk').text,
                "instructor":card.find_element_by_class_name('course-card--instructor-list--lIA4f').text,
                "rating":card.find_element_by_class_name('star-rating--rating-number--3lVe8').text,
                "revies":card.find_element_by_class_name('course-card--reviews-text--12UpL').text
                })
    

    # with open('data.json', 'w', encoding='utf-8') as f:
    #    json.dump(aList, f, ensure_ascii=False, indent=4)
         

def search_command(link,title,headline, instructor,rating,review):
    
    for row in backend.search(title,instructor):
        if row:
            print("it exists")
        else:
            backend.insert(link,title,headline, instructor,rating,review)
    
    if not backend.search(title,instructor):
            backend.insert(link,title,headline, instructor,rating,review)
            print("inserted the following",title,instructor,headline)



Start()

# for row in backend.view():
#     print(row)
driver.quit() 
backend.view()






