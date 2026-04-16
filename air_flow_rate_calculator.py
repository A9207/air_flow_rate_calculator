iimport streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

st.set_page_config(page_title="Bag Filter Calculator", page_icon="🏭")

st.title("Bag Filter Air Flow Calculator")

# Inputs
P = st.number_input("Duct Perimeter, P (m)", min_value=0.0, format="%.2f")
filter_area = st.number_input("Total Filter Area (m²)", min_value=0.0, format="%.2f")
delta_p = st.number_input("Pressure Drop ΔP (Pa)", min_value=0.0, format="%.2f")

st.subheader("Air Velocity Readings (m/s)")
V1 = st.number_input("V1", format="%.2f")
V2 = st.number_input("V2", format="%.2f")
V3 = st.number_input("V3", format="%.2f")
V4 = st.number_input("V4", format="%.2f")
V5 = st.number_input("V5", format="%.2f")

velocities = [V1, V2, V3, V4, V5]

if st.button("Calculate"):
    try:
        # Average velocity
        V = sum(velocities) / len(velocities)

        # Diameter
        D = P / math.pi

        # Area
        A = (math.pi * D * D) / 4

        # Flow rate
        Q_m3h = A * V * 3600
        Q_cfm = Q_m3h * 0.5886

        # Air-to-cloth ratio
        if filter_area > 0:
            ACR = Q_m3h / filter_area
        else:
            ACR = 0

        st.success("Calculation Complete!")

        st.write(f"**Average Velocity:** {V:.2f} m/s")
        st.write(f"**Flow Rate:** {Q_m3h:.2f} m³/h")
        st.write(f"**Flow Rate:** {Q_cfm:.2f} CFM")
        st.write(f"**Air-to-Cloth Ratio:** {ACR:.2f} m³/m²/h")

        # ----------------------------
        # 📊 Graph 1: Velocity Profile
        # ----------------------------
        st.subheader("Velocity Profile")

        fig1, ax1 = plt.subplots()
        ax1.plot(range(1, 6), velocities, marker='o')
        ax1.set_title("Velocity Distribution")
        ax1.set_xlabel("Point")
        ax1.set_ylabel("Velocity (m/s)")
        ax1.grid(True)

        st.pyplot(fig1)

        # ----------------------------
        # 📊 Graph 2: Flow vs Pressure Drop
        # ----------------------------
        st.subheader("Flow Rate vs Pressure Drop")

        q_range = np.linspace(0, Q_m3h * 1.5, 50)

        # Simplified relationship (for visualization)
        dp_range = delta_p * (q_range / Q_m3h)**2 if Q_m3h > 0 else q_range

        fig2, ax2 = plt.subplots()
        ax2.plot(q_range, dp_range)
        ax2.set_xlabel("Flow Rate (m³/h)")
        ax2.set_ylabel("Pressure Drop (Pa)")
        ax2.set_title("System Resistance Curve")
        ax2.grid(True)

        st.pyplot(fig2)

    except Exception as e:
        st.error(f"Error: {e}")
