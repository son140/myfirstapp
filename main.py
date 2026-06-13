import streamlit as st

st.set_page_config(
page_title="PokéMBTI",
page_icon="🌷"
)

st.title("🌷 PokéMBTI")

mbti = st.selectbox(
"MBTI 선택",
["INFP", "ENFP", "INFJ", "INTJ"]
)

if st.button("결과 보기"):

```
data = {
    "INFP": "🎀 이브이",
    "ENFP": "⚡ 피카츄",
    "INFJ": "💙 루카리오",
    "INTJ": "🧠 뮤츠"
}

st.balloons()

st.success(
    data[mbti]
)
```
