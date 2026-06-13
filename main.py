import streamlit as st
import random

st.set_page_config(
    page_title="PokéMBTI",
    page_icon="🌷",
    layout="centered"
)

pokemon = {
    "INFP": {
        "name": "이브이",
        "image": "https://img.pokemondb.net/artwork/large/eevee.jpg",
        "desc": "🌷 상상력이 풍부하고 감정이 깊은 타입"
    },
    "ENFP": {
        "name": "피카츄",
        "image": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
        "desc": "⚡ 밝고 에너지 넘치는 타입"
    },
    "INFJ": {
        "name": "루카리오",
        "image": "https://img.pokemondb.net/artwork/large/lucario.jpg",
        "desc": "💙 조용하지만 깊은 타입"
    },
    "INTJ": {
        "name": "뮤츠",
        "image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg",
        "desc": "🧠 계획적이고 전략적인 타입"
    }
}

st.title("🌷 PokéMBTI")
st.caption("MBTI로 나와 닮은 포켓몬 찾기")

mbti = st.selectbox(
    "MBTI 선택",
    list(pokemon.keys())
)

if st.button("결과 보기"):
    result = pokemon[mbti]

    st.balloons()

    st.image(
        result["image"],
        width=300
    )

    st.subheader(result["name"])

    st.write("### 성향")
    st.write(result["desc"])

    score = random.randint(90, 100)

    st.write("### 싱크로율")
    st.progress(score)

    st.success(f"{score}% 일치!")
