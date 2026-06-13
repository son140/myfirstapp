import streamlit as st
import random
import time

st.set_page_config(
page_title="PokéMBTI",
page_icon="🌷"
)

pokemon = {
"INFP": (
"이브이",
"https://img.pokemondb.net/artwork/large/eevee.jpg"
),

```
"ENFP": (
    "피카츄",
    "https://img.pokemondb.net/artwork/large/pikachu.jpg"
),

"INTJ": (
    "뮤츠",
    "https://img.pokemondb.net/artwork/large/mewtwo.jpg"
),

"INFJ": (
    "루카리오",
    "https://img.pokemondb.net/artwork/large/lucario.jpg"
)
```

}

st.title("🌷 PokéMBTI")

mbti = st.selectbox(
"MBTI 선택",
list(pokemon.keys())
)

if st.button("결과 보기"):

```
bar = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    bar.progress(i + 1)

st.balloons()

name, image = pokemon[mbti]

st.image(
    image,
    width=300
)

st.subheader(name)
```
