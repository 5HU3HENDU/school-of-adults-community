import streamlit as st

st.set_page_config(layout=
                  "wide")

st.title("🚙 Buying A Car | SofA")

st.divider()

st.info("**Key considerations when buying a car:**")
with st.expander("**New vs Old Car**", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("**New Car**")
        st.write("**pros:**")
        st.write("- New cars come with a full warranty for 3-5 years.")
        st.write("- They have the latest safety features and technology.")
        st.write("**cons:**")
        st.write("- They lose about 20-30% of value in the first year.")
    with col2:
        st.subheader("**Old Car**")
        st.write("**pros:**")
        st.write("- Old cars cost 30-50% less upfront.")
        st.write("- They show proven reliability with low kilometers.")
        st.write("**cons:** ")
        st.write("- They carry risk of hidden defects.")

with st.expander("**Budgeting and Finance (Car Loan, EMI)**"):

        st.write("- Calculate the total cost as ex-showroom price plus 15-20% for RTO, insurance, and fastag.")
        st.write("- Keep EMI below 40% of your monthly income.")
        st.write("- Check your CIBIL score above 750 for loans.")
        st.write("- Compare interest rates of 8-10% from banks like SBI or HDFC.")
        st.write("- Include processing fees in true cost calculations.")
        st.write("- Set aside ₹50k-1L yearly for fuel, servicing, and tyres.")

with st.expander("**Essential Pre-Purchasing Steps (Documentation, Test Driving, DLL)**"):
        st.write("- Take a test drive for 30+ minutes with full throttle, brakes, and AC on of the same model you are going to purchase.")
        st.write("- Check noise, vibration, harshness, and panel gaps on at least 3 models.")
        st.write("- Verify the invoice matches the car variant.")
        st.write("- Check PUC and insurance validity.")
        st.write("- Ensure your Driving License is valid with endorsements for automatic cars.")
        st.write("- Negotiate 5-15% off at two-three different dealers.")
        st.write("- Pre-approve your loan for better bargaining power.")

with st.expander("**Post-Purchasing Steps**"):
        st.write("- Activate zero-depreciation insurance and roadside assistance on the same day.")
        st.write("- Transfer RC to your name within 30 days.")
        st.write("- Log all services digitally for better resale value.")
        st.write("- Fit accessories if needed.")
        st.write("- Use an app for fuel economy and service reminders.")
