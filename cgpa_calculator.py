import streamlit as st


def calculate_cgpa(credits, gpas):
    total_credits = sum(credits)
    weighted_gpa = sum(c * g for c, g in zip(credits, gpas))
    if total_credits == 0:
        return 0
    return weighted_gpa / total_credits

st.title("CGPA Checker")

num_semesters = st.number_input("Enter number of semesters", min_value=1, step=1)

if num_semesters:
    credits = []
    gpas = []

    for i in range(num_semesters):
        st.header(f"Semester {i + 1}")
        credits.append(st.number_input(f"Enter credits for semester {i + 1}", min_value=0.0, step=0.5))
        gpas.append(st.number_input(f"Enter GPA for semester {i + 1}", min_value=0.0, max_value=10.0, step=0.1))

    if st.button("Calculate CGPA"):
        cgpa = calculate_cgpa(credits, gpas)
        st.success(f"Your CGPA is: {cgpa:.2f}")
