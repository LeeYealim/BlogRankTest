# 링크 : https://yenpa.tistory.com/4

import os
import sys
import urllib.request
import json
import pandas as pd

def getresult(client_id,client_secret,query,display=10,start=1,sort='sim'):
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + \
    "&display=" + str(display) + "&start=" + str(start) + "&sort=" + sort

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_json = json.loads(response_body)
    else:
        print("Error Code:" + rescode)

    return pd.DataFrame(response_json['items'])


# 아래의 4개의 항목은 설정이 필요
client_id = "6lXOqIvTziAhwgS39m3G"
client_secret = "A0HN5YYqv5"
query = '한의원'
mybloggername = '건강한 하루'

display = 100
start = 1
sort = 'sim'

result_all = pd.DataFrame()
for i in range(0, 2):
    start = 1 + 100 * i
    result = getresult(client_id, client_secret, query, display, start, sort)

    result_all = pd.concat([result_all, result])
rank = 10000
result_all = result_all.reset_index()  # index가 100단위로 중복되는것을 초기화
result_all = result_all.drop('index', axis=1)  # reset_index후 생기는 이전 index의 column을 삭제
for index, result in result_all.iterrows():
    bloggername = result['bloggername']
    if mybloggername == bloggername:
        rank = index + 1  # index가 0부터 시작하므로 실제 순위는 +1이 되어야 함.
        break  # 내 블로그 이름이 매칭이 되어 이후는 break로 for문을 빠져나옴

print('나의 검색어 ' + query + '에 대한 블로그 검색 순위는 ' + str(rank) + '입니다.')