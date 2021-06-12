from selenium import webdriver #cong cu su dung
from time import sleep
from selenium.webdriver.common.keys import Keys  #cong cu su dung
from tqdm import tqdm
import json  #cong cu su dung

# khai bao bien

browser = webdriver.Chrome(executable_path="chromedriver.exe") #cong cu su dung
# test open web

#Domain chính của trang mà nhóm crawl dữ liệu
browser.get(
    "http://thuvienso.hcmute.edu.vn/cong-nghe-thong-tin/tat-ca-tai-lieu-cong-nghe-thong-tin-478-0.html")
browser.maximize_window()
browser.execute_script("window.scrollBy(0,1000)", "")
sleep(5)

#Phần chứa dữ liệu để crawl
blockDocument = browser.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]')
#List dữ liệu để crawl
# list_documents = browser.find_elements_by_xpath(
#     '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li')
# print(len(list_documents))
listOfDocuments = []
condition = True
count = 0
while condition:

    # count += 1
    # if(count == 1183):
    #     continue
    #List dữ liệu để crawl trong 1 page
    list_documents = browser.find_elements_by_xpath(
        '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li')
    #lấy phần tử cuối.
    checkPage = browser.find_elements_by_xpath(
        '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/ul/li')[-1]
    #lấy phần tử nextPage.
    lastPage = browser.find_elements_by_xpath(
        '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/ul/li')[-2]
    # xxx = lastPage.find_element_by_tag_name('a').text
    for document in tqdm(list_documents):
        x = document.find_element_by_class_name('decs_book')
        y = document.find_element_by_class_name('txt_gray')
        # z = y.find_elements_by_class_name('txt_note')[1].text
        term = {
            "documentTitle": document.find_element_by_class_name('colorlink').text,
            "documentDes": x.find_element_by_tag_name("p").text,
            "documentSource": y.find_elements_by_class_name('txt_note')[1].text,
            "dateCreate": y.find_elements_by_class_name('txt_note')[2].text,
            "review": y.find_elements_by_class_name('txt_note')[3].text,
            "downloaded": y.find_elements_by_class_name('txt_note')[4].text
        }
        listOfDocuments.append(term)
    try:
        if(count >= 3000):
            condition = False
        # if(lastPage == checkPage):
        #     condition = False
        checkPage.find_element_by_class_name('bor_none').click()
    except:
        condition = False
print(len(listOfDocuments))
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(listOfDocuments, f, ensure_ascii=False, indent=4)

sleep(5)
