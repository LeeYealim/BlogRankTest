# (성공) 블로그 제목 가져오기 

from bs4 import BeautifulSoup
import urllib.request as req
import datetime

# 블로그 url
# main_url='https://blog.naver.com/anus35/223181049124'           # 대상 블로그 url 입력
main_url='https://blog.naver.com/anus35/223186827044'
blog_url = 'https://blog.naver.com/'


res= req.urlopen(main_url)
soup= BeautifulSoup(res, 'html.parser')

# iframe src 가져오기
i_src = soup.find_all('iframe')[0]['src']

i_url = blog_url + i_src
print('iframe url :', i_url)

# 블로그 ifrma 내용 요청
res= req.urlopen(i_url)
soup= BeautifulSoup(res, 'html.parser')

# 게시글 제목
if soup.find("div", attrs={"class":"se-title-text"}):
    text = soup.find("div", attrs={"class":"se-title-text"}).get_text()
    print(text)

# 게시글 작성 날짜
if soup.find("span", attrs={"class":"se_publishDate"}):
    text = soup.find("span", attrs={"class":"se_publishDate"}).get_text()
    if '전' in text:
        print('포함')
        print(datetime.datetime.today().strftime("%Y-%m-%d"))
    else:
        dlist = text.split('. ')
        puble_date = datetime.date(year=int(dlist[0]), month=int(dlist[1]), day=int(dlist[2]))
        print(puble_date)

# 내용
if soup.find("div", attrs={"class":"se-main-container"}):
    text = soup.find("div", attrs={"class":"se-main-container"}).get_text()
    text = text.replace("\n","")    # 공백 제거
    print(text)
