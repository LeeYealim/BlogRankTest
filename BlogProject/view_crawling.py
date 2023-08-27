# 뷰 크롤링
# https://www.youtube.com/watch?v=XVaC4prLsrY&list=RDCMUCdNSo3yB5-FRTFGbUNKNnwQ&start_radio=1&rv=XVaC4prLsrY&t=18



from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?nso=&where=blog&sm=tab_opt&query="    # blog URL
# base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="       # view URL

# 전달받은 블로그 url
target_url = 'https://blog.naver.com/bburihan/223185074420' # 양천구 3위

keyword = input("검색할 키워드를 입력하세요 : ")

search_url = base_url + keyword

r = requests.get(search_url)
soup = BeautifulSoup(r.text, "html.parser")

# 이 클래스를 가진 것을 전부 가져옴
items = soup.select(".total_wrap.api_ani_send")

rank_num = 0    # 노출순위
g_num = 0       # 광고 개수

for i, item in enumerate(items, 1):
    ad = item.select_one(".link_ad")
    if ad:
        g_num += 1  # 광고 + 1
        continue

    rank_num += 1   # 랭크 + 1

    # 블로그 제목
    # blog_title = item.select_one(".sub_txt.sub_name").text
    # print(f"{blog_title}")

    # 게시글 제목
    post_title = item.select_one(".api_txt_lines.total_tit")
    print(f"{post_title.text}")

    # 게시글 URL
    blog_url = post_title.get('href')
    print(rank_num, ":", blog_url)
    
    # 게시글 URL과 타겟 URL이 같은 경우(순위 확인 가능)
    if blog_url == target_url:
        break

    # print("광고 ", gg)
    # print()












# from bs4 import BeautifulSoup
# import requests
#
# base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
# # base_url = "https://search.naver.com/search.naver?nso=&where=blog&sm=tab_opt&query="
#
# keyword = input("검색할 키워드를 입력하세요 : ")
#
# search_url = base_url + keyword
#
# r = requests.get(search_url)
#
# soup = BeautifulSoup(r.text, "html.parser")
#
# # 이 클래스를 가진 것을 전부 가져옴
# items = soup.select(".total_wrap.api_ani_send")
#
#
# gg = 0
#
# for rank_num, item in enumerate(items, 1):
#     # print(f"{rank_num} : {item.text}")
#
#     print(f"<<{rank_num}>>")
#     ad = item.select_one(".link_ad")
#     if ad:
#         gg += 1
#         print("광고입니다.")
#         continue
#
#     blog_title = item.select_one(".sub_txt.sub_name").text
#     print(f"{blog_title}")
#
#     post_title = item.select_one(".api_txt_lines.total_tit._cross_trigger")
#     print(f"{post_title.text}")
#
#     print(f"{post_title.get('href')}")
#     print(f"{post_title['href']}")
#
#     print("광고 ", gg)
#     print()
