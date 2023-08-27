# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import pandas as pd

client_id = "6lXOqIvTziAhwgS39m3G"
client_secret = "6lXOqIvTziAhwgS39m3G"


query = urllib.parse.quote(input("검색 질의 : "))
idx = 0
display = 100
start = 1
end = 1000

web_df = pd.DataFrame(columns=("Title", "Link", "Description"))

for start_index in range(start, end, display):
    url = "https://openapi.naver.com/v1/search/webkr?query=" + query \
        + "&display=" + str(display) \
        + "&start=" + str(start_index)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)