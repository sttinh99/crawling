from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import json

# khai bao bien

browser = webdriver.Chrome(executable_path="chromedriver.exe")

# test open web

browser.get(
    "https://www.vietnamworks.com/it+nganh-it-phan-mem-tai-ho-chi-minh-i35v29-vn")
# Dien thong tin vao email va fb
browser.maximize_window()
browser.execute_script("window.scrollBy(0,1000)", "")
sleep(5)

blockDocument = browser.find_element_by_class_name(
    "block-job-list")
# box_email = browser.find_element_by_tag_name('tbody')
# print(blockjob.text)

list_documents = browser.find_elements_by_xpath(
    '/html/body/div[1]/div[7]/div[2]/main/div/div/div[1]/div[3]/div')
# print(list_documents)
listOfDocuments = []


# document = list_documents[0]
# x = document.find_element_by_class_name('decs_book')
# y = document.find_element_by_class_name('txt_gray')
# z = y.find_elements_by_class_name('txt_note')[1].text
# term = {
#     "documentTitle": document.find_element_by_class_name('colorlink').text,
#     "job_des": x.find_element_by_tag_name("p").text,
#     "job_cre": y.find_elements_by_class_name('txt_note')[1].text,
#     "date_create": y.find_elements_by_class_name('txt_note')[2].text
# }
# print(term)
condition = True
count = 0
while condition:

    count += 1
    sleep(5)
    jobs = browser.find_elements_by_class_name(
        'job-info-wrapper')
    print(len(jobs))
    # print(jobs, 'asdddddddd')
    # xxx = lastPage.find_element_by_tag_name('a').text
    for job in tqdm(jobs):
        term = {
            "job_title": job.find_element_by_class_name('job-title').text,
            "company_name": job.find_element_by_class_name("company-name").text,
            "location": job.find_element_by_class_name('location').text,
            "post_date": job.find_element_by_class_name('posted-date').text
        }
        listOfDocuments.append(term)
    if(count >= 3):
        condition = False
    browser.find_elements_by_class_name('page-link')[-2].click()
    
print(len(listOfDocuments))
with open('vietnamworks.json', 'w', encoding='utf-8') as f:
    json.dump(listOfDocuments, f, ensure_ascii=False, indent=4)
# for job in list_jobs:
#     job_title = job.find_element_by_class_name('job-title')
#     job.find_element_by_class_name('mt-1')
#     job.find_element_by_class_name('location')
# txtUser = browser.find_element_by_id("email")
# txtUser.send_keys("sttinh1103")

# txtPassword = browser.find_element_by_id("pass")
# txtPassword.send_keys("54264598464cC@")

# submit form

# txtPassword.send_keys(Keys.ENTER)

# Stop program 5s

sleep(5)

# Dong trinh duyen

# browser.close()
