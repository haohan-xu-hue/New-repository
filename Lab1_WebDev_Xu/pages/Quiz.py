import os
import streamlit as st

# ====== Path setup (works locally + Streamlit Cloud) ======
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def img_path(filename: str) -> str:
    return os.path.join(BASE_DIR, "images", filename)

st.set_page_config(page_title="Travel Quiz", page_icon="🧳")

st.title("Travel Preference Quiz")
st.write("Lab 1 Quiz - answer 5 questions to find your style!")

st.image(img_path("travel1.jpg"), caption="Travel Pic 1")
st.divider()

if "city" not in st.session_state:
    st.session_state.city = 0
if "nature" not in st.session_state:
    st.session_state.nature = 0

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

st.caption("Current score")
st.write("City =", st.session_state.city, "| Nature =", st.session_state.nature)

q1_ans = st.radio(
    "1) Travel pace?",
    ["Fast (see a lot)", "Slow (relax)", "Either one"],
    index=None
)

if st.button("Submit Q1"):
    if st.session_state.q1 is True:
        st.warning("Oops! Q1 already done")
    else:
        if q1_ans is None:
            st.error("Pick an option first!")
        else:
            if q1_ans == "Fast (see a lot)":
                st.session_state.city += 2
            elif q1_ans == "Slow (relax)":
                st.session_state.nature += 2
            else:
                st.session_state.city += 1
                st.session_state.nature += 1
            st.session_state.q1 = True
            st.success("Q1 saved!")

if st.session_state.q1:
    st.write("Q1: submitted")

st.divider()

q2_ans = st.multiselect(
    "2) What do you do on trips? (pick all)",
    ["Museums", "Eat local food", "Hike", "Beach", "Night markets"]
)

if st.button("Submit Q2"):
    if st.session_state.q2 is True:
        st.warning("Q2 already submitted!")
    else:
        if len(q2_ans) == 0:
            st.error("Choose at least one!")
        else:
            if "Museums" in q2_ans:
                st.session_state.city += 2
            if "Eat local food" in q2_ans:
                st.session_state.city += 2
            if "Night markets" in q2_ans:
                st.session_state.city += 1
            if "Hike" in q2_ans:
                st.session_state.nature += 2
            if "Beach" in q2_ans:
                st.session_state.nature += 2

            st.session_state.q2 = True
            st.success("Q2 submitted!")

st.image(img_path("travel2.jpg"), caption="City vs Nature")
st.divider()

steps = st.number_input(
    "3) Steps per day on trips (roughly)",
    min_value=0,
    max_value=40000,
    value=9000,
    step=500
)

if st.button("Save Q3"):
    if st.session_state.q3 is True:
        st.warning("Q3 already done!")
    else:
        if steps < 6500:
            st.session_state.nature += 2
        elif steps > 14000:
            st.session_state.city += 2
        else:
            st.session_state.city += 1
            st.session_state.nature += 1
        st.session_state.q3 = True
        st.success("Q3 saved!")

st.divider()

busy = st.slider("4) Busy places? (0 quiet - 10 crowded)", 0, 10, 6)

if st.button("Submit Q4"):
    if st.session_state.q4 is True:
        st.warning("Q4 already submitted!")
    else:
        if busy >= 6:
            st.session_state.city += 2
        else:
            st.session_state.nature += 2
        st.session_state.q4 = True
        st.success("Q4 submitted!")

st.divider()

stay = st.selectbox(
    "5) Where would you stay?",
    ["City center", "Quiet country", "Either is fine"],
    index=None
)

if st.button("Submit Q5"):
    if st.session_state.q5 is True:
        st.warning("Q5 already done!")
    else:
        if stay is None:
            st.error("Pick an option first!")
        else:
            if stay == "City center":
                st.session_state.city += 2
            elif stay == "Quiet country":
                st.session_state.nature += 2
            else:
                st.session_state.city += 1
                st.session_state.nature += 1
            st.session_state.q5 = True
            st.success("Q5 submitted!")

st.image(img_path("travel3.jpg"), caption="Your Travel Style")
st.divider()

st.subheader("Result")

if st.button("Show result"):
    if not (st.session_state.q1 and st.session_state.q2 and st.session_state.q3 and st.session_state.q4 and st.session_state.q5):
        st.error("Finish all questions first")
    else:
        c = st.session_state.city
        n = st.session_state.nature

        st.write("Final score -> City:", c, "| Nature:", n)

        if c > n:
            st.write("City traveler")
            st.write("You like busy areas, food, and attractions.")
        elif n > c:
            st.write("Nature traveler")
            st.write("You prefer quiet places and outdoor stuff.")
        else:
            st.write("Balanced")
            st.write("A bit of both is good for you.")

if st.button("Reset"):
    st.session_state.city = 0
    st.session_state.nature = 0
    st.session_state.q1 = False
    st.session_state.q2 = False
    st.session_state.q3 = False
    st.session_state.q4 = False
    st.session_state.q5 = False
    st.success("Reset done")
