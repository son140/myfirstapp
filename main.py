import streamlit as st
import random

st.set_page_config(
page_title="PokéMBTI",
page_icon="🌷",
layout="centered"
)

pokemon_data = {
"INFP": {
"name": "이브이",
"image": "https://img.pokemondb.net/artwork/large/eevee.jpg",
"mbti": "🌷 상상력이 풍부하고 감정이 깊은 편이에요.",
"match": "따뜻하고 다양한 가능성을 가진 이브이와 잘 어울려요."
},

```
"ENFP": {
    "name": "피카츄",
    "image": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
    "mbti": "⚡ 밝고 사람들에게 에너지를 주는 타입이에요.",
    "match": "피카츄처럼 존재만으로 분위기를 밝게 만들어요."
},

"INFJ": {
    "name": "루카리오",
    "image": "https://img.pokemondb.net/artwork/large/lucario.jpg",
    "mbti": "💙 조용하지만 깊게 생각하는 타입이에요.",
    "match": "루카리오처럼 차분하고 신뢰감 있어요."
},

"INTJ": {
    "name": "뮤츠",
    "image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg",
    "mbti": "🧠 계획적이고 목표 지향적인 타입이에요.",
    "match": "뮤츠처럼 조용하지만 강한 존재감이 있어요."
}
```

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
"mbti": "✨ 자신만의 분위기를 가진 타입이에요.",
"match": "편안하고 자연스러운 매력이 있어요."
}

for mbti in mbti_list:
if mbti not in pokemon_data:
pokemon_data[mbti] = default

st.markdown(
"""

<style>
.stApp{
background: linear-gradient(
180deg,
#fffdfd,
#fff7fb,
#f6f4ff
);
}
</style>

""",
unsafe_allow_html=True
)

st.title("🌷 PokéMBTI")
st.caption("MBTI로 나와 닮은 포켓몬 찾기")

selected = st.selectbox(
"🫧 MBTI 선택",
mbti_list
)

if st.button("💖 결과 보기"):

```
st.balloons()

result = pokemon_data[selected]

score = random.randint(90, 100)

st.image(
    result["image"],
    width=320
)

st.subheader("🎀 " + result["name"])

st.markdown("### 🌸 MBTI 성향")
st.write(result["mbti"])

st.markdown("### ✨ 왜 어울릴까?")
st.write(result["match"])

st.markdown("### 💖 싱크로율")
st.progress(score)

st.success(f"{score}% 일치!")
```
