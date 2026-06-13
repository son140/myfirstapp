import streamlit as st
import random

st.set_page_config(
page_title="PokéMBTI",
page_icon="🌷",
layout="centered"
)

data = {
"INFP": {
"name": "이브이",
"desc": "🌷 상상력이 풍부하고 감정이 깊은 타입",
"image": "https://img.pokemondb.net/artwork/large/eevee.jpg"
},
"ENFP": {
"name": "피카츄",
"desc": "⚡ 밝고 에너지 넘치는 타입",
"image": "https://img.pokemondb.net/artwork/large/pikachu.jpg"
},
"INFJ": {
"name": "루카리오",
"desc": "💙 조용하지만 깊은 생각을 하는 타입",
"image": "https://img.pokemondb.net/artwork/large/lucario.jpg"
},
"INTJ": {
"name": "뮤츠",
"desc": "🧠 계획적이고 목표 지향적인 타입",
"image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg"
}
}

st.title("🌷 PokéMBTI")
st.caption("MBTI로 어울리는 포켓몬 찾기")

choice = st.selectbox(
"🫧 MBTI 선택",
list(data.keys())
)

if st.button("💖 결과 보기"):

```
result = data[choice]

st.balloons()

st.image(
    result["image"],
    width=300
)

st.subheader("🎀 " + result["name"])

st.write("### 🌸 성향")
st.write(result["desc"])

score = random.randint(90, 100)

st.write("### 💖 싱크로율")
st.progress(score)

st.success(f"{score}% 일치!")
```
