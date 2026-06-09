import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Bangalore House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ----------------------------------
# LOAD MODEL
# ----------------------------------

with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("columns.json", "r") as f:
    columns = json.load(f)

locations = sorted(columns[3:])

# ----------------------------------
# HEADER
# ----------------------------------

st.title("🏠 Bangalore House Price Predictor")
st.markdown(
    "Predict house prices in Bangalore based on location, area, bathrooms, and BHK."
)

st.divider()

# ----------------------------------
# INPUT SECTION
# ----------------------------------

col1, col2 = st.columns(2)

with col1:
    location = st.selectbox(
        "📍 Location",
        locations
    )

    sqft = st.number_input(
        "📐 Total Square Feet",
        min_value=300,
        max_value=10000,
        value=1200
    )

with col2:
    bath = st.selectbox(
        "🚿 Bathrooms",
        [1,2,3,4,5,6,7,8,9,10],
        index=1
    )

    bhk = st.selectbox(
        "🛏 BHK",
        [1,2,3,4,5,6,7,8,9,10],
        index=1
    )

predict = st.button("Predict Price", use_container_width=True)

# ----------------------------------
# PREDICTION
# ----------------------------------

if predict:

    x = np.zeros(len(columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location in columns:
        loc_index = columns.index(location)
        x[loc_index] = 1

    input_df = pd.DataFrame([x], columns=columns)

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]

    if prediction >= 100:
        display_price = f"₹ {prediction/100:.2f} Cr"
    else:
        display_price = f"₹ {prediction:.2f} Lakhs"

    st.divider()

    st.subheader("Estimated Property Value")

    st.success(display_price)

    st.subheader("Property Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Location", location)
    c2.metric("Area", f"{sqft} sqft")
    c3.metric("Bathrooms", bath)
    c4.metric("BHK", bhk)

st.divider()

st.caption("Built by Asmita Kabra")