import streamlit as st
import random

st.set_page_config(
    page_title="✨ PokéMBTI",
    page_icon="🌷",
    layout="centered"
)

# -------------------
# 디자인
# -------------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#fff6fb,
#f7f2ff,
#eef5ff
);
}

.main-card{
background:white;
padding:35px;
border-radius:30px;
box-shadow:0 10px 40px rgba(190,180,255,.25);
}

.title{
text-align:center;
font-size:52px;
font-weight:900;
background:linear-gradient(
90deg,
#ff9fd6,
#9a8cff
);

-webkit-background-clip:text;
color:transparent;
}

.subtitle{
text-align:center;
color:#888;
}

.result{
background:#ffffffcc;
padding:25px;
border-radius:24px;
}

</style>
""",
unsafe_allow_html=True
)

# -------------------
# 데이터
# -------------------

pokemon = {

"INFP":{
"name":"이브이",
"img":"https://img.pokemondb.net/artwork/large/eevee.jpg",
"text":"🌷 상상력이 풍부하고 감정이 깊어요."
},

"ENFP":{
"name":"피카츄",
"img":"https://img.pokemondb.net/artwork/large/pikachu.jpg",
"text":"⚡ 에너지 넘치고 사람을 행복하게 만들어요."
},

"INFJ":{
"name":"루카리오",
"img":"https://img.pokemondb.net/artwork/large/lucario.jpg",
"text":"💙 차분하고 깊은 생각을 하는 편이에요."
},

"INTJ":{
"name":"뮤츠",
"img":"https://img.pokemondb.net/artwork/large/mewtwo.jpg",
"text":"🧠 전략적이고 조용한 카리스마가 있어요."
}

}

# -------------------

st.markdown("""
<div class="main-card">

<div class="title">
🌷 PokéMBTI
</div>

<div class="subtitle">
MBTI로 나와 닮은 포켓몬 찾기 ✨
</div>

</div>
""",
unsafe_allow_html=True)

st.write("")

mbti = st.selectbox(
"🫧 MBTI 선택",
list(pokemon.keys())
)

if st.button(
"💖 결과 보기",
use_container_width=True
):

    st.balloons()

    result = pokemon[mbti]

    score = random.randint(
        91,
        100
    )

    st.markdown(
        "<div class='result'>",
        unsafe_allow_html=True
    )

    c1,c2 = st.columns([1,1])

    with c1:

        st.image(
            result["img"],
            use_container_width=True
        )

    with c2:

        st.markdown(
f"""
# 🎀 {result["name"]}

### 🌸 성향
{result["text"]}

### 💖 싱크로율
{score}%

✨ 포켓몬이 널 선택했어
"""
)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.progress(score)

    st.success("매칭 완료 🎈")

st.write("")
st.caption("made with 🌷")
