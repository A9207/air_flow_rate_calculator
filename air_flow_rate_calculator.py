import streamlit as st

st.set_page_config(page_title="Flow Calculator", page_icon="📊")

st.title("Air Flow Rate Calculator For Bag Filter System")

st.write("Enter the required values below:")

# Input fields
P = st.number_input("Enter P (in meter)", min_value=0.0, format="%.2f")

st.subheader("Enter Air Velocity, V values")
V1 = st.number_input("V1", format="%.2f")
V2 = st.number_input("V2", format="%.2f")
V3 = st.number_input("V3", format="%.2f")
V4 = st.number_input("V4", format="%.2f")
V5 = st.number_input("V5", format="%.2f")

# Calculate button
if st.button("Calculate"):
    try:
        # Step 1: Average velocity
        V = (V1 + V2 + V3 + V4 + V5) / 5

        # Step 2: D calculation
        D = P / 3.142

        # Step 3: Area calculation
        A = (3.142 * D * D) / 4

        # Step 4: Flow rate in m³/h
        Q_m3h = A * V * 3600

        # Step 5: Convert to CFM
        Q_cfm = Q_m3h * 0.5886

        # Output results
        st.success("Calculation Complete!")

        st.write(f"**Average Velocity, V:** {V:.2f} m/s")
        st.write(f"**Diameter, D:** {D:.2f} m")
        st.write(f"**Ducting Cross Section Area, A:** {A:.2f} m²")
        st.write(f"### Final Q: {Q_m3h:.2f} m³/h")
        st.write(f"### Final Q: {Q_cfm:.2f} CFM")

    except Exception as e:
        st.error(f"Error: {e}")
