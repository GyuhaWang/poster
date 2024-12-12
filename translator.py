import streamlit as st
from translate import Translator
import os
import sys
import urllib.request
import json


os.environ["CLIENT_ID"] = st.secrets["CLIENT_ID"]
os.environ["CLIENT_SECRET"] = st.secrets["CLIENT_SECRET"]
def getNaveSearchResult(searchKeyword):
    encText = urllib.parse.quote(searchKeyword)
    url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText # JSON 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",os.environ.get("CLIENT_ID"),)
    request.add_header("X-Naver-Client-Secret",os.environ.get("CLIENT_SECRET"),)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsonResponse = json.loads(response_body.decode('utf-8'))
        return jsonResponse 
    else:
        print("Error Code:" + rescode)
        return "Error Code:" + rescode

st.title('한국어-영어 번역 프로그램')
kor = st.text_input("한국어 문장을 입력하세요.")
option = st.selectbox(
    "번역할 언어 코드를 선택해주세요",
    ("en", "es", "zh"))
if st.button('번역'):
    translator = Translator(to_lang=option, from_lang="ko")   
    result = translator.translate(kor)  # 한국어를 영어로 번역
    st.write('번역 결과::',result)

st.title('네이버 검색창')
searchText = st.text_input("검색어를 입력하세요")
if st.button('검색'):
    result = getNaveSearchResult(searchText)
    st.title('검색 결과')
   
    for item in result['items']:
        st.write(item)
