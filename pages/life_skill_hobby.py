import streamlit as st

st.set_page_config(layout = "wide")

st.title("🏓Hobbies | SofA")

st.divider()


city = st.text_input("**📍Enter your Area or City**", placeholder="e.g. Powai, Mumbai")



st.write("**Select a Hobby:**")

hobbies = [
    "🏓Pickleball", "🏺Pottery & Ceramics", "🧑🏻‍🌾Kitchen Gardening", "🏇🏻Horse Riding",
    "🏎️Go-Karting", "🎮PlayStation Gaming", "🧶Knitting & Crochet", 
    "🧗🏻Bouldering", "🐧Birdwatching", "♟️Chess", "🏏Cricket", "🎷Learning an instrument",
    "📖Language Learning", "🥾Hiking", "🧘🏻Yoga", "🎾Padel", "🏊🏻‍♂️Swimming", "💃🏻Dance"
]

cols = st.columns(4)

for i, hobby in enumerate(hobbies):
    with cols[i % 4]:
        if st.button(hobby, use_container_width=True):
            if city:
                search_query = f"best+{hobby.replace(' ', '+')}+near+{city.replace(' ', '+')}"
                maps_url = f"https://www.google.com/maps/search/{search_query}"
                

                st.components.v1.html(
                    f"<script>window.open('{maps_url}', '_blank');</script>",
                    height=0
                )
            else:
                st.warning("Please enter a city first!")

st.divider()
