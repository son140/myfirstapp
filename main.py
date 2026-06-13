import streamlit as st
import random

# 페이지 설정

st.set_page_config(
page_title="PokéMBTI",
page_icon="🌷",
layout="centered"
)

# 데이터

pokemon = {
"INFP": {
"name": "이브이",
"image": "https://img.pokemondb.net/artwork/large/eevee.jpg",
"desc": "🌷 상상력이 풍부하고 감정이 깊은 타입이에요.",
"match": "따뜻하고 다양한 가능성을 가진 이브이와 잘 어울려요."
},
"ENFP": {
"name": "피카츄",
"image": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
"desc": "⚡ 밝고 자유롭고 에너지가 넘치는 타입이에요.",
"match": "주변 분위기를 환하게 만드는 매력이 있어요."
},
"INFJ": {
"name": "루카리오",
"image": "https://img.pokemondb.net/artwork/large/lucario.jpg",
"desc": "💙 조용하지만 사람을 깊게 이해하는 타입이에요.",
"match": "차분하고 신뢰감 있는 루카리오와 잘 어울려요."
},
"INTJ": {
"name": "뮤츠",
"image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg",
"desc": "🧠 계획적이고 목표 지향적인 타입이에요.",
"match": "조용하지만 강한 존재감을 가진 분위기예요."
}
}

mbti_list = [
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]

default = {
"name": "나몰빼미",
"image": "https://img.pokemondb.net/artwork/large/rowlet.jpg",
"desc": "✨ 자신만의 분위기를 가진 타입이에요.",
"match": "편안하고 자연스러운 매력이 있어요."
}

for mbti in mbti_list:
if mbti not in pokemon:
pokemon[mbti] = default

# 화면

st.title("🌷 PokéMBTI")
st.caption("MBTI로 나와 어울리는 포켓몬 찾기")

selected = st.selectbox(
"🫧 MBTI 선택",
mbti_list
)

if st.button("💖 결과 보기"):

```
result = pokemon[selected]

st.balloons()

st.image(
    result["image"],
    width=300
)

st.subheader("🎀 " + result["name"])

st.markdown("### 🌸 MBTI 성향")
st.write(result["desc"])

st.markdown("### ✨ 왜 어울릴까?")
st.write(result["match"])

score = random.randint(90, 100)

st.markdown("### 💖 싱크로율")
st.progress(score)

st.success(str(score) + "% 일치!")
```
