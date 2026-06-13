import streamlit as st
import random
import time

st.set_page_config(
page_title="PokéMBTI ✨",
page_icon="🌷",
layout="centered"
)

data={

"INFP":(
"이브이",
"https://img.pokemondb.net/artwork/large/eevee.jpg",
"🌷 조용하지만 마음이 깊고 상상력이 풍부해. 자기만의 세계가 있고 소중한 사람을 오래 기억하는 편.",
"이브이처럼 다양한 가능성과 따뜻한 분위기를 가진 타입!"
),

"ENFP":(
"피카츄",
"https://img.pokemondb.net/artwork/large/pikachu.jpg",
"⚡ 밝고 호기심 많고 새로운 걸 좋아해. 주변에 에너지를 주는 편.",
"피카츄처럼 존재만으로 분위기를 밝게 만드는 타입!"
),

"INTJ":(
"뮤츠",
"https://img.pokemondb.net/artwork/large/mewtwo.jpg",
"🧠 계획적이고 독립적이며 깊게 생각하는 편.",
"뮤츠처럼 조용하지만 강한 존재감!"
),

"INFJ":(
"루카리오",
"https://img.pokemondb.net/artwork/large/lucario.jpg",
"💙 사람 감정을 잘 읽고 가치관이 뚜렷한 편.",
"루카리오처럼 차분하고 신뢰감 있는 타입!"
)
}

# 나머지 자동 채우기

fallback=(
"나몰빼미",
"https://img.pokemondb.net/artwork/large/rowlet.jpg",
"✨ 균형 있고 자신만의 매력이 있는 타입.",
"자연스럽고 편안한 분위기!"
)

all_mbti=[
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]

for i in all_mbti:
if i not in data:
data[i]=fallback

st.markdown("""

<style>

.stApp{

background:
linear-gradient(
180deg,
#fffdfd,
#fff7fb,
#f5f4ff
);

}

.block{

padding:38px;

background:
rgba(255,255,255,.68);

border-radius:34px;

backdrop-filter:blur(16px);

}

.card{

padding:24px;

background:white;

border-radius:30px;

box-shadow:
0 12px 40px rgba(210,210,240,.18);

}

.img{

border-radius:22px;

overflow:hidden;

}

.title{

font-size:42px;

font-weight:900;

text-align:center;

color:#666;

}

.center{
text-align:center;
}

</style>

""",unsafe_allow_html=True)

st.markdown("""

<div class='block'>
<div class='title'>
🌷 PokéMBTI
</div>

<div class='center'>
나와 닮은 포켓몬 찾기 ✨
</div>

</div>
""",unsafe_allow_html=True)

st.write("")

mbti=st.selectbox(
"🫧 MBTI 선택",
all_mbti
)

if st.button(
"💖 결과 보기",
use_container_width=True
):

```
p=st.progress(0)

for i in range(100):
    time.sleep(.008)
    p.progress(i+1)

st.balloons()

poke,img,mbti_text,why=data[mbti]

score=random.randint(91,100)

st.markdown("<div class='card'>",
unsafe_allow_html=True)

left,right=st.columns([1,1])

with left:

    st.image(
        img,
        use_container_width=True
    )

with right:

    st.markdown(
```

f"""

### 🎀 {poke}

{random.choice([
"운명 매칭 완료 💌",
"포켓몬이 널 골랐대 ✨",
"꽤 잘 어울리는 조합 🌸"
])}

### 🌷 MBTI 성향

{mbti_text}

### 🫧 왜 어울릴까?

{why}

### 💖 싱크로율

# {score}%

"""
)

```
st.markdown("</div>",
unsafe_allow_html=True)

st.success(
    f"{mbti} × {poke} 매칭 성공 🎈"
)
```

st.caption("made with 💌 streamlit")
