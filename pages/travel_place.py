import streamlit as st

st.set_page_config(
    layout="wide"
)

st.title("🏖️ Places | SofA")

"""
**City Specific Information** 
"""

st. divider()

col1, col2, col3 = st.columns(3)
with col1:
    with st.expander("**Ludhiana**"):
        st.markdown("""
        - Chawala Chicken :material/restaurant:
        - Any Parantha Shop near Clock Tower :material/restaurantlocation_on:
        - Sharmam Shawl Factory :material/location_on:
        - Panditji Di Hatti in Chaura Bazar :material/restaurant:
        """)

with col2:
    with st.expander("**Kolkata**"):
        st.markdown("""
        - Tri Art Gallary :material/location_on:
        - KCC Art gallery :material/location_on:
        - Asia’s largest flower market :material/location_on:
        - Tram Ride :material/location_on:
        - Tiretta Bazaar :material/location_on:
        - James Prinsep Monument & Ghat :material/location_on:
        - Mishti Doi :material/restaurant:
        - Nolen gur sandesh :material/restaurant:
        - KC Das Rosogolla :material/restaurant:
        - Park street :material/location_on:
        """)

with col3:
    with st.expander("**Lucknow**"):
        st.markdown("""
        - The Residency :material/location_on:
        - National Botanical Garden :material/park:
        - Hazratganj :material/restaurantlocation_on:
        - Dilkusha Garden :material/park:
        - Aminabad Bazaar :material/restaurantlocation_on:
        - Ratti Lal(Khasta Kachodi) :material/restaurant:
        - Tundey kebabi :material/restaurant:
        - Raheem's Kulche Nihari :material/restaurant:
        - Ghanta Ghar :material/location_on:
        - Hanumant Dham :material/location_on:
        - Bada Imambara :material/castle:
        - Janeshwar Mishra Park (Asia's Largest Park) :material/Park:
        - Rumi Darwaza  :material/location_on:
        - La Martiniere College  :material/castle:
        - Chowk: Akbari Gate (for Chikan and zardozi works; Idrees Biryani) :material/restaurantlocation_on:
        - Lulu mall (hypermarket food court)  :material/restaurant:
        """)

col4, col5, col6 = st.columns(3)
with col4:
    with st.expander("**Delhi**"):
        st.markdown("""
        - Hauz Khas :material/location_on:
        - Majnu ka Tilla(Tibetan Food) :material/restaurant:
        - Jama Masjid :material/location_on:
        - Dilli Haat :material/restaurantlocation_on:
        - Qutub Minar :material/location_on:
        - Red Fort :material/fort:
        - Humayun's tomb :material/location_on:
        - Swaminarayan Akshardham :material/location_on:
        - Lotus Temple :material/location_on:
        - Janpath Market :material/location_on:
        - India Gate :material/location_on:
        """)

with col5:
    with st.expander("**Jodhpur**"):
        st.markdown("""
        - Umaid Bhawan :material/location_on:
        - Jaswant Thada :material/castle:
        - Rao Jodha Desert Rock Park :material/location_on:
        - Mehrangarh Fort(Ziplining) :material/fort:
        - Chaudhary - Mirchi Pakoda :material/restaurant:
        - Janta Sweet Home - kachodi/Jaleba :material/restaurant:
        - Mandore Garden :material/location_on:
        - Blue City Walk near Singhvi Haveli :material/location_on:
        - Toorji ka Jhalra Bavdi :material/location_on:
        - Arora Chat- Palak Patta Chat :material/restaurant:
        - Shri Misri Lal-Lassi :material/restaurant:
        - Book Cafe (open until 3am) :material/restaurant:
        - Singhoria Hills :material/location_on:
        - Ghanta Ghar/Sardar market :material/restaurantlocation_on:
        - Nehru park( Bun makhan, paneer pakoda) :material/restaurantpark:
        - Ghasmandi (rawat ka Munim, Ram Namkeen wala) :material/restaurantlocation_on:
        """)

with col6:
    with st.expander("**Amritsar**"):
        st.markdown("""
        - Kesar Dhaba :material/restaurant:
        - Brothers dhaba (Prahvan da dhaba) :material/restaurant:
        - Bhai Kulwant Singh Kulchey Wale :material/restaurant:
        - Haveli :material/restaurant:
        - Makhan Fish and Chicken Corner :material/restaurant:
        - A-one Kulfa :material/icecream:
        - Masala darbar :material/restaurant:
        - Ramdas Jalebi Wale :material/restaurant:
        - Gian Chand di lassi :material/restaurant:
        """)


col7, col8 = st.columns(2)
with col7:
    with st.expander("**Surat**"):
        st.markdown("""
        - Surat Fort :material/fort:
        - Gopal Locho (Sev Khamanis)  :material/restaurant:
        - Chirag Nankhatai :material/restaurant:
        - Dabelis Fafdas :material/restaurant:
        - Dumas beach (black sand) :material/location_on:
        - Gopi talav :material/location_on:
        - Bombay Market :material/location_on:
        - Baroda Market (clothes at cheap prices):material/location_on:
        - Swaminarayan Temple :material/location_on:
        - Shah Jamnadas Ghariwala (Gharis) :material/restaurant:
        """)

with col8:
    with st.expander("**Srinagar**"):
        st.markdown("""
        - Dal Lake (Shikara ride) 
        - Nishat Bagh (Mughal Garden)
        - Shalimar Bagh 
        - Chashme Shahi Garden
        - Shankaracharya Temple 
        - Hazratbal Shrine
        - Pari Mahal (sunset views)
        - Old City Bazaars (Pashmina, Kahwa)
        - Houseboat stay (Nigeen Lake)
        - Boulevard Road (evening walk, cycling)
        - Pampore Saffron Fields
        - Hari Parbat Fort
        """)


