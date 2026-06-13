import streamlit as st
import random

st.set_page_config(
page_title="PokéMBTI",
page_icon="🌷",
layout="centered"
)

pokemon_data = {
"INTJ": {
"pokemon": "뮤츠",
"image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg",
"desc": "🧠 계획적이고 목표 지향적인 성향이에요."
},

```
"INFP": {
    "pokemon": "이브이",
    "image": "https://img.pokemondb.net/artwork/large/eevee.jpg",
    "desc": "🌷 상상력이 풍부하고 감정이 깊은 성향이에요."
},

"ENFP": {
    "pokemon": "피카츄",
    "image": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
    "desc": "⚡ 밝고 에너지 넘치는 분위기예요."
},

"INFJ": {
    "pokemon": "루카리오",
    "image": "https://img.pokemondb.net/artwork/large/lucario.jpg",
    "desc": "💙 조용하지만 사람을 깊게 이해하는 성향이에요."
}
```

}

st.title("🌷 PokéMBTI")
st.caption("MBTI로 어울리는 포켓몬 찾기")

mbti = st.selectbox(
"🫧 MBTI 선택",
["INTJ", "INFP", "ENFP", "INFJ"]
)

if st.button("💖 결과 보기"):

```
result = pokemon_data[mbti]

st.balloons()

st.image(
    result["image"],
    width=280
)

st.subheader(
    "🎀 " + result["pokemon"]
)

st.write("### 🌸 MBTI 성향")
st.write(
    result["desc"]
)

score = random.randint(90, 100)

st.write("### 💖 싱크로율")

st.progress(score)

st.success(
    str(score) + "% 일치!"
)
```

st.write("")
