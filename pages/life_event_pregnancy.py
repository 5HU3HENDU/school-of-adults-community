import streamlit as st

st.set_page_config(layout="wide")

st.title("🤰 Pregnancy | SofA")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "Find Doctors & Hospitals", 
    "Pre-Pregnancy Planning", 
    "Hospital Delivery Checklist",
    "Contingency planning"
])

with tab1:
  
    user_location = st.text_input("Enter your city/area:",
                                  placeholder="Indira nagar, Bangalore")

    search_items = {
        "Gynecologist/Obstetrician": "gynecologist+obstetrician+ pregnancy",
        "Government Maternity Hospital": "government+maternity+hospital", 
        "Private Maternity Hospital": "private+maternity+hospital",
        "Specialty Maternity Chain": "apollo+cloundnine+motherhood",
        "Fertility Specialist/IVF": "fertility+specialist+ivf"
    }
    
    for label, search_term in search_items.items():
        if st.button(label, use_container_width=True):
            if user_location:
                maps_url = f"https://www.google.com/maps/search/{search_term}+near+{user_location.replace(' ', '+')}"
                st.components.v1.html(
                    f"<script>window.open('{maps_url}', '_blank');</script>",
                    height=0
                )

with tab2:
    
    st.subheader("Preconception Checklist")
    
    with st.expander("**Medical Tests for Wife**", expanded = True):
        st.markdown("""
        - Complete Blood Count (CBC) 
        - Thyroid profile (TSH)   
        - Blood Sugar (HbA1c)
        - Vitamin D and B12 for fertility
        - Rubella IgG for Immunity check
        - Pelvic Ultrasound
        - Blood Group + Rh
        """)
    
    with st.expander("**Medical Tests for Husband**"):
        st.markdown("""
        - Semen Analysis 
        - CBC
        - Blood Sugar
        - Vitamin D
        - Thyroid profile
        """)
    
with tab3:
    
    st.subheader("Hospital Bag:")

    """
    **DOCUMENTS** 
    """
    st.checkbox("Aadhar card of both the partners + 2 photocopies")
    st.checkbox("Pan card + 2 photocopies")
    st.checkbox("passport-size photos of both partners")
    st.checkbox("Hospital Registration form")
    st.checkbox("Insurance card + policy photocopy")
    st.checkbox("All scan report files( blood report, ultrasound, etc)")
    st.checkbox("Antenatal (ANC) Records Booklet")
    st.checkbox("Emergency contact list (mobile + on paper)")
    st.checkbox("Emergency cash + debit card + credit card")

    """
    **CLOTHES for MOM**
    """
    st.checkbox("Front-open nighty/kurta (2 sets)")
    st.checkbox("Nursing bras (2) + nursing pads")
    st.checkbox("Maternity pads (3 packs-heavy flow)")
    st.checkbox("Peri bottle (for stitch cleaning)")
    st.checkbox("Comb + toiletries")
    
    """
    **BABY KIT**
    """
    st.checkbox("Newborn diapers (size 0)")
    st.checkbox("Baby vests/onesies(4 sets)")
    st.checkbox("2 Swaddle cloth")
    
    """
    **PARTNER KIT**
    """
    st.checkbox("Phone - both partners")
    st.checkbox("charger + powerbank")
    st.checkbox("Water bottle + snacks")
    st.checkbox("Cash Rs.5000 (small notes)")


with tab4:

    st.info("Coming soon")


