import streamlit as st

def calculate_delirium_risk_score(age, spells_world_backward, oriented_to_location, nursing_illness_severity):
    # Age: <80 years (0) or >=80 years (1)
    # Correctly spells "world" backward: Yes (0) or No (1)
    # Oriented to city/state/county/hospital/floor: Yes (0) or No (1)
    # Nursing illness severity assessment: Not ill (0), Mildly ill (0), Moderately ill (1), Severely ill (1), Moribund (1)
    risk_score = age + spells_world_backward + oriented_to_location + nursing_illness_severity
    return risk_score

st.title("Delirium Risk Calculator")

nursing_illness_severity_mapping = {
    "Not ill": 0,
    "Mildly ill": 0,
    "Moderately ill": 1,
    "Severely ill": 1,
    "Moribund": 1
}

# User input for delirium risk score parameters
age = st.selectbox("Age (<80 years or >=80 years)", [0, 1], format_func=lambda x: "<80 years" if x == 0 else ">=80 years")
spells_world_backward = st.selectbox("Correctly spells 'world' backward (Yes or No)", [0, 1], format_func=lambda x: "Yes" if x == 0 else "No")
oriented_to_location = st.selectbox("Oriented to city, state, county, hospital name, and floor (Yes or No)", [0, 1], format_func=lambda x: "Yes" if x == 0 else "No")
nursing_illness_severity = st.radio(
    "Nursing illness severity assessment",
    options=list(nursing_illness_severity_mapping.keys())
)


# Get the point value for the selected nursing illness severity level
nursing_illness_severity_points = nursing_illness_severity_mapping[nursing_illness_severity]

# Calculate delirium risk score
if st.button("Calculate Delirium Risk Score"):
    risk_score = calculate_delirium_risk_score(age, spells_world_backward, oriented_to_location, nursing_illness_severity)
    st.write("Delirium Risk Score:", risk_score)

    # Interpretation of the Delirium Risk Score
    if risk_score <= 1:
        st.write("Low risk for delirium")
    elif risk_score > 1:
        st.write("High risk for delirium")
