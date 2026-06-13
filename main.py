import streamlit as st
import random

st.set_page_config(
    page_title="✨ PokéMBTI",
    page_icon="🌷",
    layout="centered"
)

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#fff6fb,
#f7f2ff,
#eef7ff
);
}

.card{
background:white;
padding:32px;
border-radius:28px;
box-shadow:0 10px 40px rgba(180,180,255,.2);
}

.title{
text-align:center;
font-size:48px;
font-weight:900;
}

.sub{
text-align:center;
color:#888;
}

</style>
""", unsafe_allow_html=True)

pokemon = {

"INTJ":["뮤츠","🧠 전략적이고 조용한 카리스마","https://img.pokemondb.net/artwork/large/mewtwo.jpg"],
"INTP":["나몰빼미","🌙 분석적이고 자기 세계가 뚜렷함","https://img.pokemondb.net/artwork/large/rowlet.jpg"],
"ENTJ":["리자몽","🔥 추진력 있고 리더십 있음","https://img.pokemondb.net/artwork/large/charizard.jpg"],
"ENTP":["팬텀","😏 아이디어 많고 자유로움","https://img.pokemondb.net/artwork/large/gengar.jpg"],

"INFJ":["루카리오","💙 깊고 따뜻한 성향","https://img.pokemondb.net/artwork/large/lucario.jpg"],
"INFP":["이브이","🌷 감성적이고 상상력 풍부","https://img.pokemondb.net/artwork/large/eevee.jpg"],
"ENFJ":["픽시","✨ 사람 챙기고 다정함","https://img.pokemondb.net/artwork/large/clefable.jpg"],
"ENFP":["피카츄","⚡ 밝고 에너지 넘침","https://img.pokemondb.net/artwork/large/pikachu.jpg"],

"ISTJ":["거북왕","🌊 책임감 강하고 안정적","https://img.pokemondb.net/artwork/large/blastoise.jpg"],
"ISFJ":["토게피","🥚 배려 깊고 다정함","https://img.pokemondb.net/artwork/large/togepi.jpg"],
"ESTJ":["보스로라","🛡️ 추진력 강함","https://img.pokemondb.net/artwork/large/aggron.jpg"],
"ESFJ":["푸린","🎀 분위기 메이커","https://img.pokemondb.net/artwork/large/jigglypuff.jpg"],

"ISTP":["개굴닌자","🌌 침착하고 실전형","https://img.pokemondb.net/artwork/large/greninja.jpg"],
"ISFP":["치코리타","🍃 감성적이고 부드러움","https://img.pokemondb.net/artwork/large/chikorita.jpg"],
"ESTP":["에이스번","🏃 활동적이고 자신감 있음","https://img.pokemondb.net/artwork/large/cinderace.jpg"],
"ESFP":["파치리스","🌈 귀엽고 활발함","https://img.pokemondb.net/artwork/large/pachirisu.jpg"]

}

st.markdown("""
<div class="card">

<div class="title">
🌷 PokéMBTI
</div>

<div class="sub">
MBTI로 나와 닮은 포켓몬 찾기 ✨
</div>

</div>
""", unsafe_allow_html=True)

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
        90,
        100
    )

    left,right = st.columns([1,1])

    with left:

        st.image(
            result[2],
            use_container_width=True
        )

    with right:

        st.markdown(
f"""
# 🎀 {result[0]}

### 🌸 성향
{result[1]}

### 💖 싱크로율
{score}%

✨ 포켓몬이 널 선택했어
"""
)

    st.progress(score)

    st.success("매칭 완료 🎈")

st.write("")
st.caption("made with 🌷 streamlit")
