import time
import streamlit as st

# 주제
st.title('Hello world!')
# 글
st.write(':red[streamlit] is :blue-background[best] :sunglasses:')

# 버튼
st.title('button example')
if st.button('click me'):
    st.write('button is clicked')

#checkbox
st.title('checkbox example')
st.write("동의하시면 아래 내용에 체크해 주세요")
agree = st.checkbox("동의합니다.")

if agree:
    st.write("이얏호!")

#input -> selectors
st.title('option example')
option = st.selectbox(
    "연락을 어떻게 받고 싶으신가요??",
    ("이메일", "유선 통화", "문자"))

st.write("선택한 방식:", option)
# slider
st.title('slider example')
age = st.slider("당신은 몇 살인가요?", 0, 130, 25)
st.write("저는 ", age, "살 입니다!")

# input area
st.title('input example')
text1 = st.text_input("이름을 입력하세요.")
text2 = st.text_area("자기소개 해주세요.")
st.write("이름 입력값: " + text1)
st.write("자기소개 입력값: " + text2)

#image
st.title('image example')
if st.button('랜덤 이미지'):
    random_url = f'https://picsum.photos/250/250?random={time.time()}'
    st.image(random_url)
# form
st.title('form example')

col1, col2 = st.columns(2) # 두 개의 컬럼 생성. 표현하고 싶은 내용을 열 데이터로 나눠 보여주고 싶을 떄 사용합니다.

with col1:
    text1 = st.text_input("form을 이용하지 않는 경우")
    text2 = st.text_area("form을 이용하지 않는 경우")
    st.write("1번 입력값: " + text1)
    st.write("2번 입력값: " + text2)


with col2:
    with st.form("form을 사용합니다"):
        text3 = st.text_input("form을 이용하는 경우")
        text4 = st.text_area("form을 이용하는 경우")
        submitted = st.form_submit_button("제출")

        if submitted:
            st.write("1번 입력값: " + text3)
            st.write("2번 입력값: " + text4)
        else:
            st.write("1번 입력값: ")
            st.write("2번 입력값: ")