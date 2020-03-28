import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}

url = "https://www.shixiseng.com/intern/inn_je3rovoyii0q?pcm=pc_SearchList&mxa=asdd.0eqlx1._.$2"
req = requests.get(url,headers=headers)
html = req.text
soup = BeautifulSoup(html,"lxml")
job = soup.title.text.split("招聘")[0]
company_name = soup.select('.com_intro .com-name')[0].text.strip()
salary_text = soup.select(".job_money.cutom_font")[0].text
print("工作职位的名称为：{}\n薪金为：{}\n招聘公司的名称为：{}\n".format(job,salary_text,company_name))
print("该页面的薪金对应为:\n\n200-400/天")
print(f"{salary_text}".encode("utf-8"))
