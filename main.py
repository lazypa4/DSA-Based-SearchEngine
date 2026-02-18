import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.codechef.com/practice/dynamic-programming")
time.sleep(5)

html= driver.page_source
soup= BeautifulSoup(html, 'html.parser')
all_ques_div= soup.find_all("div", {"class": "_practiceProblemRow_1edov_4053"})

all_ques=[]

for i in all_ques_div:
    all_ques.append(i.findAll("div")[0].find("a"))

urls=[]
titles=[]

for i in all_ques:
    urls.append(i["href"])
    titles.append(i.text)

with open("codechef_urls.txt","w+") as f:
    f.write('\n'.join(urls))

with open("codechef_titles.txt","w+") as f:
    f.write('\n'.join(titles))



all_ques_div_diff= soup.find_all("div", {"class": "_practiceDifficultyBadge_1edov_4170"})
diff =[]
for i in all_ques_div_diff:
    diff.append(i.find("span").text)

# with open("codechef_difficulty.txt","w+") as f:
#     f.write('\n'.join(diff))

