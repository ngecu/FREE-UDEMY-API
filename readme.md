![COVER IMAGE](/cover.png)

# Part 1: Set-up packages for web scraping

## Virtual Environment Setup
start by creating a virtual environment
```
py -m venv env

```
We then activate it
```
env\Scripts\activate
```
After installation next is the web driver manager.
Library provides the way to automatically manage drivers for different browsers

```
pip install webdriver-manager
```

```
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
```

# Part 2: Find CSS tags to input into python code

## NUMBER OF PAGES  TO SCRAPE



```

"filter-panel--item-count--2JGx3"

def Start():
    # selenium options


    driver.get("https://www.udemy.com/courses/free/")
    time.sleep(10)

    results = driver.find_element_by_class_name('filter-panel--item-count--2JGx3').text
    course_count = results.split()[0]

    number_of_pages = math.ceil((int(course_count)/16))
    print(number_of_pages)
```