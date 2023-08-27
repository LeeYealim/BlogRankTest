# 블로그 제목 가져오기
import requests
from bs4 import BeautifulSoup


url = 'https://blog.naver.com/anus35/223181049124'
url = 'https://blog.naver.com/anus35/223181049124/PostView.naver?blogId=anus35&logNo=223181049124&redirect=Dlog&widgetTypeCall=true&directAccess=false'

response = requests.get(url)

if response.status_code == 200: # 정상 연결시
    soup = BeautifulSoup(response.text, 'html.parser') # 수프 text 형태로 만들기
    print(soup)
    print()
    
    # iframe src 가져오기
    print(soup.find_all('iframe'))
    print(soup.find_all('iframe')[0]['src'])


