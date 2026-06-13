import streamlit as st
import random
import time

st.set_page_config(
page_title="PokéMBTI 🌷",
page_icon="✨",
layout="centered"
)

# -----------------------

# 데이터

# -----------------------

pokemon_data = {

"INFP":{
"name":"이브이",
"img":"https://img.pokemondb.net/artwork/large/eevee.jpg",
"mbti":"🌷 상상력이 풍부하고 감정이 깊은 편. 자기만의 가치관을 중요하게 생각해.",
"reason":"이브이처럼 다양한 가능성과 따뜻한 분위기를 가진 타입!"
},

"ENFP":{
"name":"피카츄",
"img":"https://img.pokemondb.net/artwork/large/pikachu.jpg",
"mbti":"⚡ 밝고 호기심 많고 사람에게 에너지를 주는 타입.",
"reason":"피카츄처럼 존재만으로 분위기를 밝게 만들어!"
},

"INFJ":{
"name":"루카리오",
"img":"https://img.pokemondb.net/artwork/large/lucario.jpg",
"mbti":"💙 사람 감정을 잘 이해하고 생각이 깊은 편.",
"reason":"루카리오처럼 차분하고 신뢰감 있어!"
},

"INTJ":{
"name":"뮤츠",
"img":"https://img.pokemondb.net/artwork/large/mewtwo.jpg",
"mbti":"🧠 계획적이고 독립적이며 분석적인 타입.",
"reason":"뮤츠처럼 조용하지만 존재감 강해!"
}

}

all_mbti = [
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]

default = {
"name":"나몰빼미",
"img":"https://img.pokemondb.net/artwork/large/rowlet.jpg",
"mbti":"✨ 차분하고 자신만의 분위기가 있는 타입.",
"reason":"나몰빼미처럼 편안하고 자연스러운 매력!"
}

for mbti in all_mbti:
if mbti not in pokemon_data:
pokemon_data[mbti] = default

# -----------------------

# 스타일

# -----------------------

st.markdown("""

<style>

.stApp{
background:
linear-gradient(
180deg,
#fffefe,
#fff8fb,
#f6f4ff
);
}

.hero{

padding:35px;

background:
rgba(255,255,255,.72);

border-radius:30px;

text-align:center;

box-shadow:
0 10px 40px rgba(220,210,250,.2);

}

.card{

padding:28px;

background:white;

border-radius:30px;

box-shadow:
0 12px 40px rgba(230,210,255,.2);

}

.title{

font-size:42px;

font-weight:800;

color:#666;

}

.small{
color:#999;
}

</style>

""",
unsafe_allow_html=True)

# -----------------------

st.markdown("""

<div class="hero">

<div class="title">
🌷 PokéMBTI
</div>

<div class="small">
MBTI로 나와 닮은 포켓몬 찾기
</div>

</div>
""",
unsafe_allow_html=True)

st.write("")

selected = st.selectbox(
"🫧 MBTI 선택",
all_mbti
)

if st.button(
"💖 결과 보기",
use_container_width=True
):

```
bar = st.progress(0)

for num in range(100):
    time.sleep(0.008)
    bar.progress(num+1)

st.balloons()

info = pokemon_data[selected]

score = random.randint(90,100)

st.markdown(
```

"<div class='card'>",
unsafe_allow_html=True
)

```
col1,col2 = st.columns([1.2,1])

with col1:

    st.image(
        info["img"],
        use_container_width=True
    )

with col2:

    st.markdown(
```

f"""

# 🎀 {info["name"]}

### 🌸 MBTI 성향

{info["mbti"]}

### ✨ 왜 어울릴까?

{info["reason"]}

### 💖 싱크로율

# {score}%

포켓몬이 널 선택했어 🌷
"""
)

```
st.markdown(
```

"</div>",
unsafe_allow_html=True
)

```
st.success(
```

f"{selected} 매칭 완료 🎈"
)

st.write("")
st.caption("made with 🌷 streamlit")
