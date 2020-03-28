import requests
from bs4 import BeautifulSoup
import xlwt
book=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=book.add_sheet('实习僧',cell_overwrite_ok=True)
sheet.write(0,0,'名称')
sheet.write(0,1,'公司')
sheet.write(0,2,'工资')
sheet.write(0,3,'关键词')
sheet.write(0,4,'城市')
n=1
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
def job_url():
    for i in range(1, 14):
        req = requests.get(
            f'https://www.shixiseng.com/interns?page={i}&keyword=python&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend=',
            headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        offers = soup.select('.intern-wrap.intern-item')
        for offer in offers:
            url = offer.select(" .f-l.intern-detail__job a")[0]['href']
            #detail_url(url)
            html = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html, 'lxml')
            title = soup.title.text
            job = title.split("招聘")[0]
            company_name = soup.select('.com_intro .com-name')[0].text.strip()
            #key_word=soup.select()
            key_word=soup.select(".com-detail div")[0].text.strip()
            city=soup.select(".job_position")[0].text.strip()
            salary = soup.select(".job_money.cutom_font")[0].text.encode("utf-8")
            salary = salary.replace(b'\xef\x9a\x8d', b"0")
            salary = salary.replace(b'\xee\x99\xb1', b"1")
            salary = salary.replace(b'\xef\x9c\x86', b"2")
            salary = salary.replace(b'\xef\x9b\x8d', b"3")
            salary = salary.replace(b'\xee\x8d\x8a', b"4")
            salary = salary.replace(b'\xee\xb6\xaa', b"5")
            salary = salary.replace(b'\xee\xb4\xac', b"6")
            salary = salary.replace(b'\xee\x94\x9d', b"7")
            salary = salary.replace(b'\xef\x9c\xb0', b"8")
            salary = salary.replace(b'\xef\x86\xbf', b"9")
            salary = salary.decode()
            #print("工作职位的名称为：{}\n薪金为：{}\n招聘公司的名称为：{}\n".format(job, salary, company_name))
            print("爬取")
            global n
            sheet.write(n, 0, job)
            sheet.write(n, 1, company_name)
            sheet.write(n, 2, salary)
            sheet.write(n, 3, key_word)
            sheet.write(n, 4, city)
            n = n + 1
def main():
    job_url()
if __name__ == '__main__':
    main()
    book.save(u'实习僧3.xlsx')