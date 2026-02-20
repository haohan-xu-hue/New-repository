import os
import streamlit as st

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def get_img(name):
    return os.path.join(BASE_DIR, "images", name)

st.set_page_config(page_title="Travel Quiz", page_icon="🧳")

st.title("🧳 Travel Preference Quiz")
st.write("Answer 5 questions to find your perfect travel style!")

with st.expander("Quiz Rules"):
    st.write("- Finish all 5 questions to see the result")
    st.write("- Different questions have different score weights")
    st.write("- Click Reset to start the quiz over")

st.image(get_img("travel1.jpg"), caption="Travel Pic 1")
st.divider()

if "city_score" not in st.session_state:
    st.session_state.city_score = 0
if "nature_score" not in st.session_state:
    st.session_state.nature_score = 0
if "q1" not in st.session_state:
    st.session_state.q1 = False
if "q2" not in st.session_state:
    st.session_state.q2 = False
if "q3" not in st.session_state:
    st.session_state.q3 = False
if "q4" not in st.session_state:
    st.session_state.q4 = False
if "q5" not in st.session_state:
    st.session_state.q5 = False

total_qs = 5
completed_qs = sum([st.session_state.q1, st.session_state.q2, st.session_state.q3, st.session_state.q4, st.session_state.q5])
st.progress(completed_qs / total_qs)
st.caption(f"Progress: {completed_qs}/{total_qs}")
st.divider()

q1_ans = st.radio(
    "1) What's your ideal travel pace?",
    ["Fast (see a lot)", "Slow (relax)", "Either one"],
    index=None,
    disabled=st.session_state.q1
)
if st.button("Submit Q1", disabled=st.session_state.q1):
    if q1_ans is None:
        st.error("Pick an option first!")
    else:
        if q1_ans == "Fast (see a lot)":
            st.session_state.city_score += 2
        elif q1_ans == "Slow (relax)":
            st.session_state.nature_score += 2
        else:
            st.session_state.city_score += 1
            st.session_state.nature_score += 1
        st.session_state.q1 = True
        st.success("Q1 saved!")
        st.rerun()
if st.session_state.q1:
    st.write("✅ Q1 completed")
st.divider()

q2_ans = st.multiselect(
    "2) What do you do on trips? (pick all)",
    ["Museums", "Local food", "Hike", "Beach", "Night markets"],
    disabled=st.session_state.q2
)
if st.button("Submit Q2", disabled=st.session_state.q2):
    if len(q2_ans) == 0:
        st.error("Choose at least one!")
    else:
        if "Museums" in q2_ans:
            st.session_state.city_score += 2
        if "Local food" in q2_ans:
            st.session_state.city_score += 2
        if "Night markets" in q2_ans:
            st.session_state.city_score += 1
        if "Hike" in q2_ans:
            st.session_state.nature_score += 2
        if "Beach" in q2_ans:
            st.session_state.nature_score += 2
        st.session_state.q2 = True
        st.success("Q2 done!")
        st.rerun()
st.image(get_img("travel2.jpg"), caption="City vs Nature")
st.divider()

steps = st.number_input(
    "3) Steps per day on trips (roughly)",
    min_value=0,
    max_value=40000,
    value=9000,
    step=500,
    disabled=st.session_state.q3
)
if st.button("Save Q3", disabled=st.session_state.q3):
    if steps < 6500:
        st.session_state.nature_score = st.session_state.nature_score + 2
    elif steps > 14000:
        st.session_state.city_score = st.session_state.city_score + 2
    else:
        st.session_state.city_score = st.session_state.city_score + 1
        st.session_state.nature_score = st.session_state.nature_score + 1
    st.session_state.q3 = True
    st.success("Q3 saved successfully!")
    st.rerun()
if st.session_state.q3:
    st.info("Q3: Finished")
st.divider()

busy = st.slider("4) Busy places? (0=quiet, 10=crowded)", 0, 10, 6, disabled=st.session_state.q4)
if st.button("Submit Q4", disabled=st.session_state.q4):
    if busy >= 6:
        st.session_state.city_score += 2
    else:
        st.session_state.nature_score += 2
    st.session_state.q4 = True
    st.success("Q4 done!")
    st.rerun()
if st.session_state.q4:
    st.write("Q4: ✔️")
st.divider()

stay = st.selectbox(
    "5) Where would you stay?",
    ["City center", "Quiet country", "Either is fine"],
    index=None,
    disabled=st.session_state.q5
)
if st.button("Submit Q5", disabled=st.session_state.q5):
    if stay is None:
        st.error("Pick an option first!")
    else:
        if stay == "City center":
            st.session_state.city_score += 2
        elif stay == "Quiet country":
            st.session_state.nature_score += 2
        else:
            st.session_state.city_score += 1
            st.session_state.nature_score += 1
        st.session_state.q5 = True
        st.success("Q5 saved!")
        st.rerun()

st.image(get_img("travel3.jpg"), caption="Your Travel Style")
st.divider()

st.subheader("Current Score")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="City Score", value=st.session_state.city_score)
with col2:
    st.metric(label="🌿 Nature Score", value=st.session_state.nature_score)
st.divider()

st.header("Your Travel Style Result")
all_done = st.session_state.q1 and st.session_state.q2 and st.session_state.q3 and st.session_state.q4 and st.session_state.q5

if st.button("Show result", disabled=not all_done):
    st.balloons()
    c = st.session_state.city_score
    n = st.session_state.nature_score
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Final City Score", value=c)
    with col2:
        st.metric(label="Final Nature Score", value=n)
    st.divider()

    if c > n:
        st.subheader("City Traveler! 🏙️")
        st.write("You love busy cities, exploring local food and museums!")
    elif n > c:
        st.subheader("Nature Traveler! 🌿")
        st.write("You prefer quiet places and outdoor activities like hiking!")
    else:
        st.subheader("Balanced Traveler! ⚖️")
        st.write("You enjoy both the hustle of cities and calm of nature!")

if st.button("Reset Quiz"):
    st.session_state.city_score = 0
    st.session_state.nature_score = 0
    st.session_state.q1 = False
    st.session_state.q2 = False
    st.session_state.q3 = False
    st.session_state.q4 = False
    st.session_state.q5 = False
    st.success("Reset done! You can start over!")
    st.rerun()
