import streamlit as st
import json
import random

# Page settings
st.set_page_config(
    page_title="Movie Recommendation Chatbot",
    page_icon="🎬",
    layout="centered"
)

# Load movie data
with open("intents.json", "r") as file:
    data = json.load(file)

# Title
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>🎬 Movie Recommendation Chatbot</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Find your next favourite movie!</h4>",
    unsafe_allow_html=True
)

st.write("---")

# Genre Selection
genre = st.selectbox(
    "🎭 Choose a Genre",
    ["action", "comedy", "horror", "romance", "sci-fi"]
)

# Button
if st.button("🎥 Recommend Movie"):

    movie = random.choice(data["movies"][genre])

    st.success(f"### 🍿 We recommend: **{movie}**")

    if genre == "action":
        st.info("💥 Full of action and adventure!")

    elif genre == "comedy":
        st.info("😂 Get ready to laugh!")

    elif genre == "horror":
        st.info("👻 Watch if you dare!")

    elif genre == "romance":
        st.info("❤️ A perfect romantic choice!")

    elif genre == "sci-fi":
        st.info("🚀 Explore another world!")

st.write("---")
st.caption("Created using ❤️ Python & Streamlit")