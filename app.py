"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
from src.mushroom_model import predict_mushroom


observation = {
    "cap-diameter": [50],
    "stem-height": [20],
    "stem-width": [30],
    "has-ring": ["t"],
    "cap-shape": ["c"],
}

cap_shapes = {
    "Bell": "b",
    "Conical": "c",
    "Convex": "x",
    "Flat": "f",
    "Sunken": "s",
    "Spherical": "p",
    "Other": "o",
}

st.markdown("# Mushroom Poisonousness Predictor")


st.markdown(
    """
    Enter the characteristics of the mushroom to determine if it is poisonous.
    > Note: this model was trained on a generated dataset and should not be used to classify real mushrooms.
    """)

has_ring = st.checkbox("Has ring?", value=True)
observation["has-ring"] = ["t"] if has_ring else ["f"]

cap_shape = st.selectbox("Cap shape", ["Bell", "Conical", "Convex",
                                       "Flat", "Sunken", "Spherical",
                                       "Other"])

observation["cap-shape"] = [cap_shapes[cap_shape]]

cap_dai = st.number_input("Cap diameter (cm)", min_value=0.0,
                          max_value=62.34, value=50.0,
                          help="Cap diameter between 0 and 62.34 cm.")
observation["cap-diameter"] = [cap_dai]

stem_hei = st.number_input("Stem height (cm)", min_value=0.0,
                           max_value=33.92, value=20.0,
                           help="Stem height between 0 and 33.92 cm.")
observation["stem-height"] = [stem_hei]

stem_wid = st.number_input("Stem width (cm)", min_value=0.0,
                           max_value=103.91, value=30.0,
                           help="Stem width between 0 and 103.91 cm.")
observation["stem-width"] = [stem_wid]

single_obs_df = pd.DataFrame(observation)
current_prediction = predict_mushroom(single_obs_df)[0]

if current_prediction == 0:
    st.markdown("### 🍄🍄🍄 This mushroom is not poisonous.")
else:
    st.markdown("### 🤮🤮 This mushroom is poisonous.")

print(f"Model results: {current_prediction}")
print(observation)
