import os
import streamlit as st

# ====== Path setup (works locally + Streamlit Cloud) ======
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def img_path(filename: str) -> str:
    return os.path.join(BASE_DIR, "images", filename)

st.set_page_config(page_title="Travel Quiz", page_icon="🧳")

# ============== Extra Credit 1: st.badge() ============== #EXTRA
st.badge("CS1301 Lab1", color="#36c9a6")
st.badge("Travel Quiz", color="#f63366")
# ======================================================== #EXTRA

st.title("🧳 Travel Preference Quiz")
st.write("Answer 5 questions to find your perfect travel style!")

# ============== Extra Credit 2: st.expander() ============== #EXTRA
with st.expander("ℹ️ Quiz Rules (Click to expand)"):
    st.write("1. Answer all 5 questions to see your result")
    st.write("2. Each question has different score weights for City/Nature")
    st.write("3. Click 'Reset' to start the quiz over")
# ========================================================== #EXTRA

st.image(img_path("travel1.jpg"), caption="Wanderlust Adventures")
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

total_qs = 5
completed_qs = sum([st.session_state.q1, st.session_state.q2, st.session_state.q3, st.session_state.q4, st.session_state.q5])
st.progress(completed_qs / total_qs) #NEW
st.caption(f"Progress: {completed_qs}/{total_qs} questions answered")

st.subheader("Current Score")
# ============== Extra Credit 3: st.metric() ============== #EXTRA
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🏙️ City Score", value=st.session_state.city)
with col2:
    st.metric(label="🌿 Nature Score", value=st.session_state.nature)
# ========================================================== #EXTRA
st.divider()

# ---------------------- Question 1: st.radio ----------------------
q1_ans = st.radio(
    "1) What's your ideal travel pace?",
    ["Fast (see as much as possible)", "Slow (relax and unwind)", "Either one is fine"],
    index=None
)
if st.button("Submit Q1"): 
    if st.session_state.q1 is True:
        st.warning("Oops! Q1 is already submitted 📝")
    else:
        if q1_ans is None:
            st.error("Please pick an option first! ⚠️")
        else:
            if q1_ans == "Fast (see as much as possible)":
                st.session_state.city += 2
            elif q1_ans == "Slow (relax and unwind)":
                st.session_state.nature += 2
            else:
                st.session_state.city += 1
                st.session_state.nature += 1
            st.session_state.q1 = True
            st.success("Q1 saved successfully! ✅")
if st.session_state.q1:
    st.info("Q1: Submitted ✔️")
st.divider()

# ---------------------- Question 2: st.multiselect ----------------------
q2_ans = st.multiselect(
    "2) What do you love to do most on trips? (Pick all that apply)",
    ["Visit museums", "Eat local food", "Go hiking", "Relax at the beach", "Explore night markets"]
)
if st.button("Submit Q2"):
    if st.session_state.q2 is True:
        st.warning("Oops! Q2 is already submitted 📝")
    else:
        if len(q2_ans) == 0:
            st.error("Please choose at least one activity! ⚠️")
        else:
            if "Visit museums" in q2_ans:
                st.session_state.city += 2
            if "Eat local food" in q2_ans:
                st.session_state.city += 2
            if "Explore night markets" in q2_ans:
                st.session_state.city += 1
            if "Go hiking" in q2_ans:
                st.session_state.nature += 2
            if "Relax at the beach" in q2_ans:
                st.session_state.nature += 2
            st.session_state.q2 = True
            st.success("Q2 submitted successfully! ✅")
st.image(img_path("travel2.jpg"), caption="City Vibes vs Nature Calm", use_column_width=True)
st.divider()

# ---------------------- Question 3: st.number_input ----------------------
steps = st.number_input(
    "3) Roughly how many steps do you walk per day on trips?",
    min_value=0,
    max_value=40000,
    value=9000,
    step=500
)
if st.button("Save Q3"):
    if st.session_state.q3 is True:
        st.warning("Oops! Q3 is already submitted 📝")
    else:
        if steps < 6500:
            st.session_state.nature += 2
        elif steps > 14000:
            st.session_state.city += 2
        else:
            st.session_state.city += 1
            st.session_state.nature += 1
        st.session_state.q3 = True
        st.success("Q3 saved successfully! ✅")
if st.session_state.q3:
    st.info("Q3: Submitted ✔️")
st.divider()

# ---------------------- Question 4: st.slider ----------------------
busy = st.slider("4) How do you feel about busy/crowded places? (0 = hate quiet → 10 = love crowded)", 0, 10, 6)
if st.button("Submit Q4"):
    if st.session_state.q4 is True:
        st.warning("Oops! Q4 is already submitted 📝")
    else:
        if busy >= 6:
            st.session_state.city += 2
        else:
            st.session_state.nature += 2
        st.session_state.q4 = True
        st.success("Q4 submitted successfully! ✅")
if st.session_state.q4:
    st.info("Q4: Submitted ✔️")
st.divider()

# ---------------------- Question 5: st.selectbox ----------------------
stay = st.selectbox(
    "5) Where would you prefer to stay during a trip?",
    ["City center (close to everything)", "Quiet countryside (far from crowds)", "Either is fine with me"],
    index=None
)
if st.button("Submit Q5"):
    if st.session_state.q5 is True:
        st.warning("Oops! Q5 is already submitted 📝")
    else:
        if stay is None:
            st.error("Please pick an option first! ⚠️")
        else:
            if stay == "City center (close to everything)":
                st.session_state.city += 2
            elif stay == "Quiet countryside (far from crowds)":
                st.session_state.nature += 2
            else:
                st.session_state.city += 1
                st.session_state.nature += 1
            st.session_state.q5 = True
            st.success("Q5 submitted successfully! ✅")
if st.session_state.q5:
    st.info("Q5: Submitted ✔️")

st.image(img_path("travel3.jpg"), caption="Your Perfect Travel Style Awaits!", use_column_width=True)
st.divider()

# ---------------------- Result Section ----------------------
st.header("🏆 Your Travel Style Result")
if st.button("Show My Result!"):
    if not (st.session_state.q1 and st.session_state.q2 and st.session_state.q3 and st.session_state.q4 and st.session_state.q5):
        st.error("Please finish all 5 questions first! ⚠️")
    else:
        st.balloons() #NEW
        c = st.session_state.city
        n = st.session_state.nature

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="🏙️ Final City Score", value=c) #EXTRA
        with col2:
            st.metric(label="🌿 Final Nature Score", value=n) #EXTRA
        st.divider()

        if c > n:
            st.subheader("You are a CITY TRAVELER! 🏙️")
            st.write("You love the hustle and bustle of cities, exploring local food, museums, and night markets—your perfect trip is filled with endless activities and new sights!")
        elif n > c:
            st.subheader("You are a NATURE TRAVELER! 🌿")
            st.write("You crave quiet and calm, hiking through trails, relaxing at the beach, and escaping the crowds—your perfect trip is all about connecting with the great outdoors!")
        else:
            st.subheader("You are a BALANCED TRAVELER! ⚖️")
            st.write("You love the best of both worlds—you can enjoy a busy city day and then unwind in a quiet nature spot! Any trip is perfect as long as it's an adventure!")

if st.button("🔄 Reset Quiz", type="secondary"):
    st.session_state.city = 0
    st.session_state.nature = 0
    st.session_state.q1 = False
    st.session_state.q2 = False
    st.session_state.q3 = False
    st.session_state.q4 = False
    st.session_state.q5 = False
    st.success("Quiz reset successfully! You can start over now ✨")
