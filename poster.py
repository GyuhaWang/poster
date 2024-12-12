import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
#--------------------------functions --------------------------
def getAnswerFromGpt(input_text):
    chat_completion = client.chat.completions.create(
            messages=[
                    {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
                },
                {
                    "role": "user",
                    "content": input_text,
                }
                
            ],
            model="gpt-4",
        )

    return chat_completion.choices[0].message.content

def getImageFromGpt(input_text):
    image_completion = client.images.generate(
    model="dall-e-3",
    prompt=input_text,
    size="1024x1024",
    n=1,
    )

    image_url = image_completion.data[0].url
    return image_url
#-------------------------- view -------------------------------
st.title('🎁 제품 홍보 포스터 생성기')
keyword = st.text_input("키워드를 입력하세요.")

if st.button('생성하기🔥'):
    with st.spinner('생성 중입니다.'):

        result = getAnswerFromGpt(keyword)
        img_url = getImageFromGpt(result)
        st.write(result)
        st.image(img_url)