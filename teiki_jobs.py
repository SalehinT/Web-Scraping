import time
import scrap
from chrome_driver import driver
from selenium.webdriver.common.by import By

def initializing():
    url = 'https://arbeit.doctor-navi.jp/re'
    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="new_q"]/table/tbody/tr[4]/td[2]/a').click()
    area = driver.find_elements(By.CLASS_NAME, 're_area_chk')

    for i in area:
        i.click()

    driver.find_element(By.XPATH, '//*[@id="re_area_modal"]/div/div[12]/a[2]').click()

    # time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="new_q"]/div[2]').click()



def teiki():

    links = []
    page_no = 1
    initializing()

    while True:
        print(page_no)
        time.sleep(5)
        elements = driver.find_element(By.CLASS_NAME, 'main-module-search-index')
        element = elements.find_elements(By.TAG_NAME, 'a')
        time.sleep(5)
        single_job_link_set = set()

        for ele in element:

            single_job_link = ele.get_attribute('href')
            links.append(single_job_link)

            if 'bookmarks' not in single_job_link and single_job_link not in single_job_link_set:
                scrap.scraping(single_job_link)
        
            single_job_link_set.add(single_job_link)

        page_no += 1
        try: 
            temp = driver.find_element(By.CLASS_NAME, 'utility-module-paginate')
            next_page = temp.find_element(By.CLASS_NAME, 'next').click()
        except:
            print('Last Page')
            break

    driver.close()

# teiki()
