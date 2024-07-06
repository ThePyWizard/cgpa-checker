import streamlit as st
import json
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import io

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def calculate_cgpa(credits, gpas):
    total_credits = sum(credits)
    weighted_gpa = sum(c * g for c, g in zip(credits, gpas))
    if total_credits == 0:
        return 0
    return weighted_gpa / total_credits

def plot_credits(credits):
    fig, ax = plt.subplots()
    semesters = range(1, len(credits) + 1)
    ax.bar(semesters, credits)
    ax.set_xlabel('Semester')
    ax.set_ylabel('Credits')
    ax.set_title('Credits per Semester')
    ax.set_xticks(semesters)
    return fig

def main():
    # Load Lottie animations from local files
    if "lottie_json1" not in st.session_state:
        lottie_file1 = "./animation1.json"
        st.session_state.lottie_json1 = load_lottiefile(lottie_file1)
    
    if "lottie_json2" not in st.session_state:
        lottie_file2 = "./animation2.json"
        st.session_state.lottie_json2 = load_lottiefile(lottie_file2)

    # Custom CSS
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
    }
    [data-testid="stNumberInput"] > div > div > div:nth-child(2) {
        display: none;
    }
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        padding-top: 20px;
        padding-bottom: 10px;
        margin-bottom: 0;
    }
    .tagline {
        text-align: center;
        font-size: 1.2em;
        font-style: italic;
        color: #666;
        margin-top: 0;
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='title'>GradeGuru</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>Your Personal CGPA Calculator</p>", unsafe_allow_html=True)

    if st.session_state.lottie_json1:
        st_lottie(st.session_state.lottie_json1, height=200, key="lottie1")

    num_semesters = st.number_input("Enter number of semesters", min_value=1, step=1, format="%d")

    if num_semesters:
        credits = []
        gpas = []

        for i in range(int(num_semesters)):
            st.header(f"Semester {i + 1}")
            credit = st.text_input(f"Enter credits for semester {i + 1}", value="", key=f"credit_{i}")
            gpa = st.text_input(f"Enter GPA for semester {i + 1}", value="", key=f"gpa_{i}")
            credits.append(float(credit) if credit else 0.0)
            gpas.append(float(gpa) if gpa else 0.0)

        if st.button("Calculate CGPA"):
            cgpa = calculate_cgpa(credits, gpas)
            st.success(f"Your CGPA is: {cgpa:.2f}")
            
            if st.session_state.lottie_json2:
                st_lottie(st.session_state.lottie_json2, height=200, key="lottie2")

            # Plot credits graph
            fig = plot_credits(credits)
            st.pyplot(fig)

            # Create a download button for the graph
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            btn = st.download_button(
                label="Download Credits Graph",
                data=buf.getvalue(),
                file_name="credits_graph.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()