import streamlit as st
import random

st.set_page_config(
page_title="PokéMBTI",
page_icon="🌷",
layout="centered"
)

pokemon = {
"INFP": (
"이브이",
"🌷 상상력이 풍부하고 감정이 깊은 타입",
"https://img.pokemondb.net/artwork/large/eevee.jpg"
),
"ENFP": (
"피카츄",
"⚡ 밝고 에너지 넘치는 타입",
"https://img.pokemondb.net/artwork/large/pikachu.jpg"
),
"INFJ": (
"루카리오",
"💙 깊게 생각하고 배려하는 타입",
"https://img.pokemondb.net/artwork/large/lucario.jpg"
),
"INTJ": (
"뮤츠",
"🧠 계획적이고 전략적인 타입",
"https://img.pokemondb.net/artwork/large/mewtwo.jpg"
)
}

st.title("🌷 PokéMBTI")
st.caption("MBTI로 나와 닮은 포켓몬 찾기")

mbti = st.selectbox(
"MBTI 선택",
["INFP", "ENFP", "INFJ", "INTJ"]
)

if st.button("결과 보기"):
name, desc, image = pokemon[mbti]

```
st.balloons()

st.image(
    image,
    width=300
)

st.subheader(name)

st.write(desc)

score = random.randint(90, 100)

st.progress(score)

st.success(
    str(score) + "% 일치!"
)
```
