import streamlit as st

def calculate_awol_score(arousal, whispers, orientation, length_of_stay):
    # Arousal: Arousable to voice (0) or Unarousable to voice (4)
    # Whispers: Hears whispers (0) or Does not hear whispers (1)
    # Orientation: Oriented to place (0) or Disoriented to place (2)
    # Length of stay: <24 hours (0) or >=24 hours (1)
    awol_score = arousal + whispers + orientation + length_of_stay
    return awol_score

st.title("AWOL Score for Delirium Calculator")

# User input for AWOL score parameters
arousal = st.selectbox("Arousal (Arousable to voice or Unarousable to voice)", [0, 4])
whispers = st.selectbox("Whispers (Hears whispers or Does not hear whispers)", [0, 1])
orientation = st.selectbox("Orientation (Oriented to place or Disoriented to place)", [0, 2])
length_of_stay = st.selectbox("Length of stay (<24 hours or >=24 hours)", [0, 1])

# Calculate AWOL score
if st.button("Calculate AWOL Score"):
    awol_score = calculate_awol_score(arousal, whispers, orientation, length_of_stay)
    st.write("AWOL Score for Delirium:", awol_score)

    # Interpretation of the AWOL Score
    if awol_score <= 2:
        st.write("Low risk for delirium")
    elif awol_score > 2:
        st.write("High risk for delirium")

