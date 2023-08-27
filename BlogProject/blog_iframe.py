# 블로그 iframe 크롤링
# 링크 : https://whiteseabubble.tistory.com/49

from bs4 import BeautifulSoup
import requests
import urllib.request as req

#iframeurl="/PostView.naver?blogId=anus35&logNo=223181049124&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fquery%3D%25ED%2595%259C%25EC%259D%2598%25EC%259B%2590%26nso%3D%26where%3Dblog%26sm%3Dtab_opt&directAccess=false"
iframeurl="/PostView.naver?blogId=anus35&logNo=223181049124&redirect=Dlog&widgetTypeCall=true&directAccess=false"
url="https://blog.naver.com/"+iframeurl
res= req.urlopen(url)
soup= BeautifulSoup(res,'html.parser')


# 게시글 제목
if soup.find("div", attrs={"class":"se-title-text"}):
    text = soup.find("div", attrs={"class":"se-title-text"}).get_text()
    text = text.replace("\n","") #공백 제거
    print(text)

print()

# 내용
if soup.find("div", attrs={"class":"se-main-container"}):
    text = soup.find("div", attrs={"class":"se-main-container"}).get_text()
    text = text.replace("\n","") #공백 제거
    print(text)