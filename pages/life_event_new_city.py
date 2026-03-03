import streamlit as st

st.set_page_config(
    layout="wide"
)

st.title(" 🚛 Moving to a New City | SofA")

tab1, tab2 = st.tabs(["◉ Verified Services & Movers", "◉ Essential Documents to update"])

with tab1:
    st.subheader("Reliable Services & Moving")

    st.markdown("""
        - **[Porter](https://porter.in/packers-and-movers):** Transparent app-based pricing and live tracking.
        - **[NoBroker](https://www.nobroker.in/):** They usually assign a 'Move Manager' to handle the laborers for you.
        - **[Boxigo](https://boxigo.in/):** Reliable tech-focused shifting service.
        """)

    st.subheader("Furniture & Appliance Renting")
    st.markdown("""
        - **[Furlenco](https://www.furlenco.com/):** Full room sets and furniture.
        - **[Rentomojo](https://www.rentomojo.com/):** Best for Fridges, Washing Machines, and Microwaves.
        """)

with tab2:
    st.header("Legal & Govt. Formalities")
    
    with st.expander("**Aadhaar Address Update**", expanded=True):
        st.markdown("""
        - **Portal:** [UIDAI MyAadhaar](https://myaadhaar.uidai.gov.in/)
        - **Requirement:** A scanned PDF of your **Registered Rental Agreement**.
        - Alwys Do this first; it acts as proof for everything else (Bank, WiFi, Gas).
        """)
    with st.expander("**Bank, PAN, mobile**"):
        st.markdown(
        """
        - Update address in mobile banking and net‑banking apps.
        - Submit address‑change for:
          - Bank accounts
          - PAN card 
          - SIM cards via operator apps/portals.
        """)
        
    with st.expander("**Gas Cylinder Transfer**"):
        st.markdown("""
        - **Current City:** Visit your agency and get a **Transfer Voucher (TV)**.
        - **New City:** Hand the TV to the local distributor to get a connection immediately.
        """)
        
    with st.expander("**Vehicle RTO (NOC)**"):
        st.markdown("""
        - **Portal:** [Parivahan Sewa](https://parivahan.gov.in/)
        - You need an NOC if staying in a new state for >11 months.
        - **Hack:** Opt for **BH Series** registration when buying a car to avoid state taxes and other hassles entirely.
        """)





