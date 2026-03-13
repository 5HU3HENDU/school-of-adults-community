import streamlit as st

st.set_page_config(layout="wide")

st.title("🧸 Kids | SofA")

st.divider()

st.header("📍 What are you looking for:")


user_location = st.text_input("🏠 Enter your Area or City:", 
                              placeholder="e.g. Powai, Mumbai")


col1, col2, col3 = st.columns(3)

search_items = {
    "🧸 Playschool": "best+playschools",
    "🏫 School": "top+rated+schools",
    "🎨 Hobby Classes": "kids+hobby+classes"
}


cols = [col1, col2, col3]

for i, (label, search_term) in enumerate(search_items.items()):
    with cols[i]:
        
        if st.button(label, use_container_width=True):
            if user_location:
                maps_url = f"https://www.google.com/maps/search/{search_term}+near+{user_location.replace(' ', '+')}"
                
                st.components.v1.html(
                    f"<script>window.open('{maps_url}', '_blank');</script>",
                    height=0
                )
            else:
                st.warning("Please enter a location first!")

st.divider()

st.header("🏠 Teaching at Home")

subject = st.radio(
    "Choose a subject:",
    ["🔠 English", "🔢 Maths", "🌱 Science", "🎨 Art"],
    horizontal=True
)


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

st.divider()

