import streamlit as st
import random
import time

st.set_page_config(
    page_title="PokéMBTI ✨",
    page_icon="🫧",
    layout="centered"
)

# ---------- 데이터 ----------

data = {
    "INTJ": ["뮤츠","전략적이고 깊게 생각하는 타입 🧠"],
    "INTP": ["후딘","호기심 폭발! 분석 천재 타입 📚"],
    "ENTJ": ["리자몽","카리스마 넘치는 리더 🔥"],
    "ENTP": ["팬텀","장난기와 아이디어의 화신 😏"],

    "INFJ": ["루카리오","조용하지만 따뜻한 이상주의자 💙"],
    "INFP": ["이브이","감성 가득 몽글몽글 🌷"],
    "ENFJ": ["픽시","사람들을 빛나게 하는 타입 ✨"],
    "ENFP": ["피카츄","밝고 자유로운 에너지 ⚡"],

    "ISTJ": ["거북왕","믿음직하고 차분한 타입 🌊"],
    "ISFJ": ["토게피","다정함 MAX 🥚"],
    "ESTJ": ["보스로라","추진력 장인 🛡️"],
    "ESFJ": ["푸린","사람 좋아하는 분위기 요정 🎀"],

    "ISTP": ["개굴닌자","쿨하고 실전형 🌙"],
    "ISFP": ["나몰빼미","조용하지만 감각적 🍃"],
    "ESTP": ["에이스번","도전 좋아하는 행동파 🏃"],
    "ESFP": ["파치리스","귀엽고 존재감 강함 🌈"]
}

quotes = [
    "포켓몬 세계에서 입단 제안 도착 📩",
    "이 조합… 생각보다 꽤 찰떡인데? 💌",
    "오늘의 운명 매칭 완료 ✨",
    "포켓몬이 먼저 널 골랐대 🌸"
]

# ---------- 디자인 ----------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#ffe6f5,
#f2ebff,
#e5f7ff
);
}

.hero{
padding:40px;
border-radius:32px;

backdrop-filter:blur(18px);

background:
rgba(255,255,255,0.35);

border:
1px solid rgba(255,255,255,0.5);

text-align:center;

box-shadow:
0 10px 40px rgba(0,0,0,.08);
}

.result{

padding:28px;

border-radius:28px;

background:white;

box-shadow:
0 10px 35px rgba(255,180,220,.25);

animation:up .5s ease;
}

@keyframes up{
from{
opacity:0;
transform:translateY(30px);
}

to{
opacity:1;
transform:none;
}
}

.title{
font-size:46px;
font-weight:900;
}

.sub{
opacity:.7;
}

.poke{
font-size:52px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------- 화면 ----------

st.markdown("""
<div class='hero'>

<div class='title'>
🌸 PokéMBTI ✨
</div>

<div class='sub'>
MBTI로 찾는 나의 운명 포켓몬
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

mbti = st.selectbox(
    "🫧 MBTI 선택",
    [""] + list(data.keys())
)

if st.button("✨ 운명 확인하기", use_container_width=True):

    if mbti:

        bar = st.progress(0)

        for i in range(101):
            time.sleep(0.008)
            bar.progress(i)

        st.balloons()

        poke, text = data[mbti]

        compatibility = random.randint(88, 100)

        st.markdown(f"""
        <div class='result'>

        <div class='poke'>
        🎀 {poke}
        </div>

        <h2 align='center'>
        {mbti}와 제일 잘 어울려!
        </h2>

        <p align='center'>
        {random.choice(quotes)}
        </p>

        <hr>

        <h3>🌷 성향</h3>

        <p>
        {text}
        </p>

        <h3>💖 싱크로율</h3>

        <h1>
        {compatibility}%
        </h1>

        <p>
        너의 분위기랑 포켓몬 에너지가 연결됐어 ✨
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.success("포켓몬이 널 선택했어 🎈")

st.write("")
st.caption("🫧 made with streamlit")
