import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    layout="wide"   
)

st.title("🚂 Train")

st.divider()

current_date = datetime.now()
days_to_add = timedelta(days=60)
new_date = current_date + days_to_add
clean_date= new_date.strftime("%A, %d %B %Y")

st.markdown("Today you can book train tickets till **"+ clean_date+"**.")

st.header("Booking Ticket")
"""
- [RailOne - Android](https://play.google.com/store/apps/details?id=org.cris.aikyam&hl=en_IN)
- [RailOne - Apple](https://apps.apple.com/in/app/railone/id6473384334)
- [AskDisha](https://askdisha.irctc.co.in/)
"""

st.header("Tracking")
"""
- [Train Status](https://www.google.com/search?q=Train+Status)
- [Where is My Train - Android](https://play.google.com/store/apps/details?id=com.whereismytrain.android&hl=en_IN)
- [Where is My Train - Apple](https://apps.apple.com/in/app/where-is-my-train-by-google/id6738965857)

"""

st.header("Food Inside Train")
"""
- [Swiggy](https://www.swiggy.com/order-food-online-in-train)
- [Menu](https://menurates.irctc.co.in/)
"""

