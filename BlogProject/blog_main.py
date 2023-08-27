# (성공) 블로그 제목 가져오기 
# test.py 파일에서 수정

from bs4 import BeautifulSoup
import requests
import urllib.request as req
import datetime
import json

# 블로그 url
# main_url='https://blog.naver.com/anus35/223181049124'           # 대상 블로그 url 입력
main_url='https://blog.naver.com/anus35/223186827044'

def test():
    return "test"

# 블로그 url 전달받아 title과 date 반환하는 함수
# 잘못된 url 전송 시, "0" 반환
# 정상 작동 시, title과 date JSON 객체 반환
# def get_blog_title_n_date(url):
def get_blog_info(url):
    try:
        res = req.urlopen(url)
        soup = BeautifulSoup(res, 'html.parser')
    except:
        return "0"

    blog_url = 'https://blog.naver.com/'

    # iframe src 가져오기
    i_src = soup.find_all('iframe')[0]['src']
    i_url = blog_url + i_src
    #print('iframe url :', i_url)
    
    # 블로그 ifrma 내용 요청
    res= req.urlopen(i_url)
    soup= BeautifulSoup(res, 'html.parser')
    
    # 게시글 제목
    blog_title = soup.find("div", attrs={"class":"se-title-text"}).get_text().replace('\n','')
    
    # 게시글 작성일
    text = soup.find("span", attrs={"class":"se_publishDate"}).get_text()
    if '전' in text:
        blog_date = datetime.datetime.today().strftime("%Y-%m-%d")
    else:
        dlist = text.split('. ')
        blog_date = datetime.date(year=int(dlist[0]), month=int(dlist[1]), day=int(dlist[2])).strftime("%Y-%m-%d")

    result = {"title":blog_title, "date":blog_date}
    # result = str(result)

    return result


# 블로그 노출순위
def get_blog_rank(keyword, url):
    base_url = "https://search.naver.com/search.naver?nso=&where=blog&sm=tab_opt&query="  # blog URL
    search_url = base_url + keyword

    r = requests.get(search_url)
    soup = BeautifulSoup(r.text, "html.parser")

    # 이 클래스를 가진 것을 전부 가져옴
    items = soup.select(".total_wrap.api_ani_send")

    is_exist = 0
    rank_num = 0  # 노출순위
    g_num = 0  # 광고 개수
    for i, item in enumerate(items, 1):
        ad = item.select_one(".link_ad")
        if ad:
            g_num += 1  # 광고 + 1
            continue

        rank_num += 1  # 랭크 + 1

        # 블로그 제목
        # blog_title = item.select_one(".sub_txt.sub_name").text
        # print(f"{blog_title}")

        # 게시글 제목
        post_title = item.select_one(".api_txt_lines.total_tit")
        #print(f"{post_title.text}")

        # 게시글 URL
        blog_url = post_title.get('href')
        #print(rank_num, ":", blog_url)

        # 게시글 URL과 타겟 URL이 같은 경우(순위 확인 가능)
        if blog_url == url:
            is_exist = 1
            break

    if is_exist :
        return str(rank_num)
    else :
        return '30+'


def get_blog_rank_n_info(keyword, url):
    rank = get_blog_rank(keyword, url)
    dict = get_blog_info(url)
    dict['rank'] = rank

    return str(dict)


# print(get_blog_rank_n_info('한의원', 'https://blog.naver.com/jc1103/223189397649'))