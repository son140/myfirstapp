import streamlit as st
import random
import time

st.set_page_config(
    page_title="PokéMBTI",
    page_icon="🌷",
    layout="centered"
)

# -------------------------
# 데이터
# -------------------------

pokemon = {

"INTJ":("뮤츠","https://img.pokemondb.net/artwork/large/mewtwo.jpg",
"조용하지만 압도적인 전략가 🧠"),

"INTP":("후딘","https://img.pokemondb.net/artwork/large/alakazam.jpg",
"호기심과 분석력 최고 📚"),

"ENTJ":("리자몽","https://img.pokemondb.net/artwork/large/charizard.jpg",
"카리스마 넘치는 리더 🔥"),

"ENTP":("팬텀","https://img.pokemondb.net/artwork/large/gengar.jpg",
"아이디어와 장난기 폭발 😏"),

"INFJ":("루카리오","https://img.pokemondb.net/artwork/large/lucario.jpg",
"깊고 따뜻한 이상주의자 💙"),

"INFP":("이브이","https://img.pokemondb.net/artwork/large/eevee.jpg",
"몽글몽글 감성 타입 🌷"),

"ENFJ":("픽시","https://img.pokemondb.net/artwork/large/clefable.jpg",
"사람들을 빛나게 하는 타입 ✨"),

"ENFP":("피카츄","https://img.pokemondb.net/artwork/large/pikachu.jpg",
"귀엽고 자유로운 에너지 ⚡"),

"ISTJ":("거북왕","https://img.pokemondb.net/artwork/large/blastoise.jpg",
"안정감 최고 🌊"),

"ISFJ":("토게피","https://img.pokemondb.net/artwork/large/togepi.jpg",
"다정함 가득 🥚"),

"ESTJ":("보스로라","https://img.pokemondb.net/artwork/large/aggron.jpg",
"추진력 만렙 🛡️"),

"ESFJ":("푸린","https://img.pokemondb.net/artwork/large/jigglypuff.jpg",
"분위기 메이커 🎀"),

"ISTP":("개굴닌자","https://img.pokemondb.net/artwork/large/greninja.jpg",
"쿨한 행동파 🌙"),

"ISFP":("나몰빼미","https://img.pokemondb.net/artwork/large/rowlet.jpg",
"조용한 감성러 🍃"),

"ESTP":("에이스번","https://img.pokemondb.net/artwork/large/cinderace.jpg",
"모험 좋아하는 타입 🏃"),

"ESFP":("파치리스","https://img.pokemondb.net/artwork/large/pachirisu.jpg",
"존재감 넘치는 귀요미 🌈")
}

quotes = [
"포켓몬 세계에서 스카우트 제안 도착 💌",
"오늘의 운명 매칭 완료 ✨",
"이 조합 꽤 귀엽다…🌸",
"포켓몬이 널 먼저 골랐대 🫧"
]

# -------------------------
# 디자인
# -------------------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
180deg,
#fffdfd,
#fff7fb,
#f6f3ff
);
}

.hero{

padding:40px;

background:
rgba(255,255,255,.65);

border-radius:30px;

backdrop-filter:blur(20px);

text-align:center;

border:1px solid #ffffff;

box-shadow:
0 12px 40px rgba(255,190,220,.15);

}

.result{

padding:28px;

background:white;

border-radius:28px;

box-shadow:
0 10px 50px rgba(230,180,255,.18);

}

.title{

font-size:42px;

font-weight:900;

color:#555;

}

.caption{

color:#999;

}

img{

border-radius:20px;

}

</style>
""", unsafe_allow_html=True)

# -------------------------

st.markdown("""
<div class='hero'>

<div class='title'>
🌷 PokéMBTI
</div>

<div class='caption'>
MBTI로 찾는 나의 포켓몬
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

mbti = st.selectbox(
"🫧 MBTI 선택",
[""]+list(pokemon.keys())
)

if st.button("✨ 결과 보기", use_container_width=True):

    if mbti:

        progress = st.progress(0)

        for i in range(101):
            time.sleep(0.006)
            progress.progress(i)

        # 풍선 여러 번
        for _ in range(3):
            st.balloons()

        name, img, desc = pokemon[mbti]

        sync = random.randint(90,100)

        st.markdown("<div class='result'>",
        unsafe_allow_html=True)

        st.image(
            img,
            use_container_width=True
        )

        st.markdown(
        f"""
        <h1 align='center'>
        🎀 {name}
        </h1>

        <p align='center'>
        {random.choice(quotes)}
        </p>

        <hr>

        ### 🌸 성향
        {desc}

        ### 💖 싱크로율
        # {sync}%

        너랑 분위기가 꽤 잘 어울려 ✨
        """,
        unsafe_allow_html=True
        )

        st.markdown("</div>",
        unsafe_allow_html=True)

        st.success("매칭 완료 🎈")

st.write("")
st.caption("🫧 made with streamlit")
