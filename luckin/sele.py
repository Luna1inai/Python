from selenium import webdriver  # 导入selenium包
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import xlwt
book=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=book.add_sheet('瑞幸咖啡',cell_overwrite_ok=True)
sheet.write(0,0,'视频名称')
sheet.write(0,1,'视频地址')
sheet.write(0,2,'视频描述')
sheet.write(0,3,'视频分区')
sheet.write(0,4,'观看次数')
sheet.write(0,5,'弹幕数')
sheet.write(0,6,'发布时间')
sheet.write(0,7,'up主')
n=1
driver = webdriver.Firefox(r'C:\Program Files\Mozilla Firefox')
WAIT = WebDriverWait(driver, 10)
def web_search():
    print('开始访问b站....')
    driver.get("http://www.bilibili.com")
    input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-search-keyword")))
    submit = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.bilifont')))
    input.send_keys('瑞幸')
    submit.click()
    print('跳转到新窗口')
    all_h = driver.window_handles
    driver.switch_to.window(all_h[1])
    submit1=WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.imgleft')))
    submit1.click()
    get_source()
def get_source():
    #WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.video-list')))
    for i in range(1, 51):
        req = requests.get(
            f'https://search.bilibili.com/all?keyword=%E7%91%9E%E5%B9%B8&from_source=nav_search&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.9&order=totalrank&duration=0&tids_1=0&page={i}')
        html = req.text
        #html = driver.page_source
        soup = BeautifulSoup(html,'lxml')
        save_to_excel(soup)
def save_to_excel(soup):
    list = soup.find(class_='video-list clearfix').find_all(class_='info')
    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_des = item.find(class_='des hide').text
        item_type = item.find(class_='type hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biubiu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text
        item_upname=item.find(class_='up-name').text
        #print('爬取：' + item_title+item_upname)
        global n
        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_des)
        sheet.write(n, 3, item_type)
        sheet.write(n, 4, item_view)
        sheet.write(n, 5, item_biubiu)
        sheet.write(n, 6, item_date)
        sheet.write(n, 7, item_upname)
        n = n + 1
def main():
    web_search()
if __name__ == '__main__':
    main()
    book.save(u'瑞幸咖啡.xlsx')