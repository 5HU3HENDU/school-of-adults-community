import streamlit as st

st.set_page_config(
    layout="wide"
)

st.title("🚘 Driving | SofA")

st.divider()

st.subheader("🚨Important Guidelines:")
"""
- **[Learner's Licence FAQs](https://transport.delhi.gov.in/transport/frequently-asked-questions)**

- **[Car Driving Tips](https://www.spinny.com/blog/car-driving-tips/)**
"""

st.divider()

st.subheader("Driving Schools Near Me:")

user_location = st.text_input("Enter your area or city",
                              placeholder="Gomti Nagar, Lucknow")

if st.button("Search", use_container_width=True):
    if user_location:
        search_term = "best+driving+schools+near+me"
        maps_url=f"https://www.google.com/maps/search/{search_term}+{user_location.replace(' ','+')}"
        st.components.v1.html(
             f"<script>window.open('{maps_url}', '_blank');</script>",
            height=0
        )

st.divider()

st.subheader("🚗 Top Schools")
"""
- **PAN-India:** [Maruti Suzuki Driving School](https://www.marutisuzukidrivingschool.com)
- **South Delhi:** [Nanda Motor](https://nandamotordrivingschool.com)
"""







