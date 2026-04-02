import streamlit as st

st.set_page_config(layout=
                   "wide"
                  )

st.title("📱 Mobile | SofA")

tab1, tab2 = st.tabs([
    "✅ Buying Checklist", 
    "🏪 Stores "
])

with tab1:
    st.header("Buying Checklist")
    
    st.markdown("**Must have specs for 3-4 year phone:**")
    
    st.checkbox("3+ Years Software Updates")
    st.checkbox("6GB - 8GB Physical RAM")
    st.checkbox("UFS 3.1+ Storage")
    st.checkbox("128GB - 256GB Storage")
    st.checkbox("5000mAh+ Battery")
    st.checkbox("5G Support")
    st.checkbox("IP Rating (IP64+)")


with tab2:
    st.header("Stores: New, Sell, Refurbished")
    
    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("New Phones")
        st.markdown("[Amazon](https://amazon.in/mobile-phones)")
        st.markdown("[Flipkart](https://flipkart.com/mobiles)")
        st.markdown("[Croma](https://croma.com/mobile-phones)")
        st.markdown("[Reliance Digital](https://reliancedigital.in/mobiles)")
        st.markdown("[Apple.in](https://apple.com/in)")
        st.markdown("[Samsung.com](https://samsung.com/in)")
    

    with c2:
        st.subheader("**Selling**")
        st.markdown("[Cashify](https://cashify.in/sell-old-mobile-phone)")
        st.markdown("[Flipkart Reset](https://www.flipkart.com/reset-sell-store)")
    
    with c3:
        st.subheader("**Refurbished**")
        st.markdown("[Budli](https://budli.in)")
        st.markdown("[Cashify](https://cashify.in/buy-refurbished-mobile-phones)")
        st.markdown("[Grest](https://grest.in)")
    
    st.divider()
    


