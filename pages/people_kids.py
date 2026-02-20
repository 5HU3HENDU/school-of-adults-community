import streamlit as st

st.set_page_config(layout="wide")

st.title("🧸 Kids | SofA")

st.divider()

subject = st.radio(
    "Choose a subject:",
    ["🔠 English", "🔢 Maths", "🌱 Science", "🎨 Art"],
    horizontal=True
)

st.divider()

st.header("🏠 Teaching at Home")

# English
if subject == "🔠 English":
    st.subheader("🔠 English")


    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 Stories & reading"):
            st.components.v1.html(
                "<script>window.open('https://learnenglishkids.britishcouncil.org/', '_blank');</script>",
                height=0
            )
    with col2:
        if st.button("🎧 Listen to stories"):
            st.components.v1.html(
                "<script>window.open('https://www.youtube.com/results?search_query=kids+story+read+aloud', '_blank');</script>",
                height=0
            )

# Maths
elif subject == "🔢 Maths":
    st.subheader("🔢 Maths")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Everyday maths"):
            st.components.v1.html(
                "<script>window.open('https://www.khanacademy.org/math', '_blank');</script>",
                height=0
            )
    with col2:
        if st.button("🧩 Fun maths games"):
            st.components.v1.html(
                "<script>window.open('https://math-world.e-learningforkids.org/en/grade-1/map', '_blank');</script>",
                height=0
            )

#Science
elif subject == "🌱 Science":
    st.subheader("🌱 Science (Life & surroundings)")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌍 Interactive science videos"):
            st.components.v1.html(
                "<script>window.open('https://pbskids.org/games/science', '_blank');</script>",
                height=0
            )
    with col2:
        if st.button("🔍 Essential life skills"):
            st.components.v1.html(
                "<script>window.open('https://www.youtube.com/results?search_query=life+skills+for+kids', '_blank');</script>",
                height=0
            )

# Art
elif subject == "🎨 Art":
    st.subheader("🎨 Art & Creativity")


    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎨 Art activities"):
            st.components.v1.html(
                "<script>window.open('https://pbskids.org/scribblesandink', '_blank');</script>",
                height=0
            )
    with col2:
        if st.button("🎵 Music & movement"):
            st.components.v1.html(
                "<script>window.open('https://www.youtube.com/results?search_query=music+and+movement+for+kids', '_blank');</script>",
                height=0
            )
