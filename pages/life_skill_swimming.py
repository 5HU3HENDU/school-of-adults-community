import streamlit as st

st.set_page_config(layout="wide")

st.title("🏊‍♂️ Swimming | SofA")

st.divider()

st.subheader("**Swimming Blogs 101**")

""" 
- [Swimming guide for beginners](https://www.trainingpeaks.com/blog/beginners-guide-to-swimming/)
- [Swimming tips for adults ](https://support.myswimpro.com/en/articles/6350503-10-beginner-swim-tips-for-adults)
- [Swish swimming](https://swishswimming.com/blog-swimming-equipment-for-beginners-what-you-need-to-start-2/)
- [Water safety tips](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/water-safety.html)

"""

st.subheader("Youtube channels")
"""
- [Skills N Talents](https://www.youtube.com/@SkillsNT)
- [Effortless Swimming](https://www.youtube.com/@EffortlessSwimming)

"""

st.divider()

st.subheader("📍Find a place to swim")

"""
- [cult.fit](https://www.cult.fit/play): This is the most reliable way to find clean, temperature-controlled pools in major Indian cities. You can often buy "per session" passes if you don't want a long-term membership.
- [Playo](https://playo.co/): App to book swim slots or find local sports complexes (especially active in cities like Bangalore and Hyderabad).
- [Fitpass](https://fitpass.co.in/swimming): Premium pools and aquatic centers across India with a single membership.

"""

st.subheader("Join a class near you:")

user_location = st.text_input("Enter your area or city",
                              placeholder="Indiranagar, Bangalore")

if st.button("Search", use_container_width=True):
    if user_location:
        search_term = f"best+swimming+classes+near+{user_location.replace(' ','+')}"
        maps_url=f"https://www.google.com/maps/search/{search_term}"
      
        st.components.v1.html(
             f"<script>window.open('{maps_url}', '_blank');</script>",
            height=0
        )

st.divider()

st.subheader("🥽**Get your Gear**")

"""
- [Decathlon](https://www.decathlon.in/shop/decathlon-swimming)
- [Speedo](https://www.speedo.in/?srsltid=AfmBOoptu0TyvLPIlVnX--b2aZhpDvzlDG43C_q9u8uiBZ0zBk5q4xJO)
- [Amazon](https://www.amazon.in/s?k=swimming&crid=D1X6XVJKXXJ4&sprefix=swimming%2Caps%2C766&ref=nb_sb_noss_2)

"""



