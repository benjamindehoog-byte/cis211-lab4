import streamlit as st

# Three key-value pairs. 
club_info = {
    "name": "Campus Financial Literacy Club",
    "day": "Thursday",
    "time": "3pm",
}
# Added one additional activity for the change check. 
activities = [
    "Budgeting Workshop",
    "Investing 101",
    "Responsible Credit Usage Seminar",
    "Considering Personal Finances and the Relationship to Mental Health"
]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")

st.header("About Our Club")

# Used triple quotes here to span several lines. 
st.markdown("""
The Campus Financial Literacy Club focuses on **financial education** and provides 
an opportunity for students to explore *practical financial skills*. 
Our purpose is to help students explore responsible and personal financial skills in a judgement free environment. 
We aim to help students make informed financial decisions during college and throughout their lives.""")

st.header("Club Activities")
# Wrote a loop which explains every value.
for activity in activities:
    st.write(activity)

st.header("Details")
st.write(f"Meeting day: {club_info['day']}")
st.write(f"Meeting time: {club_info['time']}")

# Used both bold and italic text
st.header("Prepare for a visit")
st.markdown("""
- Come eager to learn, discuss and engage with the presenters and your fellow students
- Have a financial question prepared
- Consider a financial goal you'd like to achieve. How realistic is this goal? 
What do you *actually* need to do to attain your desired outcome?""")
# One meaningful, external link.
st.markdown("[Financial Education Resources](https://www.consumerfinance.gov/consumer-tools/)")

# Performed both change checks.
